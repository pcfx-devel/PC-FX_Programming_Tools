# Usage example for cvtgfx

## EXAMPLE 1 - Character data

### Inputs

File bgchr0.txt is used as the ASCII art template in this example

File bgchar0.xlate is used as the 'translation' file (i.e. character position 0 = '0',
so the value of '0' in the ASCII art file is interpreted as colour 0).

### Command-line

```
python cvtgfx.py tile bgchr0 bgdata.txt 48 0 1 1 1 bgdata.xlate
```

This converts an 8x8 single tile at coordinates (48,0) through (55,7) in the
ASCII art file into a CHARACTER TILE data definition, in the output file "bgchr0.gen_data"
which can then be used in a host C program as a #include

### Outputs

See file bgchr0.gen_data for the example output, which consists of a definition of a
uint16_t array of data, to be loaded directly into video memory for the HuC6270 processor.



## EXAMPLE 2 - Sprite data

### Inputs

File spr0data.txt is used as the ASCII art template in this example

Again, file bgchar0.xlate is used as the 'translation' file (i.e. character position 0 = '0',
so the value of '0' in the ASCII art file is interpreted as colour 0).

### Command-line

```
python cvtgfx.py sprite spr0 spr0data.txt 0 0 2 2 2 bgdata.xlate
```

This converts a series of sprite cells - 2 wide by 2 high - which are each 16x16 pixels,
at coordinates (0,0) through (31,31) in the ASCII art file into a SPRITE data definition,
in the output file "spr0.gen_data" which can then be used in a host C program as a #include

### Outputs

See file spr0.gen_data for the example output, which consists of a definition of a
uint16_t array of data, to be loaded directly into video memory for the HuC6270 processor.

