from z3 import *
import string

allowed_chars = list(string.ascii_letters+string.punctuation+string.digits)
chars = [BitVec(f"char[{i}]", 8) for i in range(16)]
s = Solver()

for byte in chars:
    s.add(Or([byte == ord(ch) for ch in allowed_chars]))
    
summs = [133,90,93,83,127,103,94,98,94,108,149,200,195,196,185]
chars1 = []

for i in chars[::-1]:
    chars1.append(i - 20)

for i in range(len(summs)):
    s.add(chars1[i]+chars1[i+1] == summs[i])
    
s.add(chars1[15]*2 == 174)    

print(s.check())
if s.check() == unsat:
    exit()
    
m = s.model()
res = ''.join([chr(m.evaluate(chars[i]).as_long()) for i in range(16)])
print(res)
