# Organise Us

## Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Download Git.
```
https://git-scm.com/download/
```

Download Python3.
```
https://www.python.org/downloads/
```
Download PyCharm (recommended).
```
https://www.jetbrains.com/pycharm/download/
```

### Installing
1. Clone the project from Github.
```
git clone https://github.com/robnixon/organise-us.git
```

2. Open the organise-us project in PyCharm.

3. Now we will setup a Python environment to separate your main python installation with the project files. All commands from now to be entered in PyCharm terminal.
```
python -m pip install --upgrade pip
pip install virtualenv
cd C:\Users\[YOURNAME]\Documents
virtualenv -p python env
cd env/scripts
activate
```

4. Set project interpreter in PyCharm settings to env\Scripts\python.exe

5. Download Django into your environment.
```
pip install django
```

6. Navigate to the mysite directory.
```
cd ..\organise-us\mysite
```

7. Start the local server.
```
python manage.py runserver
```

8. In a web browser, go to http://127.0.0.1:8000/polls

