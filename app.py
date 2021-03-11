
class Employee:

    emp_amt = 0
    total_pay = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        Employee.emp_amt += 1
        Employee.total_pay += pay

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.fist = first
        self.last = last

    def apply_raise(self, raise_amt):
        self.pay = int(self.pay * raise_amt)

    def set_pay(self, amount):
        self.pay = amount

    def get_pay(self):
        return self.pay
    
    def get_emp_amount():
        return Employee.emp_amt
    
    def get_total_pay():
        return Employee.total_pay

class Developer(Employee):
    def __init__(self, first, last, pay, lang): 
        super().__init__(first, last, pay)
        self.lang = lang 

class Manager(Employee):
    def __init__(self, first, last, pay, emps = None):
        super().__init__(first, last, pay)
        if emps is None:
            self.emps = []
        else:
            self.emps = emps
    
    def add_emp(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)

    def remove_emp(self, emp):
        if emp in self.emps:
            self.emps.remove(emp)
       
emp_1 = Employee('Arttu', 'Mäkelä', 60000)

emp_2 = Employee('Janne', 'Java', 90000) 

manager_1 = Manager('Petri', 'Pomo', 180000, [emp_1, emp_2]) 

print(Employee.get_emp_amount())
    