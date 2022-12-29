from itertools import cycle, islice # introducing functional programming

def bytes_xor(a: bytes, b: bytes) -> bytes:
    return bytes(byte1 ^ byte2 for byte1, byte2 in zip(a, b))

def bytes_multy_xoring(*args: bytes) -> bytes:
    result = args[0]
    for arg in args[1:]:
        result = bytes_xor(result, arg)
    return (result)

def repeating_key_xoring(key: bytes, plaintext: bytes) -> bytes:
    full_key = bytes(islice(cycle(key), len(plaintext)))
    print(f"The full key is : {full_key}")
    return bytes_multy_xoring(full_key, plaintext)

if __name__ == '__main__':
    result = repeating_key_xoring(b"ICE", b"Burning 'em, if you ai n't quick and nimble\n")
    # expected = bytes.fromhex("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272")
    print(f"The result of the key xoring is : {result.hex()}")
