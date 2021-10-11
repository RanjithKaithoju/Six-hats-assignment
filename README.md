# Six-hats-assignment

1, Create project -  django-admin startproject six_hats_assignment \n
2, create app - user - python manage.py startapp user\n
3, Taking secret key from environment.\n


#Usage
For getting all & creating records - http://localhost:8000/users/

\n

For getting records with pagination - http://localhost:8000/users_pagination/?page=1&per_page=10

\n

To GET/DELETE/UPDATE record - http://localhost:8000/user_detail/{id}/