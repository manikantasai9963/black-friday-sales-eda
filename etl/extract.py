import pandas as pd

def extract_data():

    matches = pd.read_csv("data/raw/matches.csv")
    deliveries = pd.read_csv("data/raw/deliveries.csv")

    print("Data extracted successfully")

    return matches, deliveries