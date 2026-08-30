import subprocess
from pathlib import Path

supported_languages = ["C", "C++", "Python", "Java"]

def menu_banner():
    ascii_menu = r"""                                                               
 ███████████                                      █████   ████ █████ ███████████
▒▒███▒▒▒▒▒▒█                                     ▒▒███   ███▒ ▒▒███ ▒█▒▒▒███▒▒▒█
 ▒███   █ ▒   ██████  ████████   ███████  ██████  ▒███  ███    ▒███ ▒   ▒███  ▒ 
 ▒███████    ███▒▒███▒▒███▒▒███ ███▒▒███ ███▒▒███ ▒███████     ▒███     ▒███    
 ▒███▒▒▒█   ▒███ ▒███ ▒███ ▒▒▒ ▒███ ▒███▒███████  ▒███▒▒███    ▒███     ▒███    
 ▒███  ▒    ▒███ ▒███ ▒███     ▒███ ▒███▒███▒▒▒   ▒███ ▒▒███   ▒███     ▒███    
 █████      ▒▒██████  █████    ▒▒███████▒▒██████  █████ ▒▒████ █████    █████   
▒▒▒▒▒        ▒▒▒▒▒▒  ▒▒▒▒▒      ▒▒▒▒▒███ ▒▒▒▒▒▒  ▒▒▒▒▒   ▒▒▒▒ ▒▒▒▒▒    ▒▒▒▒▒    
                                ███ ▒███                                        
                               ▒▒██████                                         
                                ▒▒▒▒▒▒    

Generate your project. Start building.
"""
    print(ascii_menu)


def create_project_directory(project_name):
    project_directory = Path(project_name)
    project_directory.mkdir(exist_ok=True)

    return project_directory

def show_supported_languages():
    for option, language in enumerate(supported_languages, start=1):
        print(option, "-", language)

def get_selected_language(language_option):
    language_index = language_option - 1
    chosen_language = supported_languages[language_index]

    return chosen_language

def initialize_git(project_directory):
    subprocess.run(["git", "init"], cwd=project_directory)

def create_project_structure(project_path, project_language):

    match project_language:
        case "C":
            initial_file_name = "main.c"
        case "C++":
            initial_file_name = "main.cpp"
        case "Python":
            initial_file_name = "main.py"
        case "Java":
            initial_file_name = "main.java"
        case _:
            print("Invalid option. Please choose a number from 1 to 4.")

    match project_language:
        case "C" | "C++":
            include_path = project_path / "include"
            include_path.mkdir(exist_ok=True)

    src_path = project_path / "src"
    src_path.mkdir(exist_ok=True)

    initial_file_path = src_path / initial_file_name
    template_file_path = Path(__file__).parent / "templates" / initial_file_name
    template_content = template_file_path.read_text()
    initial_file_path.write_text(template_content)

    readme_file_path = Path(__file__).parent / "templates" / "README.md"
    readme_content = readme_file_path.read_text()
    readme_path = project_path / "README.md"
    readme_path.write_text(readme_content)

    

def main():
    menu_banner()

    project_name = input("Project name: ")
    project_path = create_project_directory(project_name)

    show_supported_languages()

    selected_language = int(input("Enter the number of the desired option: "))
    project_language = get_selected_language(selected_language)

    git_response = input("Initialize Git repository? (y/n): ").lower()

    if git_response == "y":
        initialize_git(project_path)

    create_project_structure(project_path, project_language)

main()