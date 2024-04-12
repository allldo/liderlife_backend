## Backend

## TODO:
- [ ] Compress all images, BLYAD
- [ ] Delete unused files? (like `team`, `programms` folders)
- [ ] Replace `liderlife.ru` by environment variable
  
## Commands
Make manual backups:
```shell
python3 manage.py dumpdata > test_dump.json
```

Apply manual backups:
```shell
python3 manage.py loaddata manual_backup/12.04.24_10:30.json
```

Create venv:
```shell
python3 -m venv backend-local
source backend-local/bin/activate
```

Install deps:
```shell
pip3 install -r requirements.txt
```

Create database:
```shell
docker run -d --name backend -e POSTGRES_DB=projectdatabase -e POSTGRES_USER=projectuser -e POSTGRES_PASSWORD=mu8mJWFW -p 5432:5432 -d -v ./dump/dump.sql:/dump/dump.sql postgres
```