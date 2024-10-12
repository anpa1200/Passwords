#!/usr/bin/python3
import base64

def encode_to_base64(username, password):
    combined_string = f"{username}:{password}"
    return base64.b64encode(combined_string.encode('utf-8')).decode('utf-8')

def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file {filepath} does not exist.")
        main()
        return None

def write_to_file(file_path, encoded_pairs):
    with open(file_path, "w") as output_file:
        for pair in encoded_pairs:
            output_file.write(pair + "\n")

def process_pairs(usernames, passwords):
    return [encode_to_base64(username, password) for username in usernames for password in passwords]

def handle_multiple_usernames():
    usernames_file = input("Enter the path to the usernames file: ")
    passwords_file = input("Enter the path to the passwords file: ")
    usernames = read_file(usernames_file)
    passwords = read_file(passwords_file)
    if usernames and passwords:
        encoded_pairs = process_pairs(usernames, passwords)
        write_to_file("matches_base64.txt", encoded_pairs)
        print("All encoded pairs have been saved to matches_base64.txt.")

def handle_single_username():
    username = input("Enter the username: ")
    passwords_file = input("Enter the path to the passwords file: ")
    passwords = read_file(passwords_file)
    if passwords:
        encoded_pairs = [encode_to_base64(username, password) for password in passwords]
        write_to_file("matches_base64.txt", encoded_pairs)
        print("All encoded pairs have been saved to matches_base64.txt.")

def main():
    response = input("Create matchlist for a specific username? (y/n): ").lower()
    if response == "y":
        handle_single_username()
    elif response == "n":
        handle_multiple_usernames()
    else:
        print("Please enter 'y' or 'n'.")
        main()

if __name__ == "__main__":
    main()
