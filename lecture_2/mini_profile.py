"""Program for gathering information from a user and presenting a simple summary."""


def generate_profile(age):
    """Define the user's life stage."""
    if 0 <= age <=12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Unknown"


# Getting the user's information
user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby == "stop":
        break
    hobbies.append(hobby)

life_stage = generate_profile(current_age)

user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

# Profile summary
print('-'*3)
print("Profile Summary:")
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