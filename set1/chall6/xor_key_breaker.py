import base64
from itertools import combinations

# def hamming_distance(string1: bytes, string2: bytes) -> int:
#     distance = 0;
#     for c1, c2 in zip(string1, string2):
#         b1 = bin(ord(c1))[2:]
#         b2 = bin(ord(c2))[2:]

#         b1 = b1.zfill(8)
#         b2 = b2.zfill(8)

#         for bit1, bit2 in zip(b1, b2):
#             if bit1 != bit2:
#                 distance += 1
#     return (distance)

def _get_hamming_weights() -> dict[int, int]:
    weights = {0: 0}
    pw_2 = 1
    for _ in range(8):
        for k, v in weights.copy().items():
            weights[k+pw_2] = v+1
        pw_2 <<= 1
    return weights

weights = _get_hamming_weights()

def bytes_xor(a: bytes, b: bytes) -> bytes:
    return bytes(byte1 ^ byte2 for byte1, byte2 in zip(a, b))

def hamming_distance(a: bytes, b: bytes) -> int:
    return sum(weights[byte] for byte in bytes_xor(a, b))

def guess_keysize(ct: bytes, num_guesses: int = 1) -> list[tuple[float, int]] :
    def get_score(size: int) -> float :
        chunks = (ct[:size],
                  ct[size:2*size],
                  ct[2*size:3*size],
                  ct[3*size:4*size])
        avg = sum(hamming_distance(a, b) for a, b in combinations(chunks, 2)) / 6
        return (avg / size)
    
    scores = [(get_score(size), size) for size in range(2, 41)]
    scores.sort()
    return scores[:num_guesses]

if __name__ == '__main__' :
    
    # 1
    with open('data.txt', 'rb') as f:
        file_bytes = f.read()
    decoded_bytes = base64.b64decode(file_bytes)
    # 2
    # KEYSIZE = keysize_finder() # while KEYSIZE is between 2 and 40
    # 3
    # string1 = "this is a test"
    # string2 = "wokka wokka!!!"

    # hamming_distance = hamming_distance(b"string1", b"string2")
    # print(f"The hamming distance is : {hamming_distance}")

    # 4
    keysize = guess_keysize(decoded_bytes, 5)
    print(f"Best key size guesses {keysize}")

