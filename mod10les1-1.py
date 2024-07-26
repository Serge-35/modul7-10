import threading
import time

flow_1 = [i for i in range(1, 11)]
flow_2 = list(map(chr, range(ord('a'), ord('j')+1)))

def f1():
    n = 0
    while n < len(flow_1):
        print(flow_1[n])
        time.sleep(1)
        n += 1

def f2():
    n = 0
    while n < len(flow_2):
        print(flow_2[n])
        time.sleep(1.01)
        n += 1


t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)

t1.start()
t2.start()

t1.join()
t2.join()

