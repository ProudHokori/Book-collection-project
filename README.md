# Book Collection Project (BCP)
***
The main objectives of this project is for concluding and applying 
all lesson in Computer Programming I subject and another objective
is for creating program that can help user to store, find and manage
the information of his/her book collection
.


## Modules

My application consists of three main modules that are `book.py`, `bookdata.py` and `display.py`. 


### 1. Module `book.py` 


This module contains the `Book` class for creating a book.


The provided `account.py` contains only some template code that you must
complete yourself. 

### 2. Module `bookdatabase.py`

This module contains the `BankDB` class for creating a database file.

    class BankDB:
        def __init__(self, name):
            self.name = name


        def insert(self, bank_account):
            # add your implementation


        def search(self, account_number):
            # add your implementation


        def delete(self, account_number):
            # add your implementation


        def record_transaction(self, account, amount):
            # add your implementation


        def __repr__(self):
            # add your implementation

The provided `database.py` contains only some template code that you must
complete yourself.


## Running Tests

Tests can be performed by running the `main.py`.  They use the `doctest` to run all
examples found inside all the documentation files in the `docs` directory.

    python main.py

## Your Task

1. Complete the implementations of the `account.py` and `database.py`
   modules.  Make sure they all pass the tests.
2. Run `main.py` to see the result and inspect the correctness.
3. Modify the `summary.txt` file.  In this summary, tell us what you have
   completed and what you have not.

**Notes:** Please do not change any file inside the `docs` directory.  These
files will be used to run tests against your submitted code.


## Submission

1. Check that everything is working as expected, i.e., all the tests are
   passed.
2. Commit your code with all related files
    * `account.py`
    * `database.py`
    * `summary.txt`
3. Push the commit to GitHub
4. Wait for GitHub Classroom to mail back your grading result.

## Grading Criteria

1. **Correctness (70%):** Your program must pass all the doctests.
3. **Cleanliness (30%):** Your program must follow the PEP8 convention.  Variable
   names are meaningful.  Docstrings are written for all methods and
   functions.  Comments are added at certain points for others to understand
   your code easily.
   