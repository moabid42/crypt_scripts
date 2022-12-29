

def bytes_xor(a: bytes, b: bytes) -> bytes:
    return bytes(byte1 ^ byte2 for byte1, byte2 in zip(a, b))


def bytes_multy_xoring(*args: bytes) -> bytes:
    result = args[0]
    for arg in args[1:]:
        result = bytes_xor(result, arg)
    return (result)


if __name__ == '__main__':
    a = bytes.fromhex('1c0111001f010100061a024b53535009181c')
    b = bytes.fromhex('686974207468652062756c6c277320657965')

    result = bytes_multy_xoring(a, b)
    print(f"The result is :{result}")
    print(f"The result in Hex is : {result.hex()}")
     