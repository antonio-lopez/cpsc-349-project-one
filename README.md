# CPSC 349 Project One

### Team Members
 
Team Member | Role | Github
------------ | ------------- | -------------
Antonio Lopez | Back-end | antonio-lopez
Javier Melendrez | Back-end | javimelendrez
Brianna Sharpe | Front-end | briannasharpe
Jose Alvarado | Front-end | Jalvarado115


### Install

Download or clone the repo

Extract folder

Open the folder that is within the extracted folder in VS Code 

Example: `cpsc-349-project-one-antonio\cpsc-349-project-one-antonio`

Dev Container configuration file will be found and will automatically give you the option to "Reopen in Container" 

Docker Desktop - Filesharing notification will pop up -> click the "Share it" option

Open up terminal with Ctrl + `

Verify you have python and pip installed in the container
```
$ python --version
$ pip --version
```

Install project requirements

```
$ pip install -r requirements.txt
```

Run Flask app

```
$ export FLASK_APP=listo.py
$ flask run
```
