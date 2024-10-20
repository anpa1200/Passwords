import itertools
import string

# Predefined list of special symbols
basic_special_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '~']

def cool_script_open():
    print("""
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                           PERSONAL PASS GENERATOR                           ║
    ║                           Created by Andrey Pautov                          ║
    ║                            Email: 1200km@gmail.com                          ║
    ║─────────────────────────────────────────────────────────────────────────────║
    ║   ⚠️  Please note: This tool may generate a very large password list        ║
    ║   (ranging from 1GB to 30GB or more), depending on the input data.          ║
    ║   The list contains many personalized password combinations, making it      ║
    ║   a powerful tool for security professionals.                               ║
    ║─────────────────────────────────────────────────────────────────────────────║
    ║   🔑  What's inside:                                                        ║
    ║   - Personalized passwords based on names, dates, nicknames, and more.      ║
    ║   - Variations using upper/lowercase, special characters, and numbers.      ║
    ║   - Smart combinations that strengthen the password list's complexity.      ║
    ║─────────────────────────────────────────────────────────────────────────────║
    ║    💡  TIP: You can use this tool to test password security or to create     ║
    ║    passwords tailored to your preferences and personal details.             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝
    """)

def generate_additional_values():
    # Ensure basic_special_symbols is defined
    basic_special_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '~']

    # List to hold additional values
    additional_values = []

    # Characters pool: numbers, lowercase and uppercase letters, and special symbols
    char_pool = list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase) + basic_special_symbols

    # Add each number, each lowercase/uppercase character, and each special symbol
    additional_values.extend(char_pool)

    # Generate combinations of two characters from the char pool
    two_char_combinations = [''.join(comb) for comb in itertools.product(char_pool, repeat=2)]
    additional_values.extend(two_char_combinations)

    # Generate combinations of three characters from the char pool
    three_char_combinations = [''.join(comb) for comb in itertools.product(char_pool, repeat=3)]
    additional_values.extend(three_char_combinations)
    return additional_values

def to_leet_speak(basic_values):
    # 1337 mode
    leet_dict = {
        'A': '4', 'a': '@','B': '8', 'c': '(', 'C': '(', 'e': '3', 'E':'3',
        'g': '9', 'h': '#', 'i': '!', 'o': '0', 'O':'0',
        's': '$', 't': '7', 'S':'$', 'z': '2', 'Z':2
    }
    new_values = []
    for value in basic_values:
        new_value = ''.join(leet_dict.get(char, char) for char in value.lower())
        new_values.append(new_value)
    basic_values.extend(new_values)

