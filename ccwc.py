#!usr/bin/env python3

import argparse
import logging
import os

# Configure logging
logging.basicConfig(filename='file_counter.log', level=logging.INFO)

def count_bytes(file_path):
    """
    Count the number of bytes in a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        Optional[int]: Number of bytes in the file, or None if an error occurs.
    """
    try:
        file_size = os.path.getsize(file_path)
        return file_size
    except OSError as e:
        logging.error(f"Error counting bytes: {e}")
        return None

def count_lines(file_path):
    """
    Count the number of lines in a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        Optional[int]: Number of lines in the file, or None if an error occurs.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_lines = len(lines)
        return num_lines
    except OSError as e:
        logging.error(f"Error counting lines: {e}")
        return None
    
def count_words(file_path):
    """
    Count the number of words in a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        Optional[int]: Number of words in the file, or None if an error occurs.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            num_words = len(words)
        return num_words
    except OSError as e:
        logging.error(f"Error counting words: {e}")
        return None
    
def count_chars(file_path):
    """
    Count the number of characters in a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        Optional[int]: Number of characters in the file, or None if an error occurs.
    """
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            num_characters = len(content)
        return num_characters
    except OSError as e:
        logging.error(f"Error counting characters: {e}")
        return None

def print_output(bytes=None, lines=None, words=None, chars=None):
    if lines:
        print(f'{lines}', end ='\t')
    if words:
        print(f'{words}', end ='\t')
    if bytes:
        print(f'{bytes}', end ='\t')
    if chars:
        print(f'{chars}', end ='\t')

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

    bytes = count_bytes(file_path)
    lines = count_lines(file_path)
    words = count_words(file_path)
    chars = count_chars(file_path)
    
    if not any([args.c, args.l, args.w, args.m]):
        print_output(bytes=bytes, lines=lines, words=words)

    else:
    # Check if the count flag is set and call the appropriate function
        if args.l:
            print_output(lines=lines)
        
        if args.w:
            print_output(words=words)

        if args.c:
            print_output(bytes=bytes)

        if args.m:
            print_output(chars=chars)
        
    print(file_path)

if __name__ == "__main__":
    main()
