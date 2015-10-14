from threading import Thread
from ccollatz import test_collatz_nogil


THREADS = 2


def worker(numbers):
    for i in numbers:
        test_collatz_nogil(i)

if __name__ == '__main__':
    all_numbers = range(1, 100000)
    for thread_no in range(0, THREADS):
        number_subset = (x for x in all_numbers if x % THREADS == thread_no)
        Thread(target=worker, args = (number_subset,)).start()
