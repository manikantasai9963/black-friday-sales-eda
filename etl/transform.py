import pandas as pd

def transform_data(matches, deliveries):

    print("Starting data transformation...")

    # Remove duplicates
    matches = matches.drop_duplicates()
    deliveries = deliveries.drop_duplicates()

    # Handle missing values
    matches = matches.fillna("Unknown")

    # Create total_runs column
    deliveries["total_runs"] = deliveries["batsman_runs"] + deliveries["extra_runs"]

    print("Transformation completed")

    return matches, deliveries


from extract import extract_data

if __name__ == "__main__":
    
    matches, deliveries = extract_data()
    
    matches, deliveries = transform_data(matches, deliveries)

    print(matches.head())
    print(deliveries.head())