# Corrected version of smgamount formatting
amount_smg = "%1000s" % "four"  # Using string formatting to allocate 1000 spaces
print(f"{amount_smg}")  # Prints 'four' aligned to the right with 1000 characters wide

smgamount = "%1000s" % "four"  # Again, using the same formatting
print(f"{amount_smg}")  # Same output as above

# Printing salary with two approaches
salary = 100.00

# Approach 1: Using string concatenation with `str`
print("Your salary is $" + str(salary))

# Approach 2: Using formatted string for two decimal places
print(f"Your salary is ${salary:.2f}")  # This ensures 2 decimal precision
