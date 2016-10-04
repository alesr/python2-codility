import even_fibonacci_numbers

def test_fibonacci():
    assert even_fibonacci_numbers.fibonacci(0) == 0
    assert even_fibonacci_numbers.fibonacci(1) == 1
    assert even_fibonacci_numbers.fibonacci(2) == 1
    assert even_fibonacci_numbers.fibonacci(3) == 2
    assert even_fibonacci_numbers.fibonacci(4) == 3
    assert even_fibonacci_numbers.fibonacci(5) == 5
    assert even_fibonacci_numbers.fibonacci(50) == 12586269025
    assert even_fibonacci_numbers.fibonacci(100) == 354224848179261915075


def test_solution():
    assert even_fibonacci_numbers.solution(9) == 10
    assert even_fibonacci_numbers.solution(4000000) == 4613732
