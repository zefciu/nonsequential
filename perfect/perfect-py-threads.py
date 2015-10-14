from threading import Thread

THREADS = 2

def is_perfect(n):
    """Check if given number is a perfect number"""
    sum_ = 0
    for i in range(1, n):
        if not n % i:
            sum_ += i
    return sum_ == n

def worker(thread_no):
    for i in range(1, 10000):
        if i % THREADS != thread_no:
            continue
        if is_perfect(i):
            print(i)


if __name__ == '__main__':
    all_numbers = range(1, 100)
    threads = []
    for thread_no in range(0, THREADS):
        thread = Thread(
            target=worker,
            args = (thread_no,)
        )
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
