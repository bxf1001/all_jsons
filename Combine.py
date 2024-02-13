import json

# List of JSON files to combine
file_list = ['user_data_1.json', 'user_data_2.json', 'user_data_3.json', 'user_data_4.json']

# Dictionary to store combined user data
user_data = {}

# Loop through each file and add its user data to the dictionary
for file_name in file_list:
    with open(file_name, 'r') as file:
        data = json.load(file)
        for user_id, user_info in data.items():
            if user_id not in user_data:
                user_data[user_id] = user_info

# Write the combined user data to a new JSON file
with open('user_data.json', 'w') as file:
    json.dump(user_data, file, indent=4)
