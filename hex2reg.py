import re
import os

OUT_SIZE = 64
REG_NUM = OUT_SIZE*OUT_SIZE//32

def format_hex(input_file, output_file):
    with open(input_file, 'rb') as f: 
            data = f.read().decode('utf-8', errors='ignore')  # 指定编码格式    

    data = re.sub(r'\/\/.*\n', '\r\n', data) # 删除注释
    # 以空格或换行划分
    hex_values = re.split(r'\s+', data)
    hex_values = [x.strip() for x in hex_values]

    # formatted_values = [val[2:] for val in hex_values if val]  # 删除 '0x' 前缀
    formatted_values = hex_values

    ### continuous output in single file
    # with open(output_file, 'w') as f:
    #     for i, val in enumerate(formatted_values):
    #         f.write(val)
    #         if (i + 1) % 128 == 0:
    #             f.write('\n\n')
    #         elif (i + 1) % 16 == 0:
    #             f.write('\n')
    #         elif (i + 1) % 4 == 0:
    #             f.write(' ')

    # 在新建文件夹中存储txt
    if not os.path.exists('reg_txt'):
        os.mkdir('reg_txt')
    # for i in range(32):
    #     filename = f"{os.path.splitext(output_file)[0]}_{i}.txt"
    #     # filename = f"reg_txt/output_file_{i}.txt"
    #     with open(filename, 'w') as f:
    #         for j in range(len(formatted_values) // 128):
    #             for k in range(4):
    #                 f.write(formatted_values[i * 4 + k + j * 128])
    #             f.write(' ')
    for i in range(REG_NUM):
        filename = f"reg_txt/output_file_{i}.txt"
        with open(filename, 'a') as f:
            # f.write('v2.0 raw\n') 
            for j in range(len(formatted_values) // REG_NUM):
                    f.write(formatted_values[i + j * REG_NUM])
                    f.write('\n') 


if __name__ == '__main__':
    input_file = 'output_3.txt'  
    output_file = 'output.txt' 
    format_hex(input_file, output_file)
