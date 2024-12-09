import os
import random
import string
import time
from collections import defaultdict
from threading import Thread, Lock
from multiprocessing import Process, Manager


def generate_large_text_file(filename, size_in_mb):
    words = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"]
    with open(filename, "w") as f:
        while f.tell() < size_in_mb * 1024 * 1024:
            sentence = " ".join(random.choices(words, k=random.randint(5, 15)))
            f.write(sentence + "\n")

def count_words(filename):
    word_count = defaultdict(int)
    with open(filename, "r") as f:
        for line in f:
            for word in line.split():
                word_count[word] += 1
    return word_count

def count_words_multithreading(filename):
    word_count = defaultdict(int)
    lock = Lock()

    def worker(lines):
        local_count = defaultdict(int)
        for line in lines:
            for word in line.split():
                local_count[word] += 1
        with lock:
            for word, count in local_count.items():
                word_count[word] += count

    threads = []
    with open(filename, "r") as f:
        lines = f.readlines()
        chunk_size = len(lines) 
        for i in range(0, len(lines), chunk_size):
            t = Thread(target=worker, args=(lines[i:i + chunk_size],))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()
    return word_count

def count_words_multiprocessing(filename):
    manager = Manager()
    word_count = manager.dict()

    def worker(lines):
        local_count = defaultdict(int)
        for line in lines:
            for word in line.split():
                local_count[word] += 1
        for word, count in local_count.items():
            if word in word_count:
                word_count[word] += count
            else:
                word_count[word] = count

    processes = []
    with open(filename, "r") as f:
        lines = f.readlines()
        chunk_size = len(lines)
        for i in range(0, len(lines), chunk_size):
            p = Process(target=worker, args=(lines[i:i + chunk_size],))
            processes.append(p)
            p.start()

    for p in processes:
        p.join()
    return dict(word_count)

def measure_performance(filename):
    start_time = time.time()
    count_words_sequential(filename)
    sequential_time = time.time() - start_time

    start_time = time.time()
    count_words_multithreading(filename)
    threading_time = time.time() - start_time

    start_time = time.time()
    count_words_multiprocessing(filename)
    multiprocessing_time = time.time() - start_time

    print(f"Sequential Time: {sequential_time:.2f} seconds")
    print(f"Multithreading Time: {threading_time:.2f} seconds")
    print(f"Multiprocessing Time: {multiprocessing_time:.2f} seconds")

    print(f"Speedup (Multithreading): {sequential_time / threading_time:.2f}")
    print(f"Speedup (Multiprocessing): {sequential_time / multiprocessing_time:.2f}")

if name == "main":
    filename = "large_text_file.txt"
    if not os.path.exists(filename):
        print("Generating large text file...")
        generate_large_text_file(filename, size_in_mb=100)

    print("Measuring performance...")
    measure_performance(filename)
