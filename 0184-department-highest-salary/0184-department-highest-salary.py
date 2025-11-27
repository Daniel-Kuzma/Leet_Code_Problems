import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department = department.rename(columns = {"id" : "departmentId"})
    employee = employee.merge(department, on = 'departmentId', how = 'right').rename(columns = {"name_y" : "Department", "name_x" : "Employee", "salary" : "Salary" })

    max = employee.groupby('Department')['Salary'].transform('max')
    employee = employee[employee["Salary"] == max]
    return employee[["Department","Employee","Salary"]]
    