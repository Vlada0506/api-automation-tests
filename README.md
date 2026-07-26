# API Automation Tests

Automated API tests for the JSONPlaceholder REST API using Python, Pytest, and Requests.

## About the project

This project was created to practice API test automation.

The test suite covers the main HTTP methods:

- GET
- POST
- PUT
- DELETE

Tests verify response status codes, response body content, and API behavior for both positive and negative scenarios.

**API used:** https://jsonplaceholder.typicode.com/


## Technologies

- Python 3
- Requests


## Project Structure

```
api-automation-tests/
│
├── tests/
│   ├── test_get_post.py
│   ├── test_create_post.py
│   ├── test_update_post.py
│   └── test_delete_post.py
│
├── requirements.txt
├── README.md
└── .gitignore
```


## Test Scenarios

### GET

- Get existing post
- Get non-existing post
- Get all posts

### POST

- Create post with valid data
- Create post without title
- Create post with empty title

### PUT

- Update existing post
- Update non-existing post

### DELETE

- Delete existing post
- Delete non-existing post


## How to Run

### Clone the repository

```bash
git clone https://github.com/Vlada0506/api-automation-tests
cd api-automation-tests
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run all tests

```bash
pytest
```

### Run a specific test file

```bash
pytest tests/test_get_post.py
```


## Notes

JSONPlaceholder is a fake REST API intended for learning and testing.

Some API behaviors differ from production APIs. For example:

- invalid data may still return **201 Created**
- updating a non-existing resource may return **500 Internal Server Error**
- deleting a non-existing resource returns **200 OK**

The automated tests validate the **actual behavior** of JSONPlaceholder rather than expected production behavior.


## Author

GitHub: https://github.com/Vlada0506