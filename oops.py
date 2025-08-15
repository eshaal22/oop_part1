'''
# ======================================================
#       PYTHON OOP (Object-Oriented Programming) PRACTICE
# ======================================================

# ----------------------------------------
# 1. CLASS & OBJECT BASICS
# ----------------------------------------

class Student:
    # Class attributes (shared by all objects)
    college_name = "ABC COLLEGE"  
    name = "Anonymous"            # Default name if not provided

    # Constructor method (runs when a new object is created)
    def __init__(self, name, marks):
        # Instance attributes (unique to each object)
        self.name = name
        self.marks = marks
        print("Adding new student to database...")

    # Instance method - uses object's own data
    def welcome(self):
        print("Welcome student", self.name)

    # Instance method - returns marks
    def get_marks(self):
        return self.marks


# --- Create a Student object ---
s1 = Student("Karan", 97)   # Creates object and runs __init__
s1.welcome()                # Calls welcome method
print(s1.get_marks())       # Prints marks


# ----------------------------------------
# 2. PRACTICE QUESTION: AVERAGE MARKS
# ----------------------------------------

class StudentAverage:
    def __init__(self, name, marks_list):
        self.name = name
        self.marks = marks_list  # List of marks for the student

    def get_average(self):
        # Calculate average marks
        total = 0
        for value in self.marks:
            total += value
        avg = total / len(self.marks)
        print(f"Hi {self.name}, your average score is {avg}")


# --- Create StudentAverage object and find average ---
s2 = StudentAverage("Eshaal", [89, 98, 70])
s2.get_average()


# ----------------------------------------
# 3. STATIC METHOD EXAMPLE
# ----------------------------------------
class StudentStatic:
    @staticmethod  # Does not need 'self' or 'cls'
    def hello():
        print("Hello from StudentStatic class!")


# --- Call static method ---
s3 = StudentStatic()
s3.hello()


# ----------------------------------------
# 4. ABSTRACTION EXAMPLE
# ----------------------------------------
# Abstraction = hiding internal working details and showing only necessary parts

class Car:
    def __init__(self):
        # Internal states (hidden from the user)
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        # Internally sets required conditions for starting the car
        self.clutch = True
        self.acc = True
        print("Car started...")


# --- Create Car object and start ---
car1 = Car()
car1.start()


# ----------------------------------------
# 5. ENCAPSULATION EXAMPLE
# ----------------------------------------
# Encapsulation = wrapping data (variables) + methods (functions) inside one unit (class)

class Account:
    def __init__(self, bal, acc_no):
        # Instance attributes
        self.balance = bal
        self.account_no = acc_no

    # Method to withdraw money
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("Total balance =", self.get_balance())

    # Method to deposit money
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("Total balance =", self.get_balance())

    # Getter method to check balance
    def get_balance(self):
        return self.balance


# --- Create Account object and perform transactions ---
acc1 = Account(10000, 12345)
acc1.debit(1000)     # Withdraw 1000
acc1.credit(90)      # Deposit 90
acc1.credit(9000)    # Deposit 9000
'''
