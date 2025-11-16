""" Program for gathering information from a user and presenting a simple summary."""

user_profile = {}
hobbies = []

def generate_profile(age):
    """Define user's life stage."""
    if 0 <= age <=12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Unknown"

# Greetings
print("Hello!")

# Getting user's information
user_name = input("Enter your full name: ")

while True:
    birth_year_str = input("Enter your birth year: ")
    if birth_year_str.isdigit():
        birth_year = int(birth_year_str)
        if 1900 < birth_year <= 2025:
            break
        else:
            print("Your birth year is incorrect")
            continue
    else:
        print("Your birth year is incorrect")

current_age = 2025 - birth_year

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby == "stop":
        break
    if hobby == "" or hobby.isspace():
        continue
    hobbies.append(hobby.strip())

user_profile["name"] = user_name
user_profile["age"] = current_age
user_profile["hobbies"] = hobbies
user_profile["stage"] = generate_profile(current_age)

# Profile summary
print('-'*3)
print("Profile Summary")
print(f'Name: {user_profile.get("name", "Unknown")}')
print(f'Age: {user_profile.get("age", "Unknown")}')
print(f'Life Stage: {user_profile.get("stage", "Unknown")}')
if user_profile.get("hobbies") == []:
    print("You didn't mention any hobbies." )
else:
    print(f'Favorite Hobbies ({len(hobbies)}):')
    for hobby in hobbies:
        print(f'- {hobby}')
print('-'*3)