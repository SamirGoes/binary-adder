def half_adder(a, b):
    sum = a ^ b
    carry = a & b

    return sum, carry


def full_adder(A, B, carry_in):
    half_adder1_sum, half_adder1_carry_out = half_adder(A, B)
    half_adder2_sum, half_adder2_carry_out = half_adder(half_adder1_sum, carry_in)

    carry_out = half_adder1_carry_out | half_adder2_carry_out

    return half_adder2_sum, carry_out

def adder(A,B,carry):
    sum, carry = full_adder(A,B,carry)

    print(f'Sum: {sum}')
    print(f'Carry: {carry}')