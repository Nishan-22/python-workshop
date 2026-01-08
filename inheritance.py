class shape:
    def infa():
        print("It is a shape")
class Rectangle(shape):
    def info():
        print("this is rectangle")
obj1 = shape
obj1 = Rectangle
obj1.infa()
obj1.info()

# multiple inheritance

class Area:
    def calculate_area(self):
        a = self.length * self.width
        print("Calculating area:", a)

class Perimeter:
    def calculate_perimeter(self):
        b = 2 * (self.length + self.width)
        print("Calculating perimeter:", b)

class Rectangle(Area, Perimeter):
    def __init__(self, length, width):
        self.length = length
        self.width = width

obj2 = Rectangle(5, 4)
obj2.calculate_area()
obj2.calculate_perimeter()


    
#     Create Employee base class with:
# - Attributes: name, base_salary
# - Method: calculate_salary() returns base_salary
# Create these child classes:
# 1. Developer: salary = base_salary + (overtime_hours × 500)
# 2. Manager: salary = base_salary + bonus + (team_size × 1000)
# 3. SalesPerson: salary = base_salary + (commission_rate × sales_amount)
# Create a function total_payroll(*employees) that returns sum of all salaries.



class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary
    
class Developer(Employee):
    def __init__(self, name, base_salary, overtime_hours):
        super().__init__(name, base_salary)
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        total = self.base_salary + (self.overtime_hours*500)
        return total

class Manager(Employee):
    def __init__(self, name, base_salary, bonus, team_size):
        super().__init__(name, base_salary)
        self.bonus = bonus
        self.team_size = team_size
    
    def calculate_salary(self):
        total2 = self.base_salary + self.bonus + (self.team_size * 1000)
        return total2

class SalesPerson(Employee):
    def __init__(self, name, base_salary, commission_rate, sales_amount):
        super().__init__(name, base_salary)
        self.commission_rate = commission_rate
        self.sales_amount = sales_amount
    def calculate_salary(self):
        total = self.base_salary + (self.commission_rate * self.sales_amount)
        return total

def total_payroll(*employees):
    total = 0
    for i in employees:
        total += i.calculate_salary()
    return total
    
dev = Developer("Alice", 60000, overtime_hours=10) 
manager = Manager("Bob", 80000, bonus=10000, team_size=5) 
sales = SalesPerson("Charlie", 40000, commission_rate=0.1, sales_amount=200000) #
salary = 60000
total = total_payroll(dev, manager, sales)

print("Total Payroll:", total)  





def twoSum(nums, target):
    seen = {}  # stores number : index

    for i in range(len(nums)):
        needed = target - nums[i]

        if needed in seen:
            return [seen[needed], i]

        seen[nums[i]] = i


# alternative approach
def twoSum(nums, target):
    for i, x in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if x + nums[j] == target:
                return [i, j]
