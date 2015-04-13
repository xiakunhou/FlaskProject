# FlaskProject
run from heroku
------
create Heroku db

    $ heroku addons:add heroku-postgresql:dev
    $ heroku pg:promote HEROKU_POSTGRESQL_ORANGE_URL
Then it will create a $DATABASE_URL variable, add it to config.py. Prepare requirements.txt and Procfile and commit to heroku.
Then create the db.

    $ heroku run init
    
run from console
-------

    foreman start web


-----
read below documents.

[ref](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-the-heroku-cloud)
[ref](https://devcenter.heroku.com/articles/getting-started-with-python-o#start-flask-app-inside-a-virtualenv)
