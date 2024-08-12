Start localy:

Install python via pyenv:
```
pyenv install 3.9.11
pyenv global 3.9.11
```

Create virtual env:
```
python -m venv app/.venv

# windows
./app/.venv/Scripts/activate.bat

# unix
source ./app/.venv/bin/activate
```

Install deps:
```
cd app
pip install -r requirements.txt
cd ..
```

Install dotenv-cli if we need this
```
pip install "python-dotenv[cli]"
```

Start server
```
dotenv run -- python app/manage.py runserver
```