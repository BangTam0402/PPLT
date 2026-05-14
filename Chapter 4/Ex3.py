class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        return "Chưa xác định"


class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, base_salary):
        super().__init__(emp_id, name)
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, work_hours, hourly_rate):
        super().__init__(emp_id, name)
        self.work_hours = work_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.work_hours * self.hourly_rate


employees = [
    FullTimeEmployee("NV01", "Tâm", 10000000),
    PartTimeEmployee("NV02", "Trường", 40, 50000),
    FullTimeEmployee("NV03", "Chi", 12000000),
    PartTimeEmployee("NV04", "Dung", 30, 60000)
]

for employee in employees:
    print("Tên nhân viên:", employee.name)
    print("Lương:", employee.calculate_salary())
    print()