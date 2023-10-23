x = "1011"
y = 0
for i in range(4):
    bit = int(x[i])
    y += bit * (2 ** (3 - i))
    
print(y)