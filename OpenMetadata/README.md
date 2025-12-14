# ref
https://docs.open-metadata.org/latest/quick-start/local-docker-deployment

# build and run
```
docker compose up -d
```

wait a few minutes, about 5 minutes.


# down
```
docker compose down
```

# How to use
```
http://localhost:8585
```
Email: admin@open-metadata.org
Password: admin

# Creating JWT
Settings -> Bots -> Add Bot
Email: sample@open-metadata.org
Display Name: sample
Token Expiration: 1h


Select Bots, Add Role, Ex, Admin.
Select Bots, Copy JWT.

# Creating Virtual Environment
```
$ python3.10 -m venv env
```

## Activate Virtual Environment
```
$ source env/bin/activate
(env) $ pip install --upgrade pip setuptools
(env) $ pip install -r requirements.txt
```

## Deactivate Virtual Environment
```
(env) $ deactivate
```

# Run Sample
```
python sample.py
```