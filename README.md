## Backend Challenge

### Built With
- Python
- Flask
- SQL Alchemy
- Vanilla Javascript

### Running Locally
1. Ensure local machine has Python 3.11 installed by running command below in terminal. Update Python version [here](https://www.python.org/downloads/).

```bash
python3 --version
>> Python 3.11.4
```

2. Clone to this repo local machine. Open with VSCode.
   
3. Create .env file using command below in terminal.
```bash
touch .env
```

4. Create key using command below in terminal.
```bash
python -c 'import secrets; print(secrets.token_hex())'
```

5. Copy key from terminal and paste into .env file with FLASK_SECRET_KEY preceding it like example below.
```bash
FLASK_SECRET_KEY=insert_key_here
```

6. Create virtual envionrment by running the following commands in terminal.
```bash
pipenv install
pipenv shell
```
6a. Copy and pase contents of repo's Pipfile into local machines Pipfile. Repeat step 6.

7. Initiliaze databse by running the following commands in terminal.
```bash
flask db init
flask db migrate
flask db upgrade
```

8. Run server by running the following commands in terminal.
```bash
python app.py
````

9. Open index.html in local browser. Ensure live server is disabled.

10. In a **seperate** terminal, run the cURL commands in curl.txt file sequentially. 

