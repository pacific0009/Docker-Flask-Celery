## Assignment Scaffolding

***Code Navigation***

This project consists of a main folder `src` which contains all the project files. The files outside the source folder consists of `docker-compose.yml`, `Dockerfile` and a `local.env` file which are used for running the docker containers. The `src` folder contains the entrypoint of the Flask project `app.py`, `settings` folder which contains your application settings and an `apis` folder that stores all your urls and views.

Specify the urls in `urls.py` file in the api folder as list of tuples with following format:

    (endpoint, view_func, methods, description)
example:

    ("/", views.index, ["GET"], "index page")

***Installation***

Running the scaffolding app is very easy. First [install](https://docs.docker.com/install/) docker for your operating system from the docs provided in the docker website. Also [install](https://docs.docker.com/compose/install/) docker-compose

Then run

    sudo docker-compose build
and then

    sudo docker-compose up
This will run the server at port http://localhost:8400/

The index view will be displayed in your browser.

***Flask commands***

Enter into web container bash to execute commands

    sudo docker -it <container id> /bin/ash

To create a new user

    flask createuser -u username -p password

To print login history (last 50 entries)

    flask loginhistory

***Login api***

Send a post request to http://localhost:8400/login 
with json data

    {
        "user_id": "<username>"
        "password": "<password>"
    }

***Task Monitor Flower***

You can monitor tasks at http://localhost:5555/