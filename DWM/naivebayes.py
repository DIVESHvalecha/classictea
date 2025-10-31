# Training data (Outlook, Temperature, Humidity, Wind, Play)
data = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High", "Weak", "No"],
    ["Sunny", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "Normal", "Weak", "Yes"],
    ["Sunny", "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High", "Strong", "Yes"],
    ["Overcast", "Hot", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Strong", "No"]
]

# Test data
outlook = "Sunny"
temp = "Hot"
humidity = "Normal"
wind = "Strong"

# Function to calculate probability
def calculate_probability(outlook, temp, humidity, wind, target):
    # Step 1: Count total Yes and No
    total_yes = 0
    total_no = 0
    for row in data:
        if row[4] == "Yes":
            total_yes += 1
        else:
            total_no += 1

    # Choose target (Yes or No)
    total_target = total_yes if target == "Yes" else total_no
    prior = total_target / len(data)

    # Step 2: Count matching values for given target
    count_outlook = 0
    count_temp = 0
    count_humidity = 0
    count_wind = 0

    for row in data:
        if row[4] == target:
            if row[0] == outlook:
                count_outlook += 1
            if row[1] == temp:
                count_temp += 1
            if row[2] == humidity:
                count_humidity += 1
            if row[3] == wind:
                count_wind += 1

    # Step 3: Calculate probability of each attribute
    p_outlook = count_outlook / total_target
    p_temp = count_temp / total_target
    p_humidity = count_humidity / total_target
    p_wind = count_wind / total_target

    # Step 4: Multiply all
    return prior * p_outlook * p_temp * p_humidity * p_wind


# Calculate probability for Yes and No
p_no = calculate_probability(outlook, temp, humidity, wind, "No")
p_yes = calculate_probability(outlook, temp, humidity, wind, "Yes")

print("Probability of Yes:", p_yes)
print("Probability of No:", p_no)

# Step 5: Decision
if p_yes > p_no:
    print("Play: Yes")
else:
    print("Play: No")