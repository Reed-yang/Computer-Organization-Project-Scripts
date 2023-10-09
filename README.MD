This repository is for the scripts used in my Computer Organization Project

**crop.py** is to crop any original video into 1x1 ratio, output named *crop.mp4*

**mov2hex.py** implements a video process, can output setting OUTPUT_SIZE demo video and the hexcal *output.txt* that maintains all the video binarized information, organized by frame

**hex2reg** implements a auto-split from single output.txt file into a series of txts that store each register's hexcal input, in the path of ./reg_txt/[The txt files].txt



NOTE:

- Before run mov2hex.py, make sure the input video's frame is 1x1 ratio

---

TODO

- [x] upload to github
- [ ] beautify the readme.md
- [ ] analyze the opencv.resize algorithm and choose the best quality
- [ ] analyze the binarization algorithm

---

将彩色图像转换为二值图像是图像处理中的一项基本任务，其目的是将图像中的信息简化为黑白两色，以便进行后续的分析或处理。以下是一些常见的彩色图像二值化算法：

1. **全局阈值法**：
   - **Otsu's方法**：Otsu's方法是一种自动确定全局阈值的技术，它试图将图像的灰度级分为两个类别，使类别内方差最小化。这是一种非常有效的方法，特别适用于具有双峰直方图的图像。
   - **Kapur's熵最大化法**：类似于Otsu's方法，但是使用了熵最大化的准则来确定阈值。

2. **局部阈值法**：
   - **Sauvola算法**：基于局部均值和标准差的自适应阈值算法，适用于光照变化较大的图像。
   - **Niblack算法**：基于局部均值和标准差的自适应阈值算法，类似于Sauvola算法。
   - **Nick算法**：对Niblack算法的改进，具有更好的性能。

3. **基于直方图形态学**：
   - **基于区域的直方图法**：利用直方图信息来确定阈值。

4. **基于颜色信息**：
   - **色彩信息的投影法**：将彩色图像投影到灰度空间来进行二值化。

5. **基于深度学习**：
   - **卷积神经网络 (CNN)**：使用深度学习模型进行图像二值化，例如使用卷积层和全连接层进行训练。

6. **基于聚类方法**：
   - **K均值聚类**：将像素分成两个类别，然后使用聚类中心作为阈值。

这些算法各自有其优缺点，适用于不同类型的图像和应用场景。例如，Otsu's方法对于具有双峰直方图的图像效果非常好，而自适应阈值方法适用于光照变化较大的图像。

算法的质量取决于许多因素，包括图像的特性、光照条件、噪声水平等等。因此，没有一种算法在所有情况下都是最佳的。通常情况下，可以通过实验和对比不同算法的结果来选择最适合特定任务的二值化算法。