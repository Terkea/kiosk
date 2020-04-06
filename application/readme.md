## requirements
first of all create a new venv and run
```
pip install -r requirements.txt
```

## run flask
```
export FLASK_APP='run.py'
flask run
```

## docker
### to get into the container go with
```
docker exec -it docker-id bash -c "source /home/oracle/.bashrc; sqlplus /nolog"
```

### to reset the password get into the container first and run
```
connect sys as sysdba
Oradoc_db1
alter session set "_ORACLE_SCRIPT"=true;
create user terkea identified by test;
grant all privileges to terkea;
```

### init datbase
```python
from application.database import init_db
init_db()
```

### sqlalchemy
https://flask.palletsprojects.com/en/1.1.x/patterns/sqlalchemy/