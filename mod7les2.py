# -*- coding: utf-8 -*-

file_name = 'My Soul is Dark.txt'
with open(file_name, mode='r') as file:
    for line in file:
        print(line, end='')

print('\n')
print(file.closed)

# оператор with - автоматически закрывает файл.




