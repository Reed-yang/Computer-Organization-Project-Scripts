This repository is for the scripts used in my Computer Organization Project

**crop.py** is to crop any original video into 1x1 ratio, output named *crop.mp4*

**mov2hex.py** implements a video process, can output setting OUTPUT_SIZE demo video and the hexcal *output.txt* that maintains all the video binarized information, organized by frame

**hex2reg** implements a auto-split from single output.txt file into a series of txts that store each register's hexcal input, in the path of ./reg_txt/[The txt files].txt



NOTE:

- Before run mov2hex.py, make sure the input video's frame is 1x1 ratio

---

TODO

- [x] upload to github
- [x] beautify the readme.md
- [x] analyze the opencv.resize algorithm and choose the best quality
- [x] analyze the binarization algorithm

---

Algorithm Description:
The choice of the binarization algorithm has a significant impact on the quality of the generated video, which is also the main reason for developing a script based on python+opencv rather than using a ready-made binarization video solution.
- `cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)`
  The most basic threshold-based binarization algorithm, its principle is straightforward, but the effect is often unsatisfactory, especially for videos with complex brightness and a lot of details. Only the "Bad Apple" video used this algorithm.
- `cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)`
  Also a threshold-based algorithm, but the threshold is determined through calculation.
- `cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)`
  Adaptive Gaussian binarization, which provides sharper edge processing, but may result in pixel color jitter. It is recommended to use only in videos with complex scenes.