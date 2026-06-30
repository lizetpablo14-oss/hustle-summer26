#Jessica Pablo | Lab 4 | Red
#Ticket 1 for Loop
age = [17, 11, 25, 13, 9]
for age in age:
    if age >= 13:
        print("Access Granted.")
    else:
        print("Too Young.")
# PREDICT: Access Granted. Too Young. Access Granted. Access Granted. Too Young.
# The loop will go through each number in the list and check if it is greater than or equal to 13. If it is, it will print "Access Granted." If it is not, it will print "Too Young."

# Ticket 2 while loop
keep_checking = "yes"
while keep_checking == "yes":
    age = int(input("Enter your age: "))
    if age >= 13:
        print("Access Granted.")
    else:
        print("Too Young.")
    keep_checking = input("Do you want to check another age? (yes/no): ")
# PREDICT: The loop will stop if the user inputs "no" when asked.
# A while loop is better because we want to keep checking the user's age until they decide to stop. A for loop would not be the best because we do not know how many times the user will want to check their age.

# Ticket 3 for loop
while True:
    age = input("Enter your age or stop to exit: ")
    if age == "stop":
        break
    age = int(age)
    if age >= 13:
        print("Access Granted.")
    else:
        print("Too Young.")
# PREDICT: If break is forgotten, the loop will continue indefinitely and the user will not be able to exit the loop. The program will keep asking for the user's age and checking if they are old enough to access the content.
# The difference between a for loop and a while loop is that a for loop is used when you know how many times you want to loop, while a while loop is used when you do not know how many times you want to loop.

# Ticket 4 functions
def can_access(age):
    if can_access(age) >= 13:
        return True
    else:
        return False
# PREDICT: Its different because the function is checking if the age is greater than or equal to 13 and returning True or False. The loop is checking if the age is greater than or equal to 13 and printing "Access Granted." or "Too Young."
# Putting check in a function is better than if/else statements because it iseasier to read.

# Ticket 5 Capstone
print("--- Streampass Signup Report ---")
signup_report = [22, 10, 15, 8, 19, 13]
approved = 0
for age, item in enumerate(signup_report, start=1):
    if item >= 13:
        approved += 1
        print(f"Signup #{age}: | Age {item} is approved.")
    else:
        print(f"Signup #{age}: | Age {item} is not approved.")
print(f"Approved: {approved} out of {len(signup_report)}")
# PREDICT: The loop will go through each number in the list and check if it is greater than or equal to 13. If it is, it will print "Signup #X: | Age Y is approved." If it is not, it will print "Signup #X: | Age Y is not approved." The final print statement will show how many signups were approved which for me will be 4 out of 6.
# Every concept I used to build this function was a for loop, if/else statements, and the enumerate function. I used a for loop to go through each number in the list, if/else statements to check if the age is greater than or equal to 13, and the enumerate function to keep track of the signup number.