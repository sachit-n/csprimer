import pytest
from varint_encode_decode import get_num_of_bits, get_num_bytes, get_curr_byte_val, encode

def test_get_num_of_bits():
    test_cases = [(150, 8)]

    for case, expected in test_cases:
        assert get_num_of_bits(case) == expected


def test_get_num_bytes():
    test_cases = [(150, 2), (128, 2), (64, 1), (50, 1), (32, 1), (1, 1)]

    for case, expected in test_cases:
        assert get_num_bytes(case) == expected


def test_get_curr_byte_val():
    test_cases_args = [(150, 1, 2), (150, 0, 2)]
    test_cases_expected = [150, 1]

    for i in range(len(test_cases_args)):
        num, byte_pos, num_bytes = test_cases_args[i]
        assert get_curr_byte_val(num, byte_pos, num_bytes) == test_cases_expected[i]

def test_encode():
    test_cases = [(150, b'\x96\x01')]

    for case, expected in test_cases:
        assert encode(case) == expected
