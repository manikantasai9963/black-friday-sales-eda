from sqlalchemy import create_engine

def load_data(matches, deliveries):

    print("Loading data into PostgreSQL...")

    engine = create_engine(
        "postgresql://postgres:9059%40Post@localhost:5433/ipl_db"
    )

    matches.to_sql(
        "dim_matches",
        engine,
        if_exists="replace",
        index=False
    )

    deliveries.to_sql(
        "fact_deliveries",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded successfully")


if __name__ == "__main__":
    from extract import extract_data
    from transform import transform_data

    matches, deliveries = extract_data()
    matches, deliveries = transform_data(matches, deliveries)

    load_data(matches, deliveries)