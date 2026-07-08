## QueryVault – Building a Database Management System from Scratch

### INDEX
 - [Project Overview](#Project-Overview)
 - [Problem Statement](#Problem-Statement)
 - [Objectives](#Objectives)
 - [Learning Outcomes](#Learning-Outcomes)
 - [Tech Stack](#Tech-Stack)
 - [Project Architecture](#Project-Architecture)
 - [file structure](#file-structure)
 - [Development Roadmap](#Development-Roadmap)
 - []()


### Project Overview

**QueryVault** is an educational Database Management System (DBMS) built from scratch using Python. Instead of relying on existing database systems like MySQL or PostgreSQL, this project focuses on understanding how a database works internally by implementing its core components step by step.

The project is designed not only to execute SQL queries but also to visualize how those queries are processed inside a database engine.

### Problem Statement

Modern databases efficiently process millions of records, but the internal mechanisms behind query execution are often hidden from users.

QueryVault aims to solve this by creating a simplified database engine that allows users to:

* Store and manage data
* Execute SQL queries
* Understand how a DBMS processes queries internally
* Visualize each stage of query execution

This project bridges the gap between theoretical DBMS concepts and practical implementation.

### Objectives

* Learn the internal architecture of a DBMS.
* Implement database operations from scratch.
* Build a basic SQL query processor.
* Visualize query execution step by step.
* Understand indexing, transactions, and concurrency control.
* Develop a full-stack application around a custom database engine.

### Learning Outcomes

After completing this project, you will understand:

* How data is stored
* Table organization
* Row and column management
* CRUD operations
* SQL parsing
* Query execution
* Query optimization
* Indexing
* Transactions
* Concurrency Control
* Database architecture

### Tech Stack

#### Backend
* Python
* FastAPI (later phase)

#### Frontend
* HTML
* CSS
* JavaScript
* React (later phase)

#### Storage
* JSON Files (initial implementation)

### Project Architecture

                 Browser
                    ↓
          React Frontend (Visualization)
                    ↓
            FastAPI Backend
                    ↓
             Query Engine
                    ↓
        Storage Layer (JSON files)

### file structure 

```
QUERYVAULT
|
├── core
|     └── databas_manager.py
|
├── database/
|    ├── courses.json
|    ├── enrollments.json
|    └── students.json
|
├── models
|
├── main.py
└── README.md
```

### Development Roadmap

### Phase 1 – Storage Engine

### Goal

Create a simple storage engine using JSON files.

### Concepts Covered

* Tables
* Rows
* Columns
* Primary Keys
* Data Storage

Example:

```text
database/
│
├── students.json
├── courses.json
└── enrollments.json
```

---

## Phase 2 – CRUD Operations

Implement basic database operations.

Functions:

* insert()
* select()
* update()
* delete()

Concepts Learned:

* Data manipulation
* Record management
* Basic database functionality

---

## Phase 3 – SQL Parser

Accept SQL queries and convert them into an internal representation.

Example Query:

```sql
SELECT *
FROM Students
WHERE age > 18;
```

Internal Representation:

```python
{
    "table": "Students",
    "condition": "age > 18"
}
```

Concepts Learned:

* SQL Parsing
* Query Representation
* Abstract Syntax Tree (Simplified)

---

## Phase 4 – Query Execution Engine

Execute parsed queries step by step.

Execution Pipeline:

```text
Table Scan
      ↓
Apply Filter
      ↓
Generate Result
```

Concepts Learned:

* Table Scan
* Filtering
* Execution Pipeline

---

## Phase 5 – Aggregation

Support SQL operations such as:

* ORDER BY
* GROUP BY
* COUNT()
* SUM()
* AVG()

Example Execution:

```text
Scan Table
      ↓
Group Records
      ↓
Aggregate Values
      ↓
Return Output
```

Concepts Learned:

* Aggregation
* Sorting
* Grouping

---

## Phase 6 – JOIN Operations

Implement joins between multiple tables.

Example:

```sql
SELECT s.name, c.course
FROM Students s
JOIN Enrollments e
ON s.id = e.student_id
JOIN Courses c
ON c.id = e.course_id;
```

Execution Pipeline:

```text
Scan Students
        ↓
Scan Enrollments
        ↓
Join Tables
        ↓
Scan Courses
        ↓
Join Again
        ↓
Return Result
```

Concepts Learned:

* JOIN Algorithms
* Relational Databases
* Multi-table Queries

---

## Phase 7 – Indexing

Implement indexes to improve query performance.

Without Index:

```text
Linear Search
```

With Index:

```text
Index Lookup
```

Concepts Learned:

* B-Tree
* Searching
* Query Optimization
* Performance Improvement

---

## Phase 8 – Transactions

Support transactional operations.

Example:

```sql
BEGIN;

UPDATE Accounts
SET balance = balance - 100
WHERE id = 1;

COMMIT;
```

Execution Pipeline:

```text
Begin Transaction
        ↓
Modify Data
        ↓
Write Log
        ↓
Commit
```

Concepts Learned:

* ACID Properties
* Commit
* Rollback
* Recovery

---

## Phase 9 – Concurrency Control

Simulate multiple users accessing the database simultaneously.

Concepts Covered:

* Shared Locks
* Exclusive Locks
* Deadlocks
* Lost Update Problem
* Isolation Levels

---

# Future Improvements

* Graphical query execution visualization
* ER Diagram generation
* Query optimization techniques
* Cost-based optimizer
* B+ Tree indexing
* Buffer Manager
* Page Management
* Disk-based storage engine
* Multi-user support
* Authentication and authorization
* Database backup and recovery

---

# Why This Project?

QueryVault is more than just a CRUD application.

It is a learning-oriented project that recreates the core components of a database system from scratch. By implementing each module yourself, you gain a deeper understanding of DBMS concepts that are usually hidden behind existing database software.

The goal is to transform theoretical knowledge into practical engineering experience while building a portfolio project that demonstrates database internals, software design, and full-stack development skills.






