number=str(input())
even_sum = 0
odd_sum = 0
for digit in number:
    digit = int(digit)
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
if (even_sum==odd_sum):
    print("True")
else:
    print("False")
