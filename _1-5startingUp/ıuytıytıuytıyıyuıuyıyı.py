import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='\n')
    time.sleep(1)
    timeLeft = timeLeft - 1

   # TODO: At the end of the countdown, play a sound file.
