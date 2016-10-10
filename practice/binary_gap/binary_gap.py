int_to_binary = lambda n: "{0:b}".format(n)

remove_leading_zeros = lambda b: b.lstrip("0")

contain_zero = lambda b: "0" in b

last_char_is_zero = lambda b: b.endswith("0")

remove_last_char = lambda b: b[:len(b)-1]

def count_consecutive_zeros(b):

    counter, total = 0, 0

    for char in b:

        if char == "0":
            counter = counter + 1

            if counter > total: 
                total = counter

        else:
            counter = 0

    return total

def solution(n):
  
    if n == 0: return 0

    raw_binary = int_to_binary(n)

    binary = remove_leading_zeros(raw_binary)

    if not contain_zero(binary): return 0

    while last_char_is_zero(binary):
        binary = remove_last_char(binary)
  
    return count_consecutive_zeros(binary)
