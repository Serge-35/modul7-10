# -*- coding: utf-8 -*-

from pprint import pprint

file_name = 'My Soul is Dark.txt'
file = open(file_name, mode='r')
file_content = file.read()
file.close()
pprint(file_content)