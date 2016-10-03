import multiples_of

def test_is_mult_of_3():
    assert multiples_of.is_mult_of_3(1) == False
    assert multiples_of.is_mult_of_3(2) == False
    assert multiples_of.is_mult_of_3(4) == False
    assert multiples_of.is_mult_of_3(0) == True
    assert multiples_of.is_mult_of_3(3) == True
    assert multiples_of.is_mult_of_3(6) == True

def test_is_mult_of_5():
    assert multiples_of.is_mult_of_5(1) == False
    assert multiples_of.is_mult_of_5(2) == False
    assert multiples_of.is_mult_of_5(4) == False
    assert multiples_of.is_mult_of_5(0) == True
    assert multiples_of.is_mult_of_5(5) == True
    assert multiples_of.is_mult_of_5(10) == True

def test_solution():
    assert multiples_of.solution(10) == 23
    assert multiples_of.solution(1000) == 233168
