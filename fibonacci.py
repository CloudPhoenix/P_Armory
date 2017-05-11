#!/mingw64/bin/python3
#
# Perform the fibonacci in python 

__author__ = 'zifengw'

def fibonacci(max):
    count, i_priv, i_cur = 0, 0, 1
    while count < max:
        yield i_cur 
        i_priv, i_cur = i_cur, i_priv + i_cur 
        count = count + 1

    return 'Done'

print('for print fibonacci:')
for value in fibonacci(5):
    print(value)

g_fib = fibonacci(5)
while True:
    try:
        i_next = next(g_fib)
        print('g_fib:', i_next)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

