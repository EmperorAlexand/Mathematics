x = 1
y = 1
crn = 0
import time
while True:
    print(x)
    time.sleep(0.5)
    crn = x + y
    x = y
    y = crn
    
