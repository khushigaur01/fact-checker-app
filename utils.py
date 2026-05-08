import pandas as pd



def create_dataframe(results):
    rows = []

    for item in results:
        rows.append({
            "Claim": item["claim"],
            "Status": item["status"],
            "Evidence": item["evidence"]
        })

    return pd.DataFrame(rows)