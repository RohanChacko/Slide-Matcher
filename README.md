# Slide Matcher

Digital Signal Analysis & Applications Project | Spring 2019

## Team Get Rect
[Rohan Chacko](https://github.com/RohanChack) [AadilMehdi Sanchawala](https://github.com/aadilmehdis) [Sumaid Syed](https://github.com/Sumaid)

## Requirements
* Python3
* Opencv-python
* Matplotlib
* numpy

## Run
  ```python3
    python3 move.py
  ```
  This will copy frames and slides from each sub-directory of ‘Dataset’ to ‘frames’
  and ‘slides’ sub-directores respectively. ‘frames’ and ‘slides’ are sub-directories of
  ‘full-test’ directory. Each filename is prefixed with the directory name it was copied from.

  ```python3
    main.py ./sample_set/slides ./sample_set/frames
  ```

## Method
Takes frames from a specified directory and finds its best match from slides by performing template matching using OpenCV

## Output
Saves to `pred_output.log` by default. Printed on the terminal by default.

## Observations

* Total failed test cases : 54/835
* Test cases failure because of inherent errors in dataset : 32/835
* Accuracy (After adjusting for data set failures) : 97.36%  
We have analyzed each failed test case and provided a detailed report in ‘Observation
Report.pdf’.
