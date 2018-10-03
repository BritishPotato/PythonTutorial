import time

def numAnal(n):
    """Analysis of integer"""
    print("Your number is:", n)
    print("Integer in binary:", bin(n))
    print("Integer in binary without leading zeros/minus signs",
          bin(n).lstrip("-0b"))
    print("Bit length:", int.bit_length(n))

numAnal(2)

i = 0
while i < 101:
    print(str(i) + ": "  + bin(i).lstrip("-0b"))
    time.sleep(1)
    i += 1
