import numpy as np

# AND
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <=  0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

def full_adder(A, B, C_in):
    s1 = XOR(A, B)
    S = XOR(s1, C_in)
    s3 = AND(C_in, s1)
    s4 = AND(A, B)
    C_out = OR(s3, s4)
    return S, C_out

input = [[0, 0, 0],
         [0, 0, 1],
         [0, 1, 0],
         [0, 1, 1],
         [1, 0, 0],
         [1, 0, 1],
         [1, 1, 0],
         [1, 1, 1]]
for A, B, C_in in input:
    print(f'입력 A = {A}, B = {B}, C_in = {C_in}')
    S, C_out = full_adder(A, B, C_in)
    print(f'출력 S = {S}, C_out = {C_out}')

