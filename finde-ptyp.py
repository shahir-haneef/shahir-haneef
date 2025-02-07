import pandas as pd

def find_ptype():
    try:
        capRooms = pd.read_csv('cap_rooms.csv')
        capRooms["Reviews"] = pd.to_numeric(capRooms["Reviews"])
        capRooms_sorted = capRooms.sort_values(by=["PType", "Reviews"], ascending=[True, False])
        return capRooms_sorted.groupby("PType").head(3)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

print(find_ptype())
