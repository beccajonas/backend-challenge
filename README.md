## Backend Challenge


https://github.com/beccajonas/backend-challenge/assets/87732074/d33b72ce-ddef-4cfb-9aea-bae6f25b19dc


### Built With
- Python
- Flask
- Flask SocketIO
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

*BEFORE STEP 6: Copy and paste the contents of the repository's Pipfile into your local machine's Pipfile if they do not match.*

6. Create virtual envionrment by running the following commands in terminal.
```bash
pipenv install
pipenv shell
```

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

