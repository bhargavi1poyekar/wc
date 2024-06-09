# Word Count (wc)

## Introduction:

This Python script, ccwc.py, is a command-line tool designed to count various attributes of a text file, including the number of bytes, lines, words, and characters. The tool offers flexible options to specify which attribute to count, or to count all attributes by default.

### -> Features
1. Count the number of bytes in a file
2. Count the number of lines in a file
3. Count the number of words in a file
4. Count the number of characters in a file (supports multibyte characters)
5. Handles file errors gracefully with logging

## Usage -> Executing the Script:

You can run the script with different options to count various attributes. Here are some examples:

1. Count bytes in a file

        python3 ccwc.py -c test.txt

2. Count lines in a file

        python3 ccwc.py -l test.txt

3. Count words in a file

        python3 ccwc.py -w test.txt

4. Count characters in a file

        python3 ccwc.py -m test.txt

5. Count bytes, lines, and words by default

    If no flags are provided, the script will count bytes, lines, and words:

        python3 ccwc.py test.txt
    
    Output Format: lines words bytes filename

6. Counting lines and bytes together

        python3 ccwc.py -l -c test.txt
    

## What I Learned
From working on this project, I learned several important concepts and skills:

1. Command-Line Arguments: I gained experience in handling command-line arguments using the argparse module, which allows for flexible input handling and provides helpful usage messages.

2. File Operations: I practiced reading from files and counting various attributes, such as bytes, lines, words, and characters. This also included handling multibyte characters correctly.






