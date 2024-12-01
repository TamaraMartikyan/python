import random
import time
import os

def file(filename):
    file = open(filename, 'w')
    for _ in range(100):
        file.write(' '.join(map(str, [random.randint(1, 100) for _ in range(20)])) + '\n')
    file.close()

def convert_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    return [list(map(int, line.split())) for line in lines]


def write_filtered_data(filename, data):
    file = open(filename, 'w')
    for line in data:
        file.write(' '.join(map(str, line)) + '\n')
    file.close()


def read_file_as_generator(filename):
    file = open(filename, 'r')
    for line in file:
        yield list(map(int, line.split()))
    file.close()


def execution_time_decorator(func):
    print('Decorator created')
    def wrapper(*args, **kwargs):
        print(f'Executing {func.__name__}')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Execution time of {func.__name__}: {end_time - start_time} seconds')
        return result
    return wrapper



@execution_time_decorator
def file(filename):

    if not os.path.exists(filename):
        print(f'File {filename} does not exist. Creating it')
        file(filename)

    converted_data = convert_file(filename)

    filtered_data = [list(filter(lambda x: x > 40, line)) for line in converted_data]
    write_filtered_data(filename, filtered_data)
    


    generator = read_file_as_generator(filename)
    for _ in range(5):
        print(next(generator))

filename = "random_numbers.txt"
file(filename)
