# Astra Challengue

# Getting Started
1) Create a new directory.
2) Open your favourite IDE and then open your directory. 
3) Open the terminal in working directory:
4) Clone this repository:
```
           git clone https://github.com/jewelazo/astra-challengue.git
```
5) Create a virtual environmnent:
```
            python -m venv .venv
```
6) Activate the virtual environment:
```
            .\.venv\Scripts\activate
```
7) Create your postgresql database and add its values in your .env file, please follow .env.example as template:

8) Install libraries:
```
            (env) pip install -r requirements.txt
```
9) Run Migrations:
```
            (env) python manage.py migrate
```
10) Go to project folder and run this command:
```
            (env) python manage.py runserver
```

  