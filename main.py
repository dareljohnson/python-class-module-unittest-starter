from hrmanager import HRManager as hr

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    employees = [
        {"name": "John", "age": 36, "country": "Norway"},
        {"name": "Alice", "age": 30, "country": "USA"},
        {"name": "Darel", "age": 62, "country": "USA"}
    ]

    # hr_manager = HRManager(employees)
    hr.greet_employees(employees)
