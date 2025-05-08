#ex-1

import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes_in_range(start, end, result):
    local_primes = []
    for num in range(start, end):
        if is_prime(num):
            local_primes.append(num)
    result.extend(local_primes)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    results = []
    result_lock = threading.Lock()

    # Shared result list to be updated by threads
    shared_results = []

    # Divide range among threads
    range_size = (end - start) // num_threads

    for i in range(num_threads):
        thread_start = start + i * range_size
        thread_end = start + (i + 1) * range_size if i != num_threads - 1 else end

        thread = threading.Thread(
            target=lambda s, e: check_primes_in_range(s, e, shared_results),
            args=(thread_start, thread_end)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Prime numbers between {start} and {end}:")
    print(sorted(shared_results))

# Example
threaded_prime_checker(1, 100, num_threads=4)


#ex-2

import threading
from collections import defaultdict
import re

def process_lines(lines, word_count, lock):
    local_count = defaultdict(int)
    for line in lines:
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            local_count[word] += 1
    with lock:
        for word, count in local_count.items():
            word_count[word] += count

def threaded_word_counter(filename, num_threads=4):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // num_threads
    threads = []
    word_count = defaultdict(int)
    lock = threading.Lock()

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else total_lines
        thread = threading.Thread(target=process_lines, args=(lines[start:end], word_count, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Word counts:")
    for word, count in sorted(word_count.items()):
        print(f"{word}: {count}")

# Example usage:
# threaded_word_counter('large_text_file.txt')
