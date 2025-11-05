# Intro to DB

A comprehensive introduction to database concepts and SQL operations using Python and MySQL.

## 📋 Project Overview

This repository contains educational materials and exercises for learning database fundamentals, including:
- SQL database creation and management
- Database queries and operations
- Python-MySQL integration
- Practical database tasks and exercises

## 📁 Repository Structure

- **MySQLServer.py** - Python script for MySQL server connection and operations
- **alx_book_store.sql** - SQL script for creating the ALX book store database
- **task_2.sql** through **task_6.sql** - Progressive SQL exercises and queries

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- MySQL Server installed and running
- MySQL Python connector (`mysql-connector-python`)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/medob6/Intro_to_DB.git
cd Intro_to_DB
```

2. Install required Python packages:
```bash
pip install mysql-connector-python
```

3. Set up the database:
```bash
mysql -u your_username -p < alx_book_store.sql
```

## 📚 Contents

### Database Setup
- **alx_book_store.sql** - Creates the main book store database schema

### Tasks
- **task_2.sql** - SQL operations exercise 2
- **task_3.sql** - SQL operations exercise 3
- **task_4.sql** - SQL operations exercise 4
- **task_5.sql** - SQL operations exercise 5
- **task_6.sql** - SQL operations exercise 6

### Python Integration
- **MySQLServer.py** - Python script demonstrating MySQL connectivity and operations

## 🛠️ Usage

### Running SQL Tasks
Execute individual SQL task files:
```bash
mysql -u your_username -p alx_book_store < task_2.sql
```

### Using Python Script
Run the Python script:
```bash
python MySQLServer.py
```

## 📖 Learning Objectives

- Understand fundamental database concepts
- Write and execute SQL queries
- Create and manage databases
- Integrate Python with MySQL
- Practice progressive database exercises

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

[medob6](https://github.com/medob6)

---

*Last updated: 2025-11-05*