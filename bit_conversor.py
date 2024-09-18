def to_bits(value, size=4):
    return bin(value)[2:].zfill(size)

def to_decimal(value):
    return int(value, 2)