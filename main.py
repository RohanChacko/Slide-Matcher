import sys
import cv2
import glob
import os
import re
import numpy as np

class SlideMatcher :
    """Match noisy frames with slides"""

    def __init__(self) :
        """Initialize SlideMatcher Class"""

        self.slidesLocation = ''
        self.framesLocation = ''
        self.outputFile = 'pred_output.log'
        self.slidesData = []
        self.framesData = []
        self.slidesNames = []
        self.framesNames = []
        self.matchedSlides = []
        self.MAX = 1000000
        self.error_rate = 0

    def inputTaker(self) :
        """Take input from given locations and store in arrays"""

        for slideFile in sorted(glob.glob(self.slidesLocation+'/*.jpg')):
            self.slidesNames.append(slideFile.split('/')[-1])
            imageData = cv2.imread(slideFile)
            imageData = cv2.resize(imageData, (1800, 1398))
            self.slidesData.append(imageData)

        for frameFile in sorted(glob.glob(self.framesLocation+'/*.jpg')):
            self.framesNames.append(frameFile.split('/')[-1])
            imageData = cv2.imread(frameFile)
            imageData = cv2.resize(imageData, (1800, 1398))
            self.framesData.append(imageData)

    def meanSquareError(self, image_a, image_b):
        """Calculates mean squared error between two images"""

        err = np.sum((image_a.astype("float") - image_b.astype("float")) ** 2)
        err /= float(image_a.shape[0] * image_b.shape[1])

        return err

    def templateMatcher(self, frame, slide):
        """Calculates the template matching result for a template and an image"""

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        slide_gray = cv2.cvtColor(slide, cv2.COLOR_BGR2GRAY)
        w, h = frame_gray.shape[::-1]
        w = int(w)
        h = int(h)

        res_1 = cv2.matchTemplate(slide_gray[0: int(h/2), 0: int(w/2)],frame_gray[0: int(h/2), 0: int(w/2)],cv2.TM_CCOEFF_NORMED)
        res_2 = cv2.matchTemplate(slide_gray[0: int(h/2), int(w/2): w],frame_gray[0: int(h/2), int(w/2): w],cv2.TM_CCOEFF_NORMED)
        res_3 = cv2.matchTemplate(slide_gray[int(h/2): h, 0: int(w/2)],frame_gray[int(h/2): h, 0: int(w/2)],cv2.TM_CCOEFF_NORMED)
        res_4 = cv2.matchTemplate(slide_gray[int(h/2): h, int(w/2): w],frame_gray[int(h/2): h, int(w/2): w],cv2.TM_CCOEFF_NORMED)

        return max(max((res_1))) + max(max((res_2))) + max(max((res_3))) + max(max((res_4)))


    def matchImages(self):
        """Finds best matching slide with respect to each frame"""

        for ind, frame in enumerate(self.framesData):
            cur_err = self.MAX
            cur_index = -1
            for i, slide in enumerate(self.slidesData):
                temp = -1 * self.templateMatcher(frame, slide)
                if temp < cur_err:
                    cur_err = temp
                    cur_index = i
            self.matchedSlides.append(self.slidesNames[cur_index])

    def outputGiver(self) :
        """Writes output to a file"""

        f = open(self.outputFile, "w")
        for i in range(len(self.framesNames)):
            print(self.framesNames[i]+' '+self.matchedSlides[i]+'\n')
            f.write(self.framesNames[i]+' '+self.matchedSlides[i]+'\n')

        f.close()

    def run(self) :
        """Main Engine of class"""

        self.inputTaker()
        self.matchImages()
        self.outputGiver()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print ('Command: python3 main.py <path/to/slides/directory> <path/to/frames/directory>')
        sys.exit(1)

    S = SlideMatcher()
    S.slidesLocation = str(sys.argv[1])
    S.framesLocation = str(sys.argv[2])
    S.run()
