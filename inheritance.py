class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display_emp(self):
        print("name:",self.name)
        print("salary:",self.salary)

      

class Devloper(Employee):
    def __init__(self,name,salary,language):
        Employee.__init__(self,name,salary)
        self.language=language

    def display_devloper(self):
        super().display_emp()
        print("programing language:",self.language)
        
    

class Tester(Employee):
    def __init__(self,name,salary,testing_tool):
        Employee.__init__(self,name,salary)
        self.testing_tool=testing_tool

    def display_tester(self):
        super().display_emp()
        print("Testing tool:",self.testing_tool)

d=Devloper('Rahul',30000,'Python')
t=Tester('Priya',5000,'selenium')
