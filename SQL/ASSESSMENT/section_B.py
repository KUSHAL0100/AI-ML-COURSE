from sqlalchemy import create_engine, text

# username = "root"
# password = "root"

# engine = create_engine(f"mysql+pymysql://{username}:{password}@localhost/analytics_db")

# with engine.connect() as conn:

#     conn.execute(text("""
#         CREATE TABLE IF NOT EXISTS restaurants(
#             restaurant_id INT PRIMARY KEY,
#             restaurant_name VARCHAR(100)
#         );
#     """))

#     conn.execute(text("""
#         CREATE TABLE IF NOT EXISTS ratings(
#             restaurant_id INT,
#             user_id INT,
#             rating DECIMAL(2,1),
#             PRIMARY KEY (restaurant_id, user_id)
#         );
#     """))

#     conn.commit()

# print("Tables Created Successfully")


"""
CREATE TABLE locations(
    location_id INT PRIMARY KEY,
    city VARCHAR(50)
);

CREATE TABLE restaurants(
    restaurant_id INT PRIMARY KEY,
    restaurant_name VARCHAR(100),
    location_id INT
);

ALTER TABLE restaurants
ADD FOREIGN KEY(location_id)
REFERENCES locations(location_id)
ON DELETE CASCADE; #If the parent row is deleted, all related child rows are automatically deleted too.
"""

# import pandas as pd

# df = pd.read_csv("SQL\ASSESSMENT\zomato.csv")
# df["rating"] = df["rating"].replace(["NEW", "-"], None)
# df["rating"] = pd.to_numeric(df["rating"])
# print(df.head())

"""
CREATE INDEX idx_location
ON restaurants(location_id);

"""