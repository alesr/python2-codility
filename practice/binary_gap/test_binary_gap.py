import binary_gap

def test_int_to_binary():
    assert binary_gap.int_to_binary(0) == "0"
    assert binary_gap.int_to_binary(1) == "1"
    assert binary_gap.int_to_binary(2) == "10"
    assert binary_gap.int_to_binary(9) == "1001"
    assert binary_gap.int_to_binary(529) == "1000010001"
    assert binary_gap.int_to_binary(0) != "01"

def test_contain_zero():
    assert binary_gap.contain_zero("1") == False
    assert binary_gap.contain_zero("11") == False
    assert binary_gap.contain_zero("0") == True
    assert binary_gap.contain_zero("10") == True
    assert binary_gap.contain_zero("101") == True

def test_last_char_is_zero():
    assert binary_gap.last_char_is_zero("1") == False
    assert binary_gap.last_char_is_zero("11") == False
    assert binary_gap.last_char_is_zero("10") == True
    assert binary_gap.last_char_is_zero("100") == True
    assert binary_gap.last_char_is_zero("1101") == False


def test_remove_trailing_zero():
    assert binary_gap.remove_trailing_zero("10") == "1"
    assert binary_gap.remove_trailing_zero("100") == "10"
    assert binary_gap.remove_trailing_zero("010") == "01"
    assert binary_gap.remove_trailing_zero("0") == ""
    assert binary_gap.remove_trailing_zero("1001000") == "100100"


def test_count_consecutive_zeros():
    assert binary_gap.count_consecutive_zeros("101") == 1
    assert binary_gap.count_consecutive_zeros("1001") == 2
    assert binary_gap.count_consecutive_zeros("11") == 0
    assert binary_gap.count_consecutive_zeros("0") == 1

def test_solution():
    assert binary_gap.solution(0) == 0
    assert binary_gap.solution(1) == 0
    assert binary_gap.solution(2) == 0
    assert binary_gap.solution(9) == 2
    assert binary_gap.solution(5) == 1
    assert binary_gap.solution(529) == 4
    assert binary_gap.solution(1041) == 5
