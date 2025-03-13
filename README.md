# Reply-From Line-Prefixer

This small Python script reads text from your clipboard, prefixes each line with `">>   "`, and copies the transformed text back to your clipboard. It also prints the result to your console.

## Features
- Reads the clipboard contents (via [pyperclip](https://pypi.org/project/pyperclip/)).
- Splits the text by line.
- Prefixes each line with `">>   "`.
- Copies the new text back to the clipboard.
- Prints the transformed text to the console for confirmation.

## Requirements
- Python 3.6+ (tested up to Python 3.10)
- [pyperclip](https://pypi.org/project/pyperclip/) (for clipboard access)

## Installation

1. **Clone this repository** (or just copy the script to your local environment):
   ```bash
   git clone https://github.com/mholzinger/reply-from.git
   cd reply-from
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

**Or simply**

  ```bash
  pip install pyperclip
  ```

## Usage

1. Copy some text to your clipboard (e.g., from a LinkedIn post or any text editor).

1. Run the script:

   ```bash
   python line_prefixer.py
   ```

- This script will:
  - Read the clipboard content.
  - Prefix each line with ">> ".
  - Copy the resulting text back to the clipboard.
  - Print the result in the terminal.

3. Paste the updated text wherever you need it (e.g., in an email, a chat, or a text editor). You’ll see each line now starts with `">> "`.

## Example
Original clipboard text

   ```text
   IMMEDIATE NEED FOR SENIOR PLATFORM OPERATIONS ENGINEER
   Hello Connections,

   Role: Senior Platform Operations Engineer
   Location: Remote
   ```

After running the script

---

   Hi, Thanks for reaching out.  
>   
> *>>   IMMEDIATE NEED FOR SENIOR PLATFORM OPERATIONS ENGINEER*  
> *>>   Hello Connections*  
> *>>*  
> *>>   Role: Senior Platform Operations Engineer*  
> *>>   Location: Remote*  

---

## Linting
This script follows the [flake8](https://pypi.org/project/flake8/) style guidelines:

- 4-space indentation
- No trailing whitespace
- 79-character max line length (if applicable)
etc.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
