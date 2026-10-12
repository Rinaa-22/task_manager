# 📋 Task Manager CLI

A simple and colorful command-line task manager written in Python.

## ✨ Features

- ➕ Add new tasks with priority (low / medium / high)
- 📋 List all tasks
- ✅ Mark tasks as done
- 🗑️ Remove tasks
- 🔍 Search tasks by keyword
- 🎯 Filter tasks (pending / done)
- 🎨 Colored output for better readability
- 💾 Data stored in a local JSON file
- ❓ Built-in help command

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Steps

1. Clone the repository:

git clone https://github.com/Rinaa-22/task-manager.git
cd task-manager
2. (Optional) Create a virtual environment:

python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # macOS / Linux
3. Install dependencies:

pip install -r requirements.txt
## 📖 Usage

### Add a task

python myproject.py add "Learn Python" --priority high
python myproject.py add "Buy milk"
Priority options: low, medium (default), high

### List all tasks

python myproject.py list
### Filter tasks

python myproject.py list --pending    # Only pending tasks
python myproject.py list --done       # Only completed tasks
### Mark a task as done

python myproject.py done 1
### Remove a task

python myproject.py remove 2
### Search tasks by keyword

python myproject.py search "python"
### Show help

python myproject.py help
## 🖼️ Example Output

[ ] 1. Learn Python (high)
[ ] 2. Buy milk (medium)
[x] 3. Read a book (low)
1/3 jobs done

## 🖼️ Screenshot

![screenshot](Screenshot%20.png)

## 🛠️ Built With

- Python 3.11 — Programming language
- argparse — Command-line argument parsing
- colorama — Colored terminal output
- json — Data storage
- pathlib — File path handling

## 📁 Project Structure

task-manager/
├── myproject.py         # Main program
├── requirements.txt     # Dependencies
├── .gitignore           # Git ignore rules
├── README.md            # This file
└── project_task.json    # Data file (auto-generated)
## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📄 License

This project is open source and available under the [MIT License](https://choosealicense.com/licenses/mit/).

## 👤 Author

Arina Madadi
- GitHub: [@Rinaa-22](https://github.com/Rinaa-22)
