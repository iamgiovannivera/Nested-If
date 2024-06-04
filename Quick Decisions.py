#Quick Decisions: The Event Planner
#Task 1 
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Task2
attendees = int(input("Enter number of attendees: "))

# Determine the venue based on the number of attendees
if attendees > 100:
    venue = "large hall"
else:
    venue = "conference room"

# Determine additional facilities based on the number of attendees
if attendees > 150:
    facilities = "audio system and projector"
elif attendees > 50:
    facilities = "projector"
else:
    facilities = "no additional facilities"

print(f"Venue: {venue}")
print(f"Recommended Facilities: {facilities}")

#Task 3
attendees = int(input("Enter number of attendees: "))

# Determine the venue based on the number of attendees
if attendees > 100:
    venue = "large hall"
else:
    venue = "conference room"

# Determine additional facilities based on the number of attendees
if attendees > 150:
    facilities = "audio system and projector"
elif attendees > 50:
    facilities = "projector"
else:
    facilities = "no additional facilities"

# Ask for food preference
vegetarian = input("Do you want vegetarian food? (yes/no): ").strip().lower()

if vegetarian == "yes":
    caterer = "Veggie Delight Caterers"
else:
    caterer = "Gourmet Meals Caterers"

print(f"Venue: {venue}")
print(f"Recommended Facilities: {facilities}")
print(f"Catering Service: {caterer}")
