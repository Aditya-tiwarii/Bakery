# Bakery


## MAIN API ENPOINTS
```bash
/admin/
api/product/products-list/
api/account/token/
api/account/token/refresh/
api/account/login/
api/account/logout_user/
api/account/register/

```
## RUN APP

### 1. Create and Activate a virtual environment

```bash
python3 -m venv env
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Make database migrations

```bash
py manage.py makemigrations
```

then

```bash
py manage.py migrate
```

### 4. Run server

```bash
py manage.py runserver
```
