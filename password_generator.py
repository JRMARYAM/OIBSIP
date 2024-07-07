import random
import string
import argparse


def generate_password(length, include_letters, include_numbers, include_symbols):
    character_pool = ""

    if include_letters:
        character_pool += string.ascii_letters
    if include_numbers:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("No character types selected. Please include at least one character type.")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password


def main():
    parser = argparse.ArgumentParser(description='Generate a random password based on user-defined criteria.')
    parser.add_argument('-l', '--length', type=int, required=True, help='Length of the password')
    parser.add_argument('--letters', action='store_true', help='Include letters in the password')
    parser.add_argument('--numbers', action='store_true', help='Include numbers in the password')
    parser.add_argument('--symbols', action='store_true', help='Include symbols in the password')

    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.letters, args.numbers, args.symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
