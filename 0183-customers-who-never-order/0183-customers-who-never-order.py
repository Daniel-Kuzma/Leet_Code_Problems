import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers = customers[~customers["id"].isin(orders["customerId"])].rename(columns = {"id" : "id", "name" : "Customers"})
    return customers.loc[:,"Customers"].to_frame()



"""def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Wybieramy klientów, których ID nie ma w zamówieniach
    # Wyciągamy kolumnę 'name' jako DataFrame i zmieniamy jej nazwę
    return customers[~customers['id'].isin(orders['customerId'])][['name']].rename(columns={'name': 'Customers'})"""