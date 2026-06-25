# Jessica Pablo | Lab 3 | Red
# String Ticket 1
username = "Jessica_Pablo"
print(len(username)) # 13
# PREDICT: 13
# C: yes, the length of the string is 13 characters
print(username[0]) # J
# PREDICT: J
print(username[12]) # o
# PREDICT: o
# C: It's -1 because o is at index 12 since it starts with 0.
first = "Jessica"
last = "Pablo"
full = "Welcome to loop, " + "@" + first + " " + last + "!"
print(full) # Welcome to loop, @Jessica_Pablo!
# PREDICT: Welcome to loop, @Jessica_Pablo!

first = "Jessica"
last = "Pablo"
print(f"Welcome to loop, @{first} {last}!")
# PREDICT: Welcome to loop, @Jessica Pablo!
print(username.upper()) # JESSICA_PABLO
#PREDICT: JESSICA_PABLO

#C: The f string is easier because the format is more understandable.

# username[0] = "x"
# TypeError: 'str' object does not support item assignment
# Immunable means string not changable.

#Lists Ticket 2
feed = ["cats", "friends", "dates"]
print(len(feed)) #3
#PREDICT: 3
feed.append("funny videos")
print(feed) # ['cats', 'friends', 'dates', 'funny videos']
# PREDICT: ['cats', 'friends', 'dates', 'funny videos']
feed.pop(0)
feed.sort()
print(feed) # ['dates', 'friends', 'funny videos']
# PREDICT: ['dates', 'friends', 'funny videos']

# Dictionary Ticket 3
profile = {"username": "Jessica_Pablo", "followers": 10000, "verified": True}
print(profile["username"]) # Jessica_Pablo
# PREDICT: Jessica_Pablo
print(profile["followers"]) # 10000
# PREDICT: 10000
print(profile["verified"]) # True
# PREDICT: True
# profile[0]
# KeyError: 0
profile["followers"] += 50
print(profile["followers"])
profile["bio"] = "I love my fat cat!"
print(profile["bio"])
print(profile.get("age"))
# PREDICT: error or nothing
# C: It's safer because it won't show error. It will just say none.

# Capstone Ticket 4
print(f"@" + profile["username"] + " has " + str(profile["followers"]) + " followers and " + str(len(feed)) + " posts." + " Top post: " + feed[0] + ".")
# PREDICT: @Jessica_Pablo has 10050 followers and 3 posts. Top post: dates.