import cv2

# 打开视频文件
cap = cv2.VideoCapture('input_video.mp4')

# 获取视频的帧率和总帧数
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# 创建一个输出视频文件
output_width = 1080
output_height = 1080
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 选择适当的编解码器
out = cv2.VideoWriter('crop.mp4', fourcc, frame_rate, (output_width, output_height))

# 读取视频帧并进行剪裁
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # 获取输入帧的宽度和高度
    input_width = frame.shape[1]
    input_height = frame.shape[0]

    # 计算剪裁区域的左上角坐标
    left = (input_width - input_height) // 2
    top = 0

    # 剪裁帧
    cropped_frame = frame[top:top+input_height, left:left+input_height]

    # 将剪裁后的帧调整为1x1画幅
    final_frame = cv2.resize(cropped_frame, (output_width, output_height))

    # 将帧写入输出视频文件
    out.write(final_frame)

# 释放视频对象和释放输出视频对象
cap.release()
out.release()
cv2.destroyAllWindows()
