# Download YouTube videos Implementation using FastAPI
* Project to download youtube videos of interest.
* Deployed app at: https://youtme.herokuapp.com/
Project Structure
```
app/ .... Top src dir
|-- backend/
|    --home.py
|-core/
|   --config.py
|-static/
|   --style.css
|   --favicon.ico
|-templates/
|   --home.html
|-main.py
|-Procfile
|-requirement.txt
|-runtime.txt
```
## To host in heroku you need the following files
* Procfile which containing the following config

        web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000}

* runtime.txt - Python version on which the app will run on. Have added below

        python-3.9.14 

* requirement.txt - This will have the packages your app will require to run  

## How to run project

## How the Page looks like
![img.png](img.png)