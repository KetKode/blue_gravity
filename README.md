# Content-sharing platform (backend)

- **API docs:** http://localhost:8000/api/docs/
- **Django admin panel:** http://localhost:8000/admin/

## Stack:

- Django
- Django REST Framework
- PostgreSQL
- Swagger UI


## Start the project locally using Docker

### clone the project repo

```
git clone https://github.com/KetKode/blue_gravity.git
```

### cd into working directory

```
cd interview_task
```

### add .env like .env.example

```
POSTGRESQL_HOST=11.22.333.44
POSTGRESQL_PORT=5432
POSTGRESQL_USER=db_user
POSTGRESQL_PASSWORD=db_password
POSTGRESQL_DBNAME=db_name

SECRET_KEY=your_secret_key
```

### create network

```
docker network create content-net
```

### run dev build

```
sudo docker compose docker-compose.yml up --build -d
```

### optionally configure db/user/role

*access the db as postgres user*
```
sudo docker compose exec db psql -U postgres
```

```
\c your_database_name
```
*or, if the db doesn't exist*

```
CREATE DATABASE <your_db_name>;
```
*configure the user and their role, priviliges*
```
GRANT ALL PRIVILEGES ON DATABASE <your_db_name> TO <your_db_user_name>;
```
```
GRANT ALL PRIVILEGES ON SCHEMA public TO <your_db_user_name>;
```
```
GRANT USAGE ON SCHEMA public TO <your_db_user_name>;
```
```
GRANT CREATE ON SCHEMA public TO <your_db_user_name>;
```

### run migrations

```
docker exec -it interview_task-backend-1 poetry run python manage.py makemigrations
docker exec -it interview_task-backend-1 poetry run python manage.py migrate
```

### create a super user to access the admin panel

```
docker exec -it interview_task-backend-1 poetry run python manage.py createsuperuser
```

### run tests

```
docker exec -ti interview_task-backend-1 coverage run --source='.' manage.py test
```
