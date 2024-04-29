#(c) 2024 David Shadoff
import sys

# Notes:
#
# This program converts a PC Engine PCEAS "defpal" RGB palette entries
# into PC-FX palette values
#
#   Usage: cvtdefpal <RGB>[,<RGB>]...
#   where R,G,B values are 0-7 (and PCE palette val is maximum 9 bits)
#
#   Example:
#     python cvtdefpal.py 000,222,175,777
#

#
# hexdecode: Get a value and convert it if it has a hexadecimal prefix
#
def hexdecode(input):
    hexadecimal = 0
    num = 0
    if input[0] == "$":
        hexadecimal = 1
        hexnum = input[1:]
    elif input[0:2] == "0x" or input[0:2] == "0X":
        hexadecimal = 1
        hexnum = input[2:]

    if hexadecimal == 1:
        num = int(hexnum, 16)
    else:
        num = int(input)
    return num

def calculate(red, green, blue):

    r = red * 36
    g = green * 36
    b = blue * 36

    yfloat = (0.299 * r) + (0.587 * g) + (0.114 * b)
    y = int(yfloat)
    ufloat = (-0.169 * r) + (-0.331 * g) + (0.499 * b) + 128
    u = int(ufloat+0.5)>>4
    vfloat = (0.499 * r) + (-0.418 * g) + (-0.0813 * b) + 128
    v = int(vfloat+0.5)>>4 

#    print("Y = ", yfloat)
#    print("U   = ", ufloat)
#    print("V  = ", vfloat)
#    print()
#    print('YUV',end='=')
    yuv = (y*256) + (u*16) + (v)
    print('0x{0:0{1}X}'.format(yuv,4), end='') 

#
## Main Program:
#

index = 0
colorset = 0
first = 0
while(1):
    if (index >= len(sys.argv[1])):
        if (colorset != 0):
            calculate(green, red, blue)
        break

    if (sys.argv[1][index] == ','):
        calculate(red, green, blue)
        colorset = 0
        red = 0
        green = 0
        blue = 0
        index = index + 1
        continue

    if ((sys.argv[1][index] < "0") or (sys.argv[1][index] > "7")):
        index = index + 1
        continue

    if (colorset == 0):           # Note that defpal sequence is RGB, not GRB
        red = int(sys.argv[1][index])
        colorset = colorset + 1
        if (first != 0):
            print(', ', end='') 
        first = 1

    elif (colorset == 1):
        green = int(sys.argv[1][index])
        colorset = colorset + 1

    elif (colorset == 2):
        blue = int(sys.argv[1][index])
        colorset = colorset + 1

    index = index + 1

print()

