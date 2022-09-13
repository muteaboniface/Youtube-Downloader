# Download YouTube videos Implementation using FastAPI
* Download YouTube videos of interest at the commandline.
* deployed app https://youtme.herokuapp.com/
* Download path C:\Users\username\Downloads

Project Structure

-app

  -backend

    --home.py

  -core

    --config.py

  -static

    --style.css

    --favicon.ico

  -templates

    --home.html

  -main.py

## To host in heroku you need the following files
* Procfile -which is required by heroku added the below.

     web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000}

* runtime.txt - Python version on which you app will run on. Have added below

     python-3.9.14 

* requirement.txt - This will have the packages your app will require to run  

## How the Page looks like
![img.png](img.png)