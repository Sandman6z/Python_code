import sys
sys.path.append(r'C:\ProgramData\Anaconda3\Lib\site-packages')  #否则会无法调用myqr库

from MyQR import myqr

myqr.run(words = 'https://space.bilibili.com/4790202/',
         version = 5,   #容错率
         level = 'H',   #纠错水平
         picture = 'D:\\Python_Code\\feifeisleep.jpg',
         colorized = True,
         save_name = 'feifeisleepQR.png')
