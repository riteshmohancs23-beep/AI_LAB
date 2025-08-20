#VACCUM CLEANER 
import random
import time

# Define 4 rooms
rooms = {
    "Room A": random.choice(["Clean", "Dirty"]),
    "Room B": random.choice(["Clean", "Dirty"]),
    "Room C": random.choice(["Clean", "Dirty"]),
    "Room D": random.choice(["Clean", "Dirty"])
}

def print_status():
    print("\nCurrent Room Status:")
    for room, status in rooms.items():
        print(f"{room}: {status}")

def vacuum_cleaner():
    print("Vacuum Cleaner Agent Started...\n")
    time.sleep(1)

    for room in rooms.keys():
        print(f"\nVacuum enters {room}...")
        if rooms[room] == "Dirty":
            print(f"{room} is Dirty. Cleaning...")
            rooms[room] = "Clean"
            time.sleep(1)
            print(f"{room} is now Clean ✅")
        else:
            print(f"{room} is already Clean ✅")
        time.sleep(1)

    print("\nAll rooms have been checked and cleaned!\n")

# Initial status
print_status()

# Run the cleaner
vacuum_cleaner()

# Final status
print_status()



#Output
# Current Room Status:
# Room A: Clean
# Room B: Dirty
# Room C: Dirty
# Room D: Clean
# Vacuum Cleaner Agent Started...


# Vacuum enters Room A...
# Room A is already Clean ✅

# Vacuum enters Room B...
# Room B is Dirty. Cleaning...
# Room B is now Clean ✅

# Vacuum enters Room C...
# Room C is Dirty. Cleaning...
# Room C is now Clean ✅

# Vacuum enters Room D...
# Room D is already Clean ✅

# All rooms have been checked and cleaned!


# Current Room Status:
# Room A: Clean
# Room B: Clean
# Room C: Clean
# Room D: Clean
