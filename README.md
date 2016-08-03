# Mashiro
A Hot Boilerplate for Django 1.9 on Heroku.

![mashiro](https://cloud.githubusercontent.com/assets/1303549/12137567/3df4ed40-b495-11e5-9b1d-80cfb394fd54.jpg)

---

### How To Use

	$ cd ~/workspace/shiina

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install --upgrade pip
    $ pip install django

    $ django-admin.py startproject --template=https://github.com/theeluwin/mashiro/archive/master.zip --name=Procfile mashiro .
    $ mv mashiro/local.sample.py mashiro/local.py
    $ mv .env.sample .env

    $ pip install -r requirements.txt
    $ fab deploy


### To Deploy on Heroku

    $ fab deploy:heroku

### Further Reading

- [Heroku Django Template](https://github.com/heroku/heroku-django-template)
- [Heroku Python Getting Started](https://github.com/heroku/python-getting-started)
- [Django Rest Framework](http://www.django-rest-framework.org/)
- [Django Rest Swagger](http://django-rest-swagger.readthedocs.io/en/latest/)
- [AngularJS](https://angularjs.org/)
