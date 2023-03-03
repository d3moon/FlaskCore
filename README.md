
# Desafio 2 - FlaskCore

Este é um desafio que uma aplicação simples em Python e Flask para cadastrar novos usuários e efetuar o login usando a biblioteca Flask-Security. 

Como base de dados para os usuários está sendo utilizado o MongoDB e a biblioteca Mongo-Engine como ORM. 

## Instalação


**Instalação local:**

```bash
  cd flask-core
  pip install -r requirements.txt
  python app.py
```



 ```Se for rodar local``` **.env**
- SECRET_KEY
- MONGO_DBNAME
- SECURITY_PASSWORD_SALT
- MONGO_URI

#

**Instalação via Docker:**

```bash
  cd flaskcore
  docker-compose build
  docker-compose up
```

**Acesse a porta:***
```bash
  http://localhost:5000
```

## Authors

- [@João Victor F. Braga](https://www.linkedin.com/in/d3moon)

