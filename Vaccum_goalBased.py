# Goal-Based Vacuum Cleaner Agent

def goal_based_agent(location, room):
    # Goal: both rooms should be clean

    if room[location] == "Dirty":
        return "Clean"

    if room["A"] == "Clean" and room["B"] == "Clean":
        return "Stop"

    if location == "A":
        return "Move Right"
    else:
        return "Move Left"


# Environment
location = "A"
room = {
    "A": "Dirty",
    "B": "Dirty"
}

while True:
    print("Location:", location)
    print("Room status:", room)

    action = goal_based_agent(location, room)
    print("Action:", action)

    if action == "Clean":
        room[location] = "Clean"

    elif action == "Move Right":
        location = "B"

    elif action == "Move Left":
        location = "A"

    elif action == "Stop":
        print("Goal achieved! Both rooms are clean.")
        break

    print()
