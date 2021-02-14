# Google Contacts Organizer

This is the API part of a project. check the front-end in Vue.js [here](https://github.com/Andre-Sacilotti/Google-Contact-Organizer-Front "here").

It stills in development.

## Api Documentation

You can check the swagger documentation here(WIP) 

## How to use

#### To run the development server:

```bash
pip install -r requirements.txt
python testserver.py
```

And to check the api documentation locally,  access:
```bash
localhost:5000/
```
It will returns an Swagger UI

#### Run development server on docker container

```
docker image build -t "conecta_api".

docker container run -v /path/to/firebase/serviceaccount:/auth/ -p 5000:5000 --name api conecta_api python testserver.py
```


#### To run on production

WIP
