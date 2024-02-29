import zipfile

def crack_zip(filename):
    # 打开加密的zip文件
    zip_file = zipfile.ZipFile(filename, 'r')
    # 定义字典类型的密码列表
    with open("passwords.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if not line:
                break
            try:
                pwd = line.strip('\n')
                # 设置解压密码
                zip_file.setpassword(pwd.encode('utf-8'))
                # 解压文件
                zip_file.extractall('output')
                print('密码破解成功:' + line)
                break
            except RuntimeError:
                print('密码错误:' + line)

# 调用函数并传入ZIP文件名 然后开始破解zip 密码
crack_zip("1.zip")