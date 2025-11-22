import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees[(employees["name"].str.slice(start = 0, stop = 1) != "M") & (employees["employee_id"] % 2 == 1)]["salary"]
    return employees.loc[:,["employee_id", "bonus"]].fillna(value = 0).sort_values("employee_id")
