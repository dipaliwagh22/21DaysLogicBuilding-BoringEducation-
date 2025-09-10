#  program to print the input number is armstrong or not.
input_number = int(input("Enter a number: "))
sum_of_cubes = sum(int(digit) ** 3 for digit in str(input_number))
if sum_of_cubes == input_number:
    print(f"{input_number} is an Armstrong number.")
else:
    print(f"{input_number} is not an Armstrong number.")