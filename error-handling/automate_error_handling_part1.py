try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("The result is:",result)
except ValueError:
    print("You must enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")

"""output:
$python automate_error_handling_part1.py
Enter a number: 4
The result is: 2.5

$python automate_error_handling_part1.py
Enter a number: 0
You cannot divide by zero.

$python automate_error_handling_part1.py
Enter a number: hel 
You must enter a valid integer."""