def gather_information():
    # Helper function to add a value with different capitalizations
    def add_variants(value, target_list):
        if value:  # Only if the value is not empty
            target_list.append(value.lower())             # Lowercase
            target_list.append(value.capitalize())        # First character uppercase
            target_list.append(value.upper())             # Uppercase

    # Helper function for valid string input, allowing empty values
    def get_optional_string(prompt):
        return input(prompt).strip().lower()

    # Helper function for valid birthdate input (in DDMMYYYY format)
    def get_valid_birthdate(prompt):
        while True:
            value = input(prompt).strip().lower()
            if len(value) == 8 and value.isdigit():
                return value
            elif value == "":
                return ""  # Allow empty value for birthdate
            else:
                print("Invalid birthdate format. Please enter in DDMMYYYY format.")

    # Helper function for valid integer input
    def get_valid_integer(prompt, default=0):
        while True:
            value = input(prompt).strip()
            if value == "":
                return default
            try:
                value = int(value)
                if value < 0:
                    raise ValueError("The number cannot be negative.")
                return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Gather information from the user
    user_info = {}

    # Basic personal info

    user_info['first_name'] = get_optional_string("Enter First Name (optional): ")
    user_info['last_name'] = get_optional_string("Enter Last Name (optional): ")
    user_info['birthdate'] = get_valid_birthdate("Enter Birthdate (DDMMYYYY, optional): ")
    user_info['nickname'] = get_optional_string("Enter Nickname (optional): ")
    user_info['phone_number'] = get_optional_string("Enter Phone Number (optional): ")
    user_info['ID_number'] = get_optional_string("Enter ID Number (optional): ")

    # Partner's info
    user_info['partners_name'] = get_optional_string("Enter Partner's Name (optional): ")
    user_info['partners_nickname'] = get_optional_string("Enter Partner's Nickname (optional): ")
    user_info['partners_birthdate'] = get_valid_birthdate("Enter Partner's Birthdate (DDMMYYYY, optional): ")

    # Exception handling for number of children
    user_info['number_of_children'] = get_valid_integer("Enter Number of Children (default is 0): ", default=0)
    user_info['children_names'] = []
    user_info['children_birthdates'] = []

    for i in range(user_info['number_of_children']):
        child_name = get_optional_string(f"Enter Child {i + 1} Name (optional): ")
        child_birthdate = get_valid_birthdate(f"Enter Child {i + 1} Birthdate (DDMMYYYY, optional): ")
        user_info['children_names'].append(child_name)
        user_info['children_birthdates'].append(child_birthdate)

    # Exception handling for number of pets
    user_info['number_of_pets'] = get_valid_integer("Enter Number of Pets (default is 0): ", default=0)
    user_info['pet_names'] = []

    for i in range(user_info['number_of_pets']):
        pet_name = get_optional_string(f"Enter Pet {i + 1} Name (optional): ")
        user_info['pet_names'].append(pet_name)

    # Additional info
    user_info['company_name'] = get_optional_string("Enter Company Name (optional): ")
    user_info['profession_name'] = get_optional_string("Enter Profession Name (optional): ")
    user_info['special_words'] = get_optional_string("Enter Special Words (optional): ")

    # Create the basic_values list
    basic_values = []

    # Add basic personal info with variants
    add_variants(user_info['first_name'], basic_values)
    add_variants(user_info['last_name'], basic_values)
    if user_info['birthdate']:
        basic_values.append(user_info['birthdate'])  # Add full birthdate
        basic_values.append(user_info['birthdate'][4:])  # Add year YYYY
        basic_values.append(user_info['birthdate'][:4])  # Add day and month DDMM
    add_variants(user_info['nickname'], basic_values)
    add_variants(user_info['phone_number'], basic_values)
    add_variants(user_info['ID_number'], basic_values)

    # Add partner's info with variants
    add_variants(user_info['partners_name'], basic_values)
    add_variants(user_info['partners_nickname'], basic_values)
    if user_info['partners_birthdate']:
        basic_values.append(user_info['partners_birthdate'])
        basic_values.append(user_info['partners_birthdate'][4:])
        basic_values.append(user_info['partners_birthdate'][:4])

    # Add children's info with variants
    for name in user_info['children_names']:
        add_variants(name, basic_values)
    for birthdate in user_info['children_birthdates']:
        add_variants(birthdate, basic_values)

    # Add pet's info with variants
    for pet_name in user_info['pet_names']:
        add_variants(pet_name, basic_values)

    # Add additional info with variants
    add_variants(user_info['company_name'], basic_values)
    add_variants(user_info['profession_name'], basic_values)
    add_variants(user_info['special_words'], basic_values)

    return basic_values


