'''

递归和循环


写一个函数，输入n，求斐波那契数列的第n项
'''


def fibo(n):
    if n == 0:
        return  0
    if n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n -2)
print(fibo(5))

