is_mult_of_3 = lambda n: n % 3 == 0

is_mult_of_5 = lambda n: n % 5 == 0

def solution(n):

    sum = 0

    for i in xrange(n):
        
        if is_mult_of_3(i) or is_mult_of_5(i):
            sum += i

    return sum
