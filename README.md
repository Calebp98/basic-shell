# Simple Shell Program

## Overview

This is a simple shell program implemented in Python that allows users to execute basic shell commands. It supports a limited set of built-in commands and can also execute external commands found in the system's PATH.

## Features

- **Built-in Commands**: The shell supports the following built-in commands:

  - `echo`: Prints the provided arguments to the standard output.
  - `exit`: Exits the shell.
  - `type`: Displays whether a command is a built-in or provides its path if it's an external command.
  - `pwd`: Prints the current working directory.
  - `cd`: Changes the current directory.

- **External Command Execution**: The shell can execute external commands that are available in the system's PATH.

## Requirements

- Python 3.x
- Basic knowledge of shell commands

## Usage

1. Clone the repository or download the script.
2. Run the script using Python:
   ```bash
   python your_script_name.py
   ```
3. You will see a prompt (`$ `) where you can enter commands.

## Example Commands

- To print a message:

  ```bash
  echo Hello, World!
  ```

- To check the type of a command:

  ```bash
  type echo
  ```

- To print the current working directory:

  ```bash
  pwd
  ```

- To change the directory:

  ```bash
  cd /path/to/directory
  ```

- To exit the shell:
  ```bash
  exit
  ```

## License

This project is licensed under the MIT License.
