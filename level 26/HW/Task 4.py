n = "*"
row = 6

def square():
    for first in range(3):
        print(n * 6)


def tree():
    for i in range(row):
        print(" " * (5 - i) + n * (2 * i -1) )
    print(" " * (row - 2) + n)
    print(" " * (row - 2) + n)


def romb():
    for i in range(4):
        print(" " * i, n * row)

def result():
    for i in range(1,120):
        square()
        tree()
        romb()
        
result()