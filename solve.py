from z3 import *
import string

def to_words(chars):
    return [Concat(chars[i+1], chars[i]) for i in range(0, 32, 2)]
    
def to_dwords(chars):
    return [Concat(chars[i+3], chars[i+2], chars[i+1], chars[i]) for i in range(0, 32, 4)]

def to_qwords(chars):
    return [Concat(chars[i+7], chars[i+6], chars[i+5], chars[i+4], chars[i+3], chars[i+2], chars[i+1], chars[i]) for i in range(0, 32, 8)]


s = Solver()

allowed_chars = list(string.ascii_letters+string.punctuation+string.digits)

chars = [BitVec(f"char[{i}]", 8) for i in range(32)]

words = to_words(chars)
dwords = to_dwords(chars)
qwords = to_qwords(chars)


for byte in chars:
    s.add(Or([byte == ord(ch) for ch in allowed_chars]))
    
s.add(words[0]+words[2]-words[5]+words[7]+words[10] == BitVecVal(60760, 16))
s.add(qwords[0]^qwords[3] == BitVecVal(2965938363618105624, 64))
s.add(words[11]-words[3]+words[0]+words[13]-words[15] == BitVecVal(19597, 16))
s.add(dwords[1]-2*dwords[4]+dwords[3]+dwords[0] == BitVecVal(1282873082, 32))
s.add(qwords[1]^qwords[2] == BitVecVal(1692449083687022, 64))
s.add(words[1]+words[4]-words[6]+words[8]+words[9]-3*words[12] == BitVecVal(18582,16))
s.add(4*dwords[2]-2*dwords[6]-dwords[7]-dwords[5] == BitVecVal(1126845477,32))


print(s.check())
m = s.model()

res = ''.join([chr(m.evaluate(chars[i]).as_long()) for i in range(32)])
print(res)
