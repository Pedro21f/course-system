# Course Management System 📚

A simple and efficient command-line interface (CLI) application built with **Python** and **SQLite3** to manage school or university courses/subjects. The system allows users to create, view, and delete records, saving all data permanently in a local database.

## 🚀 Features

- **Add Subjects:** Insert new courses/subjects into the database with an automatic timestamp.
- **View Subjects:** List all saved subjects alongside their precise creation date and time.
- **Delete Subjects:** Remove a specific subject from the database.
- **Persistent Storage:** Uses SQLite3, meaning data is safe even after closing the program.

## 🛠️ Technologies Used

- **Python 3** (Core logic and CLI)
- **SQLite3** (Relational Database Management System)

## 📁 Project Structure

```text
├── portfolios/
│   ├── classmats.py       # Main application loop and interface (this code)
│   ├── classmatsDB.py     # Database operations (Create, Read, Delete queries)
│   └── materias.sqlite3   # SQLite database file containing the tables
└── README.md
```

## ⚙️ How to Run

1. **Clone the repository** (or download the files):
   ```bash
   git clone https://github.com
   ```

2. **Navigate to the project directory**:
   ```bash
   cd course-system/portfolios
   ```

3. **Run the application**:
   ```bash
   python classmats.py
   ```

## 🎮 How to Use

When you run the script, a menu will appear in your terminal:

```text
 1 - Adicionar | 2 - Ver | 3 - Apagar | Digite -cls- para sair
O que deseja? 
```

- Type `1` to add a new subject.
- Type `2` to display all saved subjects.
- Type `3` to delete an existing subject.
- Type `cls` to safely close the application.
