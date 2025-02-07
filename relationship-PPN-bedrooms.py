import pandas as pd
import re
import matplotlib.pyplot as plt

def clean_price(value):
    if isinstance(value, str): 
        value = value.replace("₹", "").replace(",", "").strip()  
        if value.isdigit(): 
            return int(value)
    return None 

def clean_bedrooms(value):
    if isinstance(value, str):  
        value = re.sub(r"\D", "", value)  # Remove non-numeric characters
    try:
        return int(value)
    except ValueError:
        return None

def ppn_bedrooms():
    capRooms = pd.read_csv("cap_rooms.csv")
    capRooms.columns = capRooms.columns.str.strip() 

    capRooms["PPN"] = capRooms["PPN"].apply(clean_price)
    capRooms["Beds"] = capRooms["Beds"].apply(clean_bedrooms)

    capRooms["PPN"] = pd.to_numeric(capRooms["PPN"])
    capRooms["Beds"] = pd.to_numeric(capRooms["Beds"])

    capRooms = capRooms.dropna(subset=["PPN", "Beds"])  

    avg_ppn_per_bed = capRooms.groupby("Beds")["PPN"].mean().sort_values(ascending=False)

    plt.figure(figsize=(10, 5))
    avg_ppn_per_bed.plot(kind="bar", color="skyblue")
    plt.xlabel("Beds")
    plt.ylabel("Average Price Per Night (INR)")
    plt.title("Average PPN Per Beds")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

ppn_bedrooms()
