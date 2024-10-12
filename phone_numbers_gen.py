#!/usr/bin/python3

def generate_and_save_phone_numbers(file_name="israeli_phone_numbers.txt"):
    # List of common prefixes used by mobile, VoIP, and landline operators in Israel
    prefixes = ["050", "052", "053", "054", "055", "058", "072", "076", "077"]

    # Open the file in write mode to store the phone numbers
    with open(file_name, "w") as file:
        # Iterate over each prefix in the list
        for prefix in prefixes:
            # Generate and write all possible phone numbers for the current prefix
            for i in range(10 ** 7):  # 7-digit numbers range from 0000000 to 9999999
                number = f"{prefix}{str(i).zfill(7)}"
                file.write(number + "\n")  # Directly write each number to the file
    print(f"All numbers have been saved to {file_name}")


# Generate and save all phone numbers to a text file
generate_and_save_phone_numbers()