def generate_passwords(basic_values, additional_values, len_bv, add_symbols):
    passwords = set()  # Use a set to ensure unique passwords

    # 1. Add each value from basic_values to the passwords list
    for bval in basic_values:
        passwords.add(bval)

    if add_symbols == "y":
        # Iterate over each combination of additional_values (addval) and basic_values (bval)
        for bval in basic_values:
            for addval in additional_values:
                # Combination: addval + bval
                passwords.add(f"{addval}{bval}")
                # Combination: bval + addval
                passwords.add(f"{bval}{addval}")
                # Combination: addval + bval + addval
                passwords.add(f"{addval}{bval}{addval}")

        # More combinations with multiple basic values if the list is long enough
        if len_bv > 3:
            for i, bval1 in enumerate(basic_values):
                for j, bval2 in enumerate(basic_values):
                    if bval1 != bval2:
                        # Combination: bval1 + bval2
                        passwords.add(f"{bval1}{bval2}")
                        for addval in additional_values:
                            # Combination involving addvals around and between bvals
                            passwords.add(f"{addval}{bval1}{bval2}")
                            passwords.add(f"{addval}{bval1}{bval2}{addval}")
                            passwords.add(f"{bval1}{bval2}{addval}")
                            passwords.add(f"{addval}{bval1}{addval}{bval2}{addval}")
                            passwords.add(f"{bval1}{addval}{bval2}{addval}")
                            passwords.add(f"{bval1}{addval}{bval2}")
                            passwords.add(f"{addval}{bval1}{addval}{bval2}")

    elif add_symbols == "n":
        # Combinations only with basic_values
        if len_bv > 3:
            for i, bval1 in enumerate(basic_values):
                for j, bval2 in enumerate(basic_values):
                    if bval1 != bval2:
                        # Combination: bval1 + bval2
                        passwords.add(f"{bval1}{bval2}")

    return passwords


def main():
    # Step 1: Generate additional values (predefined and character combinations)
    additional_values = generate_additional_values()
    cool_script_open()
    mode1337 = input("Enable 1337 Leet mode? y/n: ").lower()
    while mode1337 not in ['y', 'n']:
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")
        mode1337 = input("Enable 1337 Leet mode? y/n: ").lower()

    # Step 2: Gather basic values from user input
    basic_values = gather_information()
    len_bv = len(basic_values)

    # Step 3: Generate passwords based on the basic and additional values
    add_symbols = input("Do you want to add additional symbols, like @pass#? y/n: ").lower()
    while add_symbols not in ['y', 'n']:
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")
        add_symbols = input("Do you want to add additional symbols, like @pass#? y/n: ").lower()

    # New Step: Set password length limits
    min_len = int(input("Enter minimum password length (default is 4): "))
    max_len = int(input("Enter maximum password length (default is 12): "))

    # Ensuring min_len is between 1 and 20
    while min_len not in range(1, 21):
        print("Invalid input. Please enter a number from 1 to 20.")
        try:
            min_len = int(input("Enter minimum password length (default is 4): "))
        except ValueError:
            print("Please enter a valid number.")

    # Ensuring max_len is between 1 and 20 and not less than min_len
    while max_len not in range(1, 21) or max_len < min_len:
        if max_len < min_len:
            print("Maximum length cannot be less than minimum length.")
        else:
            print("Invalid input. Please enter a number from 1 to 20.")
        try:
            max_len = int(input("Enter maximum password length (default is 12): "))
        except ValueError:
            print("Please enter a valid number.")

    try:
        min_len = int(min_len)
    except ValueError:
        min_len = 4  # Default minimum length
    if min_len < 1:
        min_len = 4

    try:
        max_len = int(max_len)
    except ValueError:
        max_len = 12  # Default maximum length
    if max_len < min_len:
        max_len = min_len

    print("Tool is working now, it can take few minutes")
    passwords = generate_passwords(basic_values, additional_values, len_bv, add_symbols)

    # Filter passwords based on length
    passwords = {pw for pw in passwords if min_len <= len(pw) <= max_len}

    # Step 4: Save passwords to a text file
    with open("special_list.txt", "w") as file:
        for password in passwords:
            file.write(f"{password}\n")

    print("\nPasswords generated and saved successfully in 'special_list.txt'")
    print(f"Generated {len(passwords)} passwords.")
    print("________________________________________________________________________")
    print("Generated with PPG - personal pass generator ")
    print("For additional information about this tool send me email: 1200km@gmail.com")


# Run the main function
if __name__ == "__main__":
    main()

