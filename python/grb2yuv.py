#(c) 2022 David Shadoff
import sys

# Notes:
#
# This program converts a PC Engine GRB palette entry into a PC-FX palette number
#
#   Usage: grb2yuv <PCE Palette val>
#   OR:    grb2yuv grb2yuv <green> <red> <blue>
#   where G,R,B values are 0-7 (and PCE palette val is maximum 9 bits)
#
#   Example:
#     python grb2yuv.py 7 0 0
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

#
## Main Program:
#

if ((len(sys.argv) != 2) and (len(sys.argv) != 4)):
    print("Usage: grb2yuv <PCE Palette val>")
    print("OR     grb2yuv <green> <red> <blue>")
    print("where G,R,B values are 0-7 (and PCE palette val is maximum 9 bits)")
    exit()

if (len(sys.argv) == 2):
    pal = hexdecode(sys.argv[1])
    blue = pal & 7
    red = (pal >> 3) & 7
    green = (pal >> 6) & 7
else:
    green = hexdecode(sys.argv[1])
    red = hexdecode(sys.argv[2])
    blue = hexdecode(sys.argv[3])

print("green = ", green)
print("red   = ", red)
print("blue  = ", blue)

g = green * 36
r = red * 36
b = blue * 36

yfloat = (0.299 * r) + (0.587 * g) + (0.114 * b)
y = int(yfloat)
ufloat = (-0.169 * r) + (-0.331 * g) + (0.499 * b) + 128
u = int(ufloat+0.5)>>4
vfloat = (0.499 * r) + (-0.418 * g) + (-0.0813 * b) + 128
v = int(vfloat+0.5)>>4 

print("Y = ", yfloat)
print("U   = ", ufloat)
print("V  = ", vfloat)
print()
print('YUV',end='=')
yuv = (y*256) + (u*16) + (v)
print('{0:0{1}X}'.format(yuv,2)) 
