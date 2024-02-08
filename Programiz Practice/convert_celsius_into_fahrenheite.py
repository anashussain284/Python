"""
fahrenheit = celsius * 1.8 + 32
celsius = (fahrenheit - 32) / 1.8
"""

fh = 990
cs = (fh - 32) / 1.8

print("%0.2f fahrenheit = %0.2f celsius" %(fh, cs))

fh = cs * 1.8 + 32
print("%0.2f celsius = %0.2f fahrenheit" %(cs, fh))