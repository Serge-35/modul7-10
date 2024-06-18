my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
def is_odd (x):
    return x % 2

def f1 (x):
    return x ** 2

res_1 = filter(is_odd, my_list)
res_2 = map(f1, res_1)
print(list(res_2))