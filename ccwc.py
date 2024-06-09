import argparse
import os

def count_bytes(file_path):
    try:
        file_size = os.path.getsize(file_path)
        return file_size
    except OSError as e:
        print(f"Error: {e}")
        return e

def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_lines = len(lines)
        return num_lines
    except OSError as e:
        print(f"Error: {e}")
        return e
    
def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            num_words = len(words)
        return num_words
    except OSError as e:
        print(f"Error: {e}")
        return e
    
def count_characters(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            num_characters = len(content)
        return num_characters
    except OSError as e:
        print(f"Error: {e}")
        return e

def main():
    # Create the parser
    parser = argparse.ArgumentParser()
    
    # Add a flag argument for counting bytes
    parser.add_argument('-c', action='store_true', help='Count the bytes in the file')

    # Add a flag argument for counting lines
    parser.add_argument('-l', action='store_true', help='Count the lines in the file')
    
    # Add a flag argument for counting words
    parser.add_argument('-w', action='store_true', help='Count the words in the file')

    # Add a flag argument for counting characters
    parser.add_argument('-m', action='store_true', help='Count the characters in the file')

    # Add a positional argument for the file path
    parser.add_argument('file_path', type=str, help='Path to the file')
    
    # Parse the arguments
    args = parser.parse_args()
    file_path = args.file_path
    
    if args.file_path and (not args.c) and (not args.l) and not(args.w) and not(args.m):
        bytes = count_bytes(file_path)
        lines = count_lines(file_path)
        words = count_words(file_path)
        print(f'{lines}\t{words}\t{bytes} {file_path}')

    else:
    # Check if the count flag is set and call the appropriate function
        if args.c:
            bytes = count_bytes(args.file_path)
            print(f"{bytes} {file_path}")

        if args.l:
            lines = count_lines(args.file_path)
            print(f"{lines} {file_path}")
        
        if args.w:
            words = count_words(args.file_path)
            print(f"{words} {file_path}")

        if args.m:
            chars = count_characters(args.file_path)
            print(f"{chars} {file_path}")

if __name__ == "__main__":
    main()
