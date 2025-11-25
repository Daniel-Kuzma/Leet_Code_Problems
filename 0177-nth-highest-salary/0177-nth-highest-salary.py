import pandas as pd


"""def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    name = f"getNthHighestSalary({N})"
    if employee["salary"].count() >= N:

        copy = employee.drop_duplicates(subset=['salary'])

        max = employee['salary'].drop_duplicates().nlargest(N).iloc[-1]

        pom = employee[employee["salary"] == max]

        if (pom["salary"].count() == 1) and (employee["salary"].count() == 1):
            return pd.DataFrame({name : [max]})

        if (pom["salary"].count() >= 2) and (employee["salary"].count() == N):
            return pd.DataFrame({name : [None]})

        return pd.DataFrame({name : [max]})
    return pd.DataFrame({name : [None]})"""

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Nazwa kolumny wynikowej
    name = f"getNthHighestSalary({N})"
    
    # KROK 1: Najpierw pobierz same unikalne zarobki (bez duplikatów)
    unique_salaries = employee["salary"].drop_duplicates()

    # KROK 2: Sprawdź, czy liczba unikalnych zarobków jest wystarczająca
    # (np. jeśli szukasz 3. zarobku, musisz mieć przynajmniej 3 różne pensje)
    if N > 0 and len(unique_salaries) >= N:
        
        # KROK 3: Weź N najwyższych unikalnych i wybierz ostatnią z nich (czyli N-tą)
        # .nlargest(N) zwraca listę [1. najwyższa, 2. najwyższa, ..., N-ta najwyższa]
        # .iloc[-1] bierze ostatni element tej listy
        nth_salary = unique_salaries.nlargest(N).iloc[-1]
        
        return pd.DataFrame({name: [nth_salary]})

    # Jeśli warunek nie jest spełniony (za mało danych lub N<=0)
    return pd.DataFrame({name: [None]})