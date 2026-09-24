# Simple Reflex Vacuum Cleaner Agent

def simple_reflex_agent(location, status):
    if status == "Dirty":
        return "Clean"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"


# Environment
location = "A"
room = {
    "A": "Dirty",
    "B": "Dirty"
}

for i in range(10):
    print("Location:", location)
    print("Room status:", room)

    action = simple_reflex_agent(location, room[location])
    print("Action:", action)

    if action == "Clean":
        room[location] = "Clean"

    elif action == "Move Right":
        location = "B"

    elif action == "Move Left":
        location = "A"

    print()
    
    # Stop when both rooms are clean
    if room["A"] == "Clean" and room["B"] == "Clean":
        print("All rooms are clean!")
        break
