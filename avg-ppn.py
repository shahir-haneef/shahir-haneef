import pandas as pd
import re
import matplotlib.pyplot as plt

def clean_price(value):
    if isinstance(value, str): 
        value = value.replace("₹", "").replace(",", "").strip()  
        if value.isdigit(): 
            return int(value)
    return None 

def avg_ppn():
    capRooms = pd.read_csv("cap_rooms.csv")
    capRooms["PPN"] = capRooms["PPN"].apply(clean_price) 
    capRooms = capRooms.dropna(subset=["PPN"]) 
    avg_ppn_per_city = capRooms.groupby("City")["PPN"].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    avg_ppn_per_city.plot(kind="bar", color="skyblue")
    plt.xlabel("City")
    plt.ylabel("Average Price Per Night (INR)")
    plt.title("Average PPN Per City")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

avg_ppn()