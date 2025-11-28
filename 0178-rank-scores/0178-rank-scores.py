import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores["rank"] = None
    if scores["score"].count() == 0: return scores[["score", "rank"]]
    
    scores = scores["score"].sort_values(ascending = False).reset_index()
    scores["rank"] = None
    pom = 1
    max_rank = scores["score"].iloc[0]
    
    

    for x in range(scores["score"].count()):
        if scores["score"].iloc[x] == max_rank:
            scores["rank"].iloc[x] = pom  
        else: 
            pom += 1
            max_rank = scores["score"].iloc[x]
            scores["rank"].iloc[x] = pom

    return scores[["score", "rank"]]
    