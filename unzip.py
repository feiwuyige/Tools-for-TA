import os
import zipfile
import rarfile
import py7zr

# 指定需要解压的文件类型
file_type = ['.zip', '.rar', '.7z' , '.RAR']



# 定义不同的函数用来解压不同的格式
def extract_zip(file_path, output_dir):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

def extract_rar(file_path, output_dir):
    with rarfile.RarFile(file_path) as rar_ref:
        rar_ref.extractall(output_dir)

def extract_7z(file_path, output_dir):
    with py7zr.SevenZipFile(file_path, mode='r') as z:
        z.extractall(path=output_dir)

def batch_extract(directory):
    count = 0
    for filename in os.listdir(directory):
        if os.path.splitext(filename)[1] in file_type:
            # 构造文件路径
            file_path = os.path.join(directory, filename)
            output_dir = os.path.join(directory, os.path.splitext(filename)[0])
            # 解压文件            
            try:
                if filename.endswith('.zip'):
                    extract_zip(file_path, output_dir)
                    print(f"解压 ZIP 文件: {filename}")
                    count += 1
                elif filename.endswith('.rar'):
                    extract_rar(file_path, output_dir)
                    print(f"解压 RAR 文件: {filename}")
                    count += 1
                elif filename.endswith('.7z'):
                    extract_7z(file_path, output_dir)
                    print(f"解压 7Z 文件: {filename}")
                    count += 1
                else:
                    print(f"不支持的文件格式: {filename}")
            except Exception as e:
                print(f"解压失败: {filename}，错误: {e}")

    print(f"总共解压了 {count} 个文件")



# 指定需要解压的文件夹路径
directory = r'你的路径'

batch_extract(directory)

print("解压完成")