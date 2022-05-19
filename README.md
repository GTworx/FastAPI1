# FastAPI Example 1
## Data Set
https://github.com/erkansirin78/datasets/blob/master/retail_db/customers.csv

## Start up virtual machine:
(base) [train@localhost ~]$ cd mlflow 
(base) [train@localhost mlflow]$ docker-compose up -d

Recreating mlflow_s3 ... 
Recreating mlflow_s3     ... done 
Recreating test_server   ... done 
Recreating mlflow_db     ... done 
Recreating mlflow_server ... 
Recreating mlflow_server ... done 
Recreating mc            ... 
Recreating mc            ... done

## Check Docker Processes
(base) [train@localhost mlflow]$ docker-compose ps 
    Name                   Command               State                                            Ports 
------------------------------------------------------------------------------------------------------------------------------------------------ 
gitea           /usr/bin/entrypoint /bin/s ...   Up       0.0.0.0:222->22/tcp,:::222->22/tcp, 0.0.0.0:3000->3000/tcp,:::3000->3000/tcp 
jenkins         /sbin/tini -- /usr/local/b ...   Up       0.0.0.0:50000->50000/tcp,:::50000->50000/tcp, 0.0.0.0:8080->8080/tcp,:::8080->8080/tcp 
mc              /bin/sh -c  /tmp/wait-for- ...   Exit 0 
mlflow_db       docker-entrypoint.sh --aut ...   Up       0.0.0.0:3306->3306/tcp,:::3306->3306/tcp, 33060/tcp 
mlflow_s3       /usr/bin/docker-entrypoint ...   Up       0.0.0.0:9000->9000/tcp,:::9000->9000/tcp, 0.0.0.0:9001->9001/tcp,:::9001->9001/tcp 
mlflow_server   mlflow server --backend-st ...   Up       0.0.0.0:5050->5000/tcp,:::5050->5000/tcp 
prod_server     /usr/sbin/init                   Up       0.0.0.0:2222->22/tcp,:::2222->22/tcp, 0.0.0.0:8000->8000/tcp,:::8000->8000/tcp 
test_server     /usr/sbin/init                   Up       0.0.0.0:2223->22/tcp,:::2223->22/tcp, 0.0.0.0:8001->8001/tcp,:::8001->8001/tcp

## stop unnecessarily services
(base) [train@localhost mlflow]$ docker-compose stop prod test jenkins mlflow minio 
Stopping mlflow_server ... done 
Stopping mlflow_s3     ... done 
Stopping prod_server   ... done 
Stopping test_server   ... done 
Stopping jenkins       ... done

## docker ps
(base) [train@localhost mlflow]$ docker-compose ps 
    Name                   Command                State                                        Ports 
---------------------------------------------------------------------------------------------------------------------------------------- 
gitea           /usr/bin/entrypoint /bin/s ...   Up         0.0.0.0:222->22/tcp,:::222->22/tcp, 0.0.0.0:3000->3000/tcp,:::3000->3000/tcp 
jenkins         /sbin/tini -- /usr/local/b ...   Exit 143 
mc              /bin/sh -c  /tmp/wait-for- ...   Exit 0 
mlflow_db       docker-entrypoint.sh --aut ...   Up         0.0.0.0:3306->3306/tcp,:::3306->3306/tcp, 33060/tcp 
mlflow_s3       /usr/bin/docker-entrypoint ...   Exit 0 
mlflow_server   mlflow server --backend-st ...   Exit 137 
prod_server     /usr/sbin/init                   Exit 137 
test_server     /usr/sbin/init                   Exit 137

## Conda Activate
cd ~/mfo/fastapi
conda activate fastapi
(fastapi) [train@localhost fastapi]$

## git  pull origin master (pull the latest changes if there is any)
(base) [train@localhost fastapi]$ git pull origin master 
remote: Enumerating objects: 5, done. 
remote: Counting objects: 100% (5/5), done. 
remote: Compressing objects: 100% (3/3), done. 
remote: Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 
Unpacking objects: 100% (3/3), done. 
From http://localhost:3000/jenkins/fastapi 
 * branch            master     -> FETCH_HEAD 
Updating a33f285..11c105a 
Fast-forward 
 main2.py | 21 +++++++++++++++++++-- 
 1 file changed, 19 insertions(+), 2 deletions(-)

 # Start Databases
 ## start mysql
 MYSQL is already started with the docker
mysql> show databases 
    -> ; 
+--------------------+ 
| Database           | 
+--------------------+ 
| fastapi            | 
| information_schema | 
+--------------------+ 
2 rows in set (0.03 sec) 
mysql> show databases; 
+--------------------+ 
| Database           | 
+--------------------+ 
| fastapi            | 
| information_schema | 
+--------------------+ 
2 rows in set (0.00 sec) 
mysql> use fastapi; 
Reading table information for completion of table and column names 
You can turn off this feature to get a quicker startup with -A 
Database changed 
mysql> show tables; 
+-------------------+ 
| Tables_in_fastapi | 
+-------------------+ 
| customers         | 
| customers_raw     | 
+-------------------+ 
2 rows in set (0.00 sec) 

 ### Check Customer Table
 mysql> select customerId, customerFName, customerLName from customers; 
