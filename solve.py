def gen_seed(s):
    i, j, k = 0, len(s), 0
    while i < j:
        k = k + ord(s[i])
        i += 1
    i = 0
    while i < j:
        if (i % 2) != 0:
            k = k - (ord(s[i]) * (j - i + 1))            
        else:
            k = k + (ord(s[i]) * (j - i + 1))
        k = k % 2147483647
        i += 1
    k = (k * j) % 2147483647
    return k

def reseed(s):
    return s * 214013 + 2531011
    
def encrypt(s, msg):
    assert s <= 2**32
    c, d = 0, s
    enc, l = b'', len(msg)
    while c < l:
        d = reseed(d)
        enc += (msg[c] ^ ((d >> 16) & 0xff)).to_bytes(1, 'big')
        c += 1
    return enc

def decrypt(s, enc):
    assert s <= 2**32
    c, d = 0, s
    msg, l = b'', len(enc)
    while c < l:
        d = reseed(d)
        msg += (enc[c] ^ ((d >> 16) & 0xff)).to_bytes(1, 'big')
        c += 1
    return msg

enc = b'T\xf0\xa9\x15I\x99\xbb\x02\xda\x88\x8a\xfe9\xc0z\x9f\xcc\xa0\xa4\xa1\x02\x05\xe3\xa6/\x063\x9e\x13W\xe5\xf1\xf6\xfd3\x8c\x07b-\xa8\xf7\\0\x9c|\xf6fF\xe2c@\xe2\xbf\xadV$>\xf8d\x9e\x87Y\xdb\x9d]\x01\xa4\xeb\x94P\xddXT6\x8aF\xd7\xf7>\xed\x1d\xe4a\xe3!g\t\xdfFEhu\xba\x83q\x84\xfd\xf0\xdc\xe8\x89l\x15|\x1bc\xbe/\x81[\xa6b^\xbb'
flag_is = binascii.hexlify(enc)[:28]
#7135fe1db74974f3fc5b20447443 - 'flag is'
    
for seeds in range(1, 2**32 + 1):
    enc2 = encrypt(seeds, binascii.hexlify(bytes(("flag is").encode('utf-8'))))
    if binascii.hexlify(enc2) == flag_is: 
        seed = seeds
        break
for char in range(256):
    dec = decrypt(seed, enc)
    if all(32 <= byte <= 126 or byte == 10 or byte == 13 for byte in dec):
        print(seed)
        print(f"Decrypted message: {binascii.unhexlify(dec.decode('utf-8'))}")
    seed += 1