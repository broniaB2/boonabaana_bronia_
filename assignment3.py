# a real world example assignment demonstrating method overriding, method overloading and MRO
# an employee payment and management system
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def compute_salary(self):
        return 0

    def display_info(self):
        print(f"Employee: {self.name} (ID: {self.employee_id})")


class MonthlypaidEmployee(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.salary = salary

    # Method overriding on the compute salary method that is calculating the monthly payment
    def compute_salary(self):
        return self.salary / 12

    def display_info(self):
        super().display_info()
        print(f"Type: paid, Annual Salary is: ugx{self.salary:,}")


class Per_daypaidEmployee(Employee):
    def __init__(self, name, employee_id, days_worked, daily_rate):
        super().__init__(name, employee_id)
        self.days_worked = days_worked
        self.daily_rate = daily_rate

    # method overriden again in this class
    def compute_salary(self):
        return self.daily_rate * self.days_worked

    def display_info(self):
        super().display_info()
        print(
            f"Type: per_day, Rate: ugx{self.daily_rate}*days, Days: {self.days_worked}"
        )


class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def compute_salary(self):
        return self.hourly_rate * self.hours_worked

    def display_info(self):
        super().display_info()
        print(
            f"Type: Hourly, Rate: ugx{self.hourly_rate}/hr, Hours: {self.hours_worked}"
        )


# this shows MRO
print("HourlyEmployee MRO:", HourlyEmployee.__mro__)

emp1 = MonthlypaidEmployee("Bronia B", "E01", 2000000)
emp2 = Per_daypaidEmployee("Bridget", "E02", 20, 90000)
emp3 = HourlyEmployee("Bruno T", "E03", 5000, 100)

for emp in [emp1, emp2, emp3]:
    emp.display_info()
    print(f"Monthly Pay: ugx{emp.compute_salary():,}\n")
