#!/usr/bin/env python3

import pyperclip


def main():
    # Read the current clipboard text
    original_text = pyperclip.paste()

    # Split it into lines
    lines = original_text.splitlines()

    # Prefix each line with '>>   '
    transformed_lines = [">>   " + line for line in lines]

    # Join back into a single string (with newlines)
    transformed_text = "\n".join(transformed_lines)

    # Copy the result to the clipboard
    pyperclip.copy(transformed_text)

    # Also print it in the console for convenience
    print("Transformed text (also copied to clipboard):\n")
    print(transformed_text)


if __name__ == "__main__":
    main()
