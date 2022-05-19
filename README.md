# FastAPI1
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

