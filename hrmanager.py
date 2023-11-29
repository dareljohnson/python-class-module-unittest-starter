# file name: hrmanager.py
from mymodule import MyModule


class HRManager:
    @staticmethod
    def greet_employees(employee_list) -> int:
        count = 0
        if len(employee_list) == 0:
            return 0

        for employee in employee_list:
            if 'name' in employee:
                MyModule.greeting(employee['name'])
                count += 1
            else:
                pass

        return count


if __name__ == "__main__":
    employees = [
        {"name": "John", "age": 36, "country": "Norway"},
        {"name": "Alice", "age": 30, "country": "USA"}
    ]

    # hr_manager = HRManager(employees)
    result = HRManager.greet_employees(employees)
    print("count: ", result)
