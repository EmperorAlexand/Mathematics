import time
prime = True
num = 0
search = 0
result = 0
while True:
    time.sleep(0.5)
    num += 1
    prime = True
    search = 0
    for i in range(num):
        search += 1
        result = num / search
        if result.is_integer() and search != 1 or num:
            prime = False
    print(num, prime)
        
