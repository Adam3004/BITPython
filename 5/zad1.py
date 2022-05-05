from datetime import *


class Employee:
    def __init__(self, first_name: str, last_name: str, date_of_birth: str, join_date: str, salary: int):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.join_date = join_date
        self.salary = salary

    def get_full_name(self):
        return (f'{self.first_name} {self.last_name}')

    def get_net_pay(self):
        return round(self.salary * 0.82, 2)

    @property
    def work_years(self):
        now = datetime.now().year
        then = datetime.strptime(self.join_date, '%Y-%m-%d').year
        return now - then


if __name__ == '__main__':
    employee = Employee('Jan', 'Kowalski', '1978-04-25', '2005-07-28', 8000)
    print(employee.get_full_name())
    print(employee.get_net_pay())
    print(employee.work_years)
