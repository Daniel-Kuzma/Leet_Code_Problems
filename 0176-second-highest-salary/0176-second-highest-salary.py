import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
        name = f"SecondHighestSalary"
        employee = employee.drop_duplicates(subset=['salary'])
        employee = employee.sort_values("salary", ascending = False).reset_index()
        if employee["salary"].count() > 1:
            return pd.DataFrame({name : [employee.loc[1,"salary"]]})
        return pd.DataFrame({name : [None]})