import time
import subprocess
import sys

#倒计时时间在命令行输入
djs = sys.argv[1]

timeLeft = int(djs)
#pirnt('本次倒计时的时间是:%秒'%timeLeft)

while timeLeft>0:
    print(timeLeft,end='')
    time.sleep(1)
    timeLeft = timeLeft - 1
#at the end of the countdown,play a sound file
subprocess.Popen(['start','alarm.wav'],shell=True)