def test_collatz(x):
    while x != 1:
        if x % 2:
            x = x * 3 + 1
        else:
            x //= 2

if __name__ == '__main__':
    for i in range(1, 100000):
        test_collatz(i)
