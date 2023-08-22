# Debit Card API in Django

This project implements a Django API to manage users, accounts, and debit cards. Users can perform CRUD operations on these entities, and the cards have the ability to process deposits and expenses with a balance.

## Author
- Carolina Soto Vazquez

## Requirements
- Python 3.x
- Pip (Python package manager)

## Instructions to Run on Windows and macOS

1. Clone this repository: `git clone https://github.com/carosoto1/challenge3`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`
5. Run Migrations: `python manage.py makemigrations`
                   `python manage.py migrate`
6. Run the `main.py` file to generate usage examples.
7. Start the development server: `python manage.py runserver`

## Usage
Once the server is running, you can access the API through the following URL: http://127.0.0.1:8000/

## Important
- Make sure you have Python 3.x installed on your system.
- Make sure you have Git installed on your system to clone the repository.
