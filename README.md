# Password-Manager-Py

This is a simple password manager application built with Python using the Tkinter library. It allows users to save, retrieve, and generate passwords for different websites.

## Features

- Users can add new website details including website name, email/username, and password.
- Passwords can be generated automatically with a combination of letters, symbols, and numbers.
- Users can search for saved website details by providing the website name.
- The application uses a JSON file to store the saved website details securely.

## Installation

1. Clone the repository

2. Install required dependencies

3. Run the application

## Usage

1. Launch the application.
2. Enter the website name, email/username, and password.
3. Click on the "Generate Password" button to generate a random password.
4. Click on the "Add" button to save the website details.
5. To retrieve saved website details, enter the website name and click on the "Search" button.

## Files

- `main.py`: Main Python script containing the GUI code and functionality for adding, searching, and saving website details.
- `data.json`: JSON file used to store the saved website details.

## Dependencies

- [Tkinter](https://docs.python.org/3/library/tkinter.html): Standard GUI toolkit for Python.
- [pyperclip](https://pypi.org/project/pyperclip/): Cross-platform module for copying and pasting text to/from the clipboard.