+------------+---------------+---------------+ 
| customerId | customerFName | customerLName | 
+------------+---------------+---------------+ 
|          1 | Richard       | Hernandez     | 
|          2 | Mary          | Barrett       | 
|          3 | Ann           | Smith         | 
|          4 | Mary          | Jones         | 
|          5 | Robert        | Hudson        | 
|          6 | Mary          | Smith         | 
|          7 | Melissa       | Wilcox        | 
|          8 | Megan         | Smith         | 
|          9 | Mary          | Perez         | 
|         10 | Melissa       | Smith         | 
|         11 | Mary          | Huffman       | 
|         12 | Christopher   | Smith         | 
|         13 | Mary          | Baldwin       | 
|         14 | Katherine     | Smith         | 
|         15 | Jane          | Luna          | 
|         16 | Tiffany       | Smith         | 
|         17 | Mary          | Robinson      | 
|         18 | Robert        | Smith         | 
|         19 | Stephanie     | Mitchell      | 
|         20 | Mary          | Ellis         | 
+------------+---------------+---------------+ 
20 rows in set (0.00 sec)

## start postgresql
(base) [train@localhost fastapi]$ docker run --rm -d \ 
> --name postgresql \ 
> -e POSTGRES_USER=postgres \ 
> -e POSTGRES_PASSWORD=Ankara06 \ 
> -e PGDATA=/var/lib/postgresql/data/pgdata \ 
> -p 5433:5432 \ 
> -v postgresql13_v:/var/lib/postgresql/data \ 
> postgres:13 
66c001ed2f024bd1a7989bbcc3ddfb2b836e56a65fe238480a33710efffa4be1 

### Connect to postgre
(base) [train@localhost fastapi]$ docker exec -it postgresql psql -U postgres 
psql (13.6 (Debian 13.6-1.pgdg110+1)) 
Type "help" for help. 

### list databases
postgres=# \l 
                                 List of databases 
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges 
-----------+----------+----------+------------+------------+----------------------- 
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          + 
           |          |          |            |            | postgres=CTc/postgres 
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          + 
           |          |          |            |            | postgres=CTc/postgres 
 traindb   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =Tc/postgres         + 
           |          |          |            |            | postgres=CTc/postgres+ 
           |          |          |            |            | train=CTc/postgres 
(4 rows)

### connect to traindb
postgres=# \c traindb 
You are now connected to database "traindb" as user "postgres". 
traindb=# \dt 
         List of relations 
 Schema |   Name    | Type  | Owner 
--------+-----------+-------+------- 
 public | customers | table | train 
(1 row)

### select from customers
traindb=# select * from customers; 
 CustomerID | Gender | Age | AnnualIncome | SpendingScore 
------------+--------+-----+--------------+--------------- 
          1 | Male   |  19 |        15000 |            39 
          2 | Male   |  21 |        15000 |            81 
(2 rows) 
traindb=#

## start apps
### start app1 (postgre)
(fastapi) [train@localhost fastapi]$ uvicorn main:app --port 8002 --host 0.0.0.0 --reload

INFO:     Will watch for changes in these directories: ['/home/train/mfo/fastapi'] 
INFO:     Uvicorn running on http://0.0.0.0:8002 (Press CTRL+C to quit) 
INFO:     Started reloader process [3826] using watchgod 
postgresql://train:Ankara06@localhost:5433/traindb 
INFO:     Started server process [3828] 
INFO:     Waiting for application startup. 
INFO:     Application startup complete. 
INFO:     10.0.2.2:61575 - "GET /docs HTTP/1.1" 200 OK 
INFO:     10.0.2.2:61575 - "GET /openapi.json HTTP/1.1" 200 OK 
INFO:     10.0.2.2:61576 - "GET /docs HTTP/1.1" 200 OK 
INFO:     10.0.2.2:61576 - "GET /openapi.json HTTP/1.1" 200 OK

### start app2 (mysql)
(fastapi) [train@localhost fastapi]$ uvicorn main2:app --port 8003 --host 0.0.0.0 --reload

INFO:     Will watch for changes in these directories: ['/home/train/mfo/fastapi'] 
INFO:     Uvicorn running on http://0.0.0.0:8003 (Press CTRL+C to quit) 
INFO:     Started reloader process [3840] using watchgod 
mysql+pymysql://fastapi:Ankara06@localhost/fastapi 
INFO:     Started server process [3842] 
INFO:     Waiting for application startup. 
INFO:     Application startup complete.