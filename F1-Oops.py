# Step1: To initiate a class
class employee:
    # There are some special methods/ magic methods or dunder methods, AKA Constructors.
    def __init__(self):
        # print("Self executed data or attributes- Start")
        self.id = 10001
        self.age = 32
        self.salary = 200000
        self.designation = "Data Scientist"
        # print("Self executed data or attributes- Done")
    
    def travel(self, destination):
        print("Manually executed functions or methods")
        print(f"Employee is now eligible to travel to {destination}")
        
        
        
# Step2: Create an object or instance of the class
John = employee()

## Calling Default features i.e., Attributes
# print("Age:",John.age)
# print("ID:",John.id)

## Calling functionalty based features i.e., Methods
# John.travel("Frankfurt")

# print(type(John))

### Step to define attribute outside the class 'Employee' in this code
# John.name = "John Doe"
# print(John.name)