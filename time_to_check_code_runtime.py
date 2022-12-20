import time
import timeit


def for_test(number):
    my_list = []
    for num in range(1, number + 1):
        my_list.append(num)
    return my_list


def while_test(number):
    my_list = []
    counter = 1
    while counter <= number:
        my_list.append(counter)
        counter += 1
    return my_list


begining = time.time()
for_test(1000000)
ending = time.time()
print(ending - begining)

begining = time.time()
while_test(1000000)
ending = time.time()
print(ending - begining)


def time_it_check(declaration, setup, times):
    length = timeit.timeit(declaration, setup, number=times)
    print(length)


time_it_check(''' 
for_test(10) 
''', ''' 
def for_test(number):
    my_list = []
    for num in range(1, number + 1):
        my_list.append(num)
    return my_list
    ''', 10000000)

time_it_check(''' 
while_test(10) 
''',
''' 
def while_test(number):
    my_list = []
    counter = 1
    while counter <= number:
        my_list.append(counter)
        counter += 1
    return my_list
    ''', 10000000 )
