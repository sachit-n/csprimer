import math

def read_binary(filename):
    """
    read a binary file
    """
    with open(filename, mode='rb') as file: # b is important -> binary
        file_content = file.read()
    return file_content


def binary_to_int(binary):
    """
    convert sequence of bits representing unsigned int to python int
    """
    return int.from_bytes(binary, 'big')


def get_num_of_bits(num):
    """
    returns the minimum number of bits required to represent num
    """
    return math.floor(math.log2(num))+1


def get_num_bytes(num):
    """
    returns number of bytes required in the varint
    """
    min_num_of_bits = get_num_of_bits(num) 
    return math.ceil(min_num_of_bits/7) # each byte uses 7 bites for the number


def get_curr_byte_val(num, byte_order):
    """
    returns the value represented in the 7 bits of the current byte
    """
    val = num // (2**(7*(byte_order)))
    return val

def encode(num: int) -> bytes:
    """
    encode the integer as a base 128 varint
    """
    num_bytes = get_num_bytes(num)
    
    curr_byte_order = num_bytes-1
    num_now = num
    out = []
    while curr_byte_order>=0:
        val_now = get_curr_byte_val(num_now, curr_byte_order)
        num_now -= val_now*(2**(7*(curr_byte_order)))
        
        if curr_byte_order<(num_bytes-1):
            val_now += 2**7 # msb represents whether more bytes follow
        out.append(val_now)

        curr_byte_order -= 1
    
    out_le = out[::-1]  # convert to little endian
        
    return bytes(out_le)

if __name__=='__main__':
    filename = "150.uint64"
    unsigned_int = read_binary(filename)
    val = binary_to_int(unsigned_int)
    print(encode(val))
    assert encode(val) == b'\x96\x01'
    
