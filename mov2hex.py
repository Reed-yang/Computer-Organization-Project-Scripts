import cv2
import numpy as np

OUT_WIDTH = 32
OUT_HEIGHT = 32


def show_frame(binary_frame):
    # 将数组转化为图像
    img = cv2.cvtColor(binary_frame, cv2.COLOR_GRAY2BGR)
    # 将图像写入文件
    cv2.imwrite('output.png', img)
    # 显示图像
    cv2.imwrite('output.png', img)


def convert_frame_to_hex(frame):
    # 将图像转化为黑白
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 缩小图像尺寸到32x32
    small_frame = cv2.resize(gray_frame, (OUT_WIDTH, OUT_HEIGHT))
    
    # 将图像转化为二值图像
    _, binary_frame = cv2.threshold(small_frame, 128, 255, cv2.THRESH_BINARY)

    # 将二值图像转化为一维数组
    binary_data = binary_frame.flatten() // 255

    # show_frame(binary_frame)

    # 将一维数组转化为32个4字节16进制数，字符串长度固定
    hex_data = [format(int(''.join(map(str, binary_data[i:i+32])), 2), '08X') for i in range(0, len(binary_data), 32)]
    
    return binary_data, hex_data


# 读取原始视频
cap = cv2.VideoCapture('crop.mp4')

# 获取原始视频的帧率、分辨率等信息
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建一个视频编写对象，用于保存新视频
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (OUT_WIDTH, OUT_HEIGHT), isColor=False)

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # 处理帧并输出16进制数
    binary_data, hex_data = convert_frame_to_hex(frame)
    
    # 将所有16进制数写入文件,每四个16进制数为一行,每帧之间空一行
    with open('output.txt', 'a') as f:
        for i in range(0, len(hex_data), 4):
            f.write(' '.join(hex_data[i:i+4]) + '\n')
        f.write('\n')

    # 将二值数组转化为32x32的二值图像
    binary_frame = np.array(binary_data).reshape((OUT_WIDTH, OUT_HEIGHT)).astype(np.uint8) * 255
    # scaled_frame = cv2.resize(binary_frame, (1080, 1080))
    # # 将图像写入输出视频
    out.write(binary_frame)

    frame_count += 1

cap.release()
out.release()

