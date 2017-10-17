# -*- coding: utf-8 -*-
# 我的代码里面有很多大文件，不是代码，是产生的文件，需要把这些文件删掉
import os
import os.path
import logging

handler = logging.FileHandler('./log.txt', 'w', encoding='utf-8')
formatter = logging.Formatter("%(message)s")
handler.setFormatter(formatter)
root_logger = logging.getLogger()
root_logger.addHandler(handler)
root_logger.setLevel(logging.DEBUG)

# logger = logging.getLogger('mylogger')
# logger.setLevel(logging.DEBUG)

# logging.basicConfig(filename='./log.txt', level=logging.DEBUG, filemode='w')

def delete_empty_files(path):
    total = 0
    total_size = 0
    for parent, dirname, filenames in os.walk(path):
        # print('parent={}, dirname={}, filenames={}'.format(parent, dirname, filenames))
        # 会获取把目录名，子目录列表，子文件列表
        # parent=D:/tmp/all_codes/python核心编程,
        # dirname=['ch01', 'ch02', 'ch03', 'ch04', 'ch05', 'ch06', 'ch07', 'ch08',
        #   'ch09', 'ch10', 'ch11', 'ch12', 'ch13', 'ch14', 'ch15'],
        # filenames=['COLOPHON.txt', 'COPYRIGHT.txt', 'LICENSE.txt', 'ls-lFR.txt', 'README.html']
        for file in filenames:
            if file.lower().endswith(('.txt', '.py', '.cpp', '.h', '.c', '.cc', 'readme',
                                      'makefile', '.md', '.php', '.html', '.cgi')):
                continue
            file_path = os.path.join(parent, file)
            file_size = os.path.getsize(file_path)/1024  # 获取文件大小 KB
            total_size += file_size

            print("{} KB, file_path = {}".format(file_size, file_path))
            try:
                os.remove(file_path)  # 删除文件
            except Exception as e:
                error_info = "rm file err,file={},err={}".format(file_path, e)
                # print(u"rm file err,file={} strtype={}".format(file_path, type(file_path)))
                print('err info={}, type={}'.format(error_info, type(error_info)))
                root_logger.error(error_info.encode('utf-8'))
        total += len(filenames)
    print('total={}, total_rm_size={} KB'.format(total, total_size))


def delete_empty_dir(path):
    empty_dir_list = []
    for parent, dirname, filenames in os.walk(path):
        if not filenames and not dirname:  # 如果这个目录下面没有目录，也没有文件，就是空目录
            empty_dir_list.append(parent)
    print('length of empty dir={}'.format(len(empty_dir_list)))
    for dir_name in empty_dir_list:
        print("empty dir = ", dir_name)
        try:
            os.rmdir(dir_name)  # 删除文件夹
        except Exception as e:
            root_logger.error("rm dir err,dir_name={},err={}".format(dir_name, e))


if __name__ == '__main__':
    # path = 'D:/tmp/test_git_windows/'
    root_logger.info("您好")
    path = 'D:/tmp/all_codes/'
    delete_empty_files(path)
    print('====================\n'*5)
    delete_empty_dir(path)

    # import ipdb
    # ipdb.set_trace()

    print("end")
