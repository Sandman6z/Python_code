#forget_password.py

import os
import sys
import datetime

#from unrar import rarfile
import unrar
import rarfile

def Crack(Encrypted_file):
    bFound = False
    fp = rarfile.RarFile(Encrypted_file)

    #使用循环尝试
    start = 0
    stop = 9999
    for i in range(start, stop):
        pwd = str(i).zfill(4)

        try:
            fp.extractall(path = "./aaa", pwd = pwd)

            print('\n暴破成功，密码：' + pwd)
            bFound = True
            fp.close()
        
        except Exception as e:
            print("\r已尝试", '{:.0%}'.format((i - start) / (stop - start)), end="")

        if bFound:
            break

if __name__ == '__main__':

    starttime = datetime.datetime.now()
    Crack(sys.argv[1])
    endtime = datetime.datetime.now()

    print("共耗时：", (endtime - starttime).seconds, "秒")