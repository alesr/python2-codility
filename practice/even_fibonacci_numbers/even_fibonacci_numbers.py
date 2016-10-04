def fibonacci(n, table = []):

    while len(table) < n+1: table.append(0)

    if n <= 1: return n
   
    if table[n-1] ==  0:
        table[n-1] = fibonacci(n-1)

    if table[n-2] ==  0:
        table[n-2] = fibonacci(n-2)

    table[n] = table[n-2] + table[n-1]
    
    return table[n]

def solution(n):

    i, total = 0, 0

    fib = fibonacci(i)

    while fib < n:

        if fib % 2 == 0:
            total += fib
        
        i += 1

        fib = fibonacci(i)

    return total
