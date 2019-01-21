value1 = 0
value2 = 0 
for i in range(1000):
    if i % 3 == 0:
        value1 += i
    if i % 5 == 0:
        value2 += i
print(value1+value2)            