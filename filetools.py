def write_file(file_path,content):
    """
    file_path:要写入的文件路径
    content：要写入的内容
    """
    with open(file_path,'w') as f:
        f.write(content)


def read_file(file_path):
    """
    方法名:读取文件
    file_path：要读取的文件路径
    """
    with open(file_path,'r') as f:
        t=f.readline()

        return t 
