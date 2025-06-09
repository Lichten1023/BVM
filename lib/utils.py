def sign_extend(value: int, bits: int) -> int:
    """Sign-extend the given value with specified bit width."""
    sign_bit = 1 << (bits - 1)
    mask = (1 << bits) - 1
    value &= mask
    return value if value < sign_bit else value - (1 << bits)
