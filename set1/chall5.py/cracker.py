import binascii

def xoring(text, key) :
    return ([a ^ key for a in text])

def Encrypter(plain_text, key):
    array_pt = [ord(a) for a in plain_text] 
    array_key = [ord(a) for a in key]

    for kb in array_key:
        print('Before :', array_pt)
        array_pt = xoring(array_pt, kb)

    array_pt = [hex(a) for a in array_pt]
    return (''.join(array_pt))

if __name__ == '__main__':
    encrypted_str = Encrypter("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal", "ICE")
    print(encrypted_str.replace("0x", ""))
