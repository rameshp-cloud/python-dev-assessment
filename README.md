# Python Developer Assessment

## Overview

This repository contains my completed Python Developer Assessment tasks.

The assessment covers Python development, Git and GitHub, code quality, data structures and algorithms, object-oriented programming, error handling, debugging, and API interaction.

## Completed Tasks

### Phase 1: Python Setup and Git/GitHub

- Set up the Python development environment.
- Created and ran a basic Python program.
- Practiced Git and GitHub workflow.
- Used branches and pull requests.
- Applied code formatting and linting using Black and Flake8.

### Phase 2: Python Programming

#### Data Structures and Algorithms

Implemented:

- `filter_and_sort_evens()`
  - Filters even numbers from a list.
  - Sorts the resulting numbers in ascending order.

- `count_character_frequency()`
  - Counts the frequency of each character in a string.

#### Object-Oriented Programming

Implemented a `Book` class with:

- `title`
- `author`
- `isbn`
- `publication_year`
- `get_age()`
- `get_summary()`

The `get_age()` method calculates the age of a book using 2026 as the current year.

#### Error Handling and Debugging

Implemented error handling for:

- Calculating the average of a list.
- Handling an empty list.
- Handling an index that is out of range.
- Handling invalid list and index types.

### Phase 3: API Interaction

Implemented API interaction using the JSONPlaceholder API.

The function:

```python
fetch_and_display_users(num_users)
```

retrieves user information and displays:

- Name
- Email
- City

The API interaction includes error handling for:

- Network/request errors.
- Non-successful HTTP status codes.
- Unexpected API response formats.
- Missing or invalid user data.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/rameshp-cloud/python-dev-assessment.git
cd python-dev-assessment
```

### 2. Install the required package

```bash
python -m pip install requests
```

### 3. Run the Python programs

```bash
python hello.py
python dsa_challenges.py
python book_store.py
python debug_errors.py
python api_client.py
```

### 4. Format the code with Black

```bash
black .
```

### 5. Check code quality with Flake8

```bash
flake8 .
```

## Git Workflow

The assessment was completed using separate Git branches for different tasks.

The completed task branches were merged into the `main` branch using GitHub pull requests.

The final `main` branch contains all completed assessment files.

## Reflections

This assessment helped me improve my understanding of Python programming and software development practices.

I practiced writing functions, working with lists and strings, creating classes, handling errors, debugging code, and interacting with a REST API.

I also gained practical experience with Git and GitHub, including creating branches, making commits, creating pull requests, and merging branches into the `main` branch.

The assessment helped me understand the importance of writing clean, readable, and maintainable Python code and using tools such as Black and Flake8 to improve code quality.

## Repository Structure

```text
python-dev-assessment/
│
├── README.md
├── hello.py
├── bad_style.py
├── dsa_challenges.py
├── book_store.py
├── debug_errors.py
└── api_client.py
```

## Status

The Python Developer Assessment tasks have been completed.

All completed task branches have been merged into the `main` branch.
