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
