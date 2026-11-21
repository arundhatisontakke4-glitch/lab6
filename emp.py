import sys
def emp(name, employee_id, department, salary):
    return f"Name: {name}\nEmployee ID: {employee_id}\nDepartment: {department}\nSalary: {salary}"
if __name__ == "__main__":
    name = sys.argv[1]
    employee_id = sys.argv[2]
    department = sys.argv[3]
    salary = sys.argv[4]
    print("\nEmployee Details")
    print("------------------")
    print(emp(name, employee_id, department, salary))
