num=int(input("Please enter a numerator:"))
den=int(input("Please enter a denominator:"))
if num%den==0:
    print(num,"can be divided by",den)
else:
    print(num,"cannot be divided by",den)