import pandas as pd
import re

def clean_price(value):
    if isinstance(value, str): 
        value = value.replace("₹", "").replace(",", "").strip()  
        if value.isdigit(): 
            return int(value)
    return None 

def find_price():
    try:
        capRooms = pd.read_csv("cap_rooms.csv")
        capRooms["PPN"] = capRooms["PPN"].apply(clean_price)
        capRooms = capRooms.dropna(subset=["PPN"])
        cheapest = capRooms.loc[capRooms.groupby("City")["PPN"].idxmin(), ["City", "ID", "PPN"]].rename(columns={"PPN": "Cheapest_Price"})
        costliest = capRooms.loc[capRooms.groupby("City")["PPN"].idxmax(), ["City", "ID", "PPN"]].rename(columns={"PPN": "Costliest_Price"})
        return pd.merge(cheapest, costliest, on="City")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

print(find_price())



