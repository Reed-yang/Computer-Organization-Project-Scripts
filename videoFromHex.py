import cv2
import numpy as np

# 读取hex_data
hex_data = ['FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00','FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00','FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00','FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', '00']

binary_data = []

# 将每个16进制数转换为8位二进制数，并添加到二进制数组中
for hex_num in hex_data:
    binary_num = bin(int(hex_num, 16))[2:].zfill(8)
    binary_data.extend([int(bit) for bit in binary_num])

# 创建一个视频编写对象，用于保存新视频
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video.mp4', fourcc, 30, (32, 32), isColor=False)

# 将32x32的点阵二值图像保存为视频输出
for i in range(300):
    # 将二值数组转化为32x32的二值图像
    binary_frame = np.array(binary_data).reshape((32, 32)).astype(np.uint8) * 255
    
    # # 将二值图像转化为彩色图像
    # color_frame = cv2.cvtColor(binary_frame, cv2.COLOR_GRAY2BGR)
    
    # # 将彩色图像写入输出视频
    out.write(binary_frame)

    # img = binary_frame
    #     # 将点阵数据写入图像
    # for i in range(32):
    #     for j in range(32):
    #         if binary_data[i*32+j] == 1:
    #             img[i, j] = 255

    # # 显示图像
    # cv2.imwrite('output.png', img)


# 释放视频编写对象
out.release()