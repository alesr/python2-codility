def int_to_binary(n):
  return "{0:b}".format(n)

def contain_zero(b):
  return "0" in b

def last_char_is_zero(b):
  return b.endswith("0")

def remove_trailing_zero(b):
  return b[:len(b)-1]

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

  binary = int_to_binary(n)

  if not contain_zero(binary): return 0

  while last_char_is_zero(binary):
    binary = remove_trailing_zero(binary)
  
  return count_consecutive_zeros(binary)

print solution(2)