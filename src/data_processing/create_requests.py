import pandas as pd
import random


def generate_requests(num=50):

    requests = []

    for i in range(1, num + 1):

        requests.append([
            i,
            "Depot_A",
            f"Customer_{i}",
            random.choice(["Low", "Medium", "High"])
        ])

    return pd.DataFrame(
        requests,
        columns=[
            "request_id",
            "source",
            "destination",
            "priority"
        ]
    )


def save_requests(path="datasets/synthetic/requests.csv", num=50):

    df = generate_requests(num)
    df.to_csv(path, index=False)

    print(f"Saved dataset at: {path}")