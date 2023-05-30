# Header to display to User
print('CALCULATOR' "\n")

# Establishing User Interface, taking input
firstnum = float(input('First number: '))
secondnum = float(input('Second number: '))

add = firstnum + secondnum
sub = firstnum - secondnum
mult = firstnum * secondnum
div = firstnum / secondnum
mod = firstnum % secondnum

# Result
print(f"\n" "Add: ", add)
print(f"Subtract: ", sub)
print(f"Multiply: ", mult)
print(f"Divide: ", div)
print(f"Modulus: ", mod)
