number = int(input("enter the number : "))
multiple = int(input("enter the limit of multiples : "))
print(f"the multiplication table of {number} is :\n")

for i in range(1, multiple +1):
    result = number * i 
    print(f"{number} x {i} = {result}")