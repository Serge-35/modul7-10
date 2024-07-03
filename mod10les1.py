import time

flow_1 = [i for i in range(1, 11)]
flow_2 = list(map(chr, range(ord('a'), ord('j')+1)))
print(flow_1)
print(flow_2)
def f1():
    n = 0
    while n < len(flow_1):
        print(flow_1[n])
        print(flow_2[n])
        time.sleep(1)
        n += 1

f1()
