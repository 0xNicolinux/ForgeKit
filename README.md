# ForgeKit

**Generate your project. Start building.**

ForgeKit is a simple command-line tool for quickly creating the initial structure of a project. Choose a name, select a language, and let ForgeKit set up the basics so you can start building.

## Supported Languages

* C
* C++
* Python
* Java

Depending on the selected language, ForgeKit creates the initial source directory and files. For C and C++ projects, an `include` directory is also created.

## Features

* Create a project directory
* Generate an initial project structure
* Add starter source files from templates
* Generate a README for the new project
* Optionally initialize a Git repository

## Usage

Clone the repository and run the script:

```bash
git clone https://github.com/0xNicolinux/ForgeKit.git
cd ForgeKit
python src/main.py
```

Then follow the prompts:

```text
Project name: my-project

1 - C
2 - C++
3 - Python
4 - Java

Enter the number of the desired option:
Initialize Git repository? (y/n):
```

## Project Structure

A generated project will follow a structure similar to this:

```text
my-project/
├── src/
│   └── main.py
└── README.md
```

C and C++ projects also include:

```text
my-project/
├── include/
├── src/
│   └── main.cpp
└── README.md
```

## Requirements

* Python 3
* Git *(optional, if you want ForgeKit to initialize repositories)*

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
