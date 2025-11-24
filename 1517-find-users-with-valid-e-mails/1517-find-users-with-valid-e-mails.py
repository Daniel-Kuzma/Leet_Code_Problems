import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    #users = users[ ((users["mail"].str.match(r"^[a-z]")) | (users["mail"].str.match(r"^[A-Z]"))) & (users["mail"].str.endswith("@leetcode.com")) & (users["mail"].str.count(r"[^\w\@.-]") == 0) & (users["mail"].str.count("@") == 1)]
    users = users[users["mail"].str.match(r'^[a-zA-Z][\w.-]*@leetcode\.com$')]
    return users


