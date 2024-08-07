import multiprocessing
import datetime

def read_info(name):
    all_data = []
    file = open(name, mode='r')
    my_line = file.readline()
    while my_line:
        my_line = file.readline()
        if my_line != '':
            all_data.append(my_line)
        else:
            break
    file.close()

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start = datetime.datetime.now()
# for i in range(len(filenames)):
#     my_file = filenames[i]
#     read_info(my_file)
# end = datetime.datetime.now()
# print(end - start, ' - (линейный)')


if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start1 = datetime.datetime.now()
        pool.map(read_info, filenames)
        end1 = datetime.datetime.now()
    print(end1 - start1, ' - (многопроцессный)')

# 0:00:06.825262  - (линейный)
# 0:00:02.545273  - (многопроцессный)
