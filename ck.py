import sys
import time

filename = sys.argv[1]
# time.sleep(10)
# filename = 'test.txt'
filename1 = 'ck.txt'
ck = ""
if '.txt' not in filename:
    print("请使用txt文件")
    time.sleep(3)
    # exit(0)
else:
    try:
        with open(filename, 'r') as f:
            line = f.readline()
            ck = ck + line.split(': ')[1].strip('\n') + ';'
            while line:
                line = f.readline()
                ck = ck + line.split(': ')[1].strip('\n') + ';'
    except:
        print(end='')

    with open(filename1, 'w') as f:
        f.write(ck)
    print("生成ck成功")
    time.sleep(3)
