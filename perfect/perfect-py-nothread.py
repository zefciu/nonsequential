def is_perfect(n):
    """Check if given number is a perfect number"""
    sum_ = 0
    for i in range(1, n):
        if not n % i:
            sum_ += i
    return sum_ == n

for i in range(1, 10000):
    if is_perfect(i):
        print(i)
