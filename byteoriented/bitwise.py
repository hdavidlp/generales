from lib2to3.pgen2.token import LESS


#More                Less 
# X  X  X  X  X  X  X  X

#   & = and
# Usually to mask
a = 0b1100
b = 0b1010
c = a & b
d = bin(a & b)

print (c)
print (d)

def byte_at(v, n):
    s = n * 8
    return (v & (0xff << s)) >> s

print(hex(byte_at(0xdc143c,0)))
print(hex(byte_at(0xdc143c,1)))
print(hex(byte_at(0xdc143c,2)))


def rgb (color):
    return (
        byte_at(color,2),
        byte_at(color,1),
        byte_at(color,0)
    )


crimson = 0xdc143c
print(rgb(crimson))


# Bitwise Or
# │

aa = 0b1100
bb = 0b1010
cc = aa | bb
print (bin(cc))








