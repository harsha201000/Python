# fibonaaci series using simple iteration
# 0 and 1 are the starting numbers

num = 10
term1, term2 = 0, 1

for i in range(2, num):
    term3 = term1 + term2
    term1 = term2
    term2 = term3
    print(term3, end=" ")
    
print()