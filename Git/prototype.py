# meeting_time_app.py

# Prototype: Single-user Meeting Time App

# Data structure to hold participant availability
data = []

def enter_availability():
    print("Enter participant availability data")
    while True:
        name = input("Enter participant name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        best_times = input("Enter best times (comma-separated, e.g. 9-10am,2-3pm): ")
        worst_times = input("Enter worst times (comma-separated, e.g. 12-1pm,4-5pm): ")
        participant = {
            'name': name,
            'best_times': [t.strip() for t in best_times.split(',')],
            'worst_times': [t.strip() for t in worst_times.split(',')]
        }
        data.append(participant)
        

def calculate_best_time():
    # create an empty dictionary to count votes for the best_times
    print("\nCalculating best time...")
    time_counter = {}
    for participant in data:
        for time in participant['best_times']:
            time_counter[time] = time_counter.get(time, 0) + 1

    # Convert the dictionary items into a sorted tuple in decending order with the most votes 
    # as the first item, then print the result
    sorted_times = sorted(time_counter.items(), key=lambda x: x[1], reverse=True)
    if sorted_times:
        print("Suggested time: ", sorted_times[0][0], "with", sorted_times[0][1], "votes")
    else:
        print("No times entered.")

def main():
    print("=== Meeting Time App Prototype ===")
    enter_availability()
    calculate_best_time()

if __name__ == "__main__":
    main()
