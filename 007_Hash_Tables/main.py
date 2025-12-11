def scream():
    print("ahhhhhh!")


user = {
    "age": 54,
    "name": "Kylie",
    "magic": True,
    "scream": scream
}

# Showing data from dict. - O(1)
print(user["age"])

# Adding to dict. - O(1)
user["spell"] = "abra kadabra"

# Using function stored in dict. - O(1)
user["scream"]()

# Is data in dict. - O(1)
print("age" in user)

# Deleting data - O(1)
del user["magic"]
print(user)
