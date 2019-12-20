trainee@tx-12:~$ cd /home/trainee/simar/simarvirenv/
trainee@tx-12:~/simar/simarvirenv$ python3 -m pip install --upgrade pip
Collecting pip
  Using cached https://files.pythonhosted.org/packages/30/db/9e38760b32e3e7f40cce46dd5fb107b8c73840df38f0046d8e6514e675a1/pip-19.2.3-py2.py3-none-any.whl
Installing collected packages: pip
  Found existing installation: pip 19.0.3
    Uninstalling pip-19.0.3:
Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/bin/pip3'
Consider using the `--user` option or check the permissions.

You are using pip version 19.0.3, however version 19.2.3 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
trainee@tx-12:~/simar/simarvirenv$ python3 -m pip install --upgrade pip --user
Collecting pip
  Using cached https://files.pythonhosted.org/packages/30/db/9e38760b32e3e7f40cce46dd5fb107b8c73840df38f0046d8e6514e675a1/pip-19.2.3-py2.py3-none-any.whl
Installing collected packages: pip
Successfully installed pip-19.2.3
You are using pip version 19.0.3, however version 19.2.3 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
trainee@tx-12:~/simar/simarvirenv$ pip3 --version
pip 19.2.3 from /home/trainee/.local/lib/python3.6/site-packages/pip (python 3.6)
trainee@tx-12:~/simar/simarvirenv$ ^C

























trainee@tx-12:~/Demo$ django-admin startproject project
trainee@tx-12:~/Demo$ django-admin startproject pro.
CommandError: 'pro.' is not a valid project name. Please make sure the name is a valid identifier.
trainee@tx-12:~/Demo$ django-admin startapp rest
trainee@tx-12:~/Demo$ python3 manage.py makemigrations
No changes detected
trainee@tx-12:~/Demo$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
trainee@tx-12:~/Demo$ python3 manage.py runserver 0:7000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 17, 2019 - 07:48:39
Django version 2.2, using settings 'project.settings'
Starting development server at http://0:7000/
Quit the server with CONTROL-C.
[17/Sep/2019 07:48:53] "GET / HTTP/1.1" 200 16348
[17/Sep/2019 07:48:53] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[17/Sep/2019 07:48:53] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[17/Sep/2019 07:48:53] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[17/Sep/2019 07:48:53] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
Not Found: /favicon.ico
[17/Sep/2019 07:48:53] "GET /favicon.ico HTTP/1.1" 404 1973
[17/Sep/2019 07:49:04] "GET /admin/ HTTP/1.1" 302 0
[17/Sep/2019 07:49:04] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 1819
[17/Sep/2019 07:49:04] "GET /static/admin/css/login.css HTTP/1.1" 200 1233
[17/Sep/2019 07:49:04] "GET /static/admin/css/base.css HTTP/1.1" 200 16378
[17/Sep/2019 07:49:04] "GET /static/admin/css/responsive.css HTTP/1.1" 200 17944
























trainee@tx-12:~/Demo$ django-admin startproject project.
CommandError: 'project.' is not a valid project name. Please make sure the name is a valid identifier.
trainee@tx-12:~/Demo$ django-admin startproject project .
trainee@tx-12:~/Demo$ python3 manage.py createsuperuser
Username (leave blank to use 'trainee'): admin
Email address: admin@test.com
Password: 
Password (again): 
The password is too similar to the username.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
trainee@tx-12:~/Demo$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 17, 2019 - 07:50:07
Django version 2.2, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[17/Sep/2019 07:50:16] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 1819
[17/Sep/2019 07:50:16] "GET /static/admin/css/login.css HTTP/1.1" 200 1233
[17/Sep/2019 07:50:16] "GET /static/admin/css/base.css HTTP/1.1" 200 16378
[17/Sep/2019 07:50:16] "GET /static/admin/css/responsive.css HTTP/1.1" 200 17944
[17/Sep/2019 07:50:16] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[17/Sep/2019 07:50:16] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[17/Sep/2019 07:50:16] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
Not Found: /favicon.ico
[17/Sep/2019 07:50:16] "GET /favicon.ico HTTP/1.1" 404 1973
[17/Sep/2019 07:50:23] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[17/Sep/2019 07:50:23] "GET /admin/ HTTP/1.1" 200 3042
[17/Sep/2019 07:50:24] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 412
[17/Sep/2019 07:50:24] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
[17/Sep/2019 07:50:24] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
[17/Sep/2019 07:50:24] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[17/Sep/2019 07:51:23] "GET / HTTP/1.1" 200 16348
[17/Sep/2019 07:51:25] "GET /admin/ HTTP/1.1" 200 3042



