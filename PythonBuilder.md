# Python Virtual envaronment builder
### virtualenv

## Linux
```sh
# install virtualenv
> pip install virtualenv 

# create venv 
> virtualenv virtualenv_name

# activate venv
> source virtualenv_name/bin/activate

# deactivate venv
> deactivate

# Create requirements.txt
> pip freeze > requirements.txt
```

## Windows
```sh
# install virtualenv
> pip install virtualenv 

# create venv 
> virtualenv virtualenv_name

# activate venv
> .\env\Scripts\activate
> python env\Scripts\activate.bat

# ectivate error commdna
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

# deactivate venv
> deactivate

# Create requirements.txt
> pip freeze > requirements.txt
```