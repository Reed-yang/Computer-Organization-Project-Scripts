This repository is for the scripts used in my Computer Organization Project

**crop.py** is to crop any original video into 1x1 ratio, output named *crop.mp4*

**mov2hex.py** implements a video process, can output setting OUTPUT_SIZE demo video and the hexcal *output.txt* that maintains all the video binarized information, organized by frame

**hex2reg** implements a auto-split from single output.txt file into a series of txts that store each register's hexcal input, in the path of ./reg_txt/[The txt files].txt



NOTE:

- Before run mov2hex.py, make sure the input video's frame is 1x1 ratio

---

TODO

- [ ] upload to github
- [ ] beautify the readme.md