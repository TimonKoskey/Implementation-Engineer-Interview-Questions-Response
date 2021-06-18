# Implementation Engineer Interview Questions Response

## Section A

**1.The following are examples of integration protocals.**

* <u>Application programming interface (API).</u>

    APIs define an interaction between two software applications by defining requests to be made, how to make them and the data formats. In the demontration at file [api.py](section_A/api.py), **Flask** is used to create a web API that receives a **GET** request and returns a JSON formated data containing a list of colors. Flask is a micro web framework written in python. To learn more check out [flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)

    From the top of the api file:

    1. Flask and jsonify are imported and the app is initialized.

    1. A list of color objects is created

    1. A function called *get_colors* is defined, this function is a web API that listens to a http GET request on route */colors/all* and returns a JSON formated data containing color objects. This method therefore acts as an interface where other applications can make a GET request for colors through the url defined and this method will send back the list of colors.

    To run the script intall flask by running the following command in your terminal.

    ```bash
    pip install Flask
    ```

    Run the script.

    ```bash
    export FLASK_ENV=development

    export FLASK_APP=api.py

    flask run
    ```

    Open your browser and enter your localhost address [localhost](http://127.0.0.1:5000/colors/all).

    The results should look like this:

    ![screenshot](/images/api-demo-screenshot.png?raw=true)

* <u>Webhooks.</u>

    Webhooks are are events emited by an application that other applications can react to them. In the demo at file [webhooks](section_A/webhooks.py) **Flask** is used to create a **POST** web API that takes a request from a Github webhook which sends POST data every time a change is made to a specific repository.

    To set up the webhook:

  * Run flask.

    ```bash
    export FLASK_ENV=development

    export FLASK_APP=webhooks.py

    flask run
    ```

  * Login to your github account, select a repository and go to   settings then select webhooks and add your URL and change content type to json. In this example ngrok is used to provide a like between the localhost server running flask and github otherwise the localhost server can not be accessed externally.

  * Install ngrok

    ```bash
    sudo snap install ngrok
    ```

  * Run ngrok with your local Flask server port number. This allows ngrok to act as a proxy to our localhost server that can be accessed externally.

    ```bash
    ngrok http 5000
    ```

  Your terminal should print data from github like this.
  ![screenshot](/images/webhooks_screenshot.png?raw=true)

  <br>

**3.The following are examples of encryption methods.**

* <u>Caesar Cipher.</u>

  In this encryption technique each letter of a plain text is replaced by another one, a fixed number of positions down the alphabet.

  In the demo at file [ceaser.py](section_a/ceaser.py), the function takes in a text to be ecrypted and a position shift value. The method takes the text and first it encrypts the upper case texts followed by the lower case text and finally any other characters and spaces. The encryption of the text is as follows:

  1. The method declares a local variable *results* to store the final encryption. The variable is initialized as an empty string.

  1. The method loops through every character in the text to be encrypted and stores each character in a local variable *char*.

  1. An if statement is used to check if the character is uppercase or lowercase. If its uppercase the method gets the decimal ASCII value of the character then adds the shift value and 65 is subtracted from the results, a modulus of the result and the total number of alphabets, i.e 26, is calculated and the result is added to 65 then the overral results is converted back to a text character and the result is appended to the results variable. The same happens with lower case text characters only this time 95 is used because of their starting position in the ASCII table.

  1. After all the characters have been encrypted the method returns the results value.

  The results looks like below:

  ![screenshot](/images/ceaser_screenshot.png?raw=true)

* <u>ROT13 Algorithm.</u>

  This is a special type of Ceaser cipher where all characters are shifted by 13 positions to achieve encryption and decryption. In the demo at file [rot13.py](section_A/rot13.py), the function takes in a text to be ecrypted then it uses the results from bytearray's *maketrans()* method talking two encoded string containing the first and the second half of both the upper and lower cases of the alphabet respectively, to perform encryption and decryption as shown below.

  ![screenshot](/images/rot13_screenshot.png?raw=true)

  * <u>Transposition Cipher.</u>

  In this technique the order of a plain text is written as a cipher text.

  The *split()* function in the demo at file [transposition.py](transposition.py) splits the text and the *encode* method creates a cipher using a key that specifies the number of columns.

  The results is as below.

  ![screenshot](/images/transposition_screenshot.png?raw=true)

## Section B

### Qestion 2

In this section I create a simple django application with two pages, one with an input form where a user can enter a name text of what they want to search and another that displays the results. If the user does not type in anything the app displays all data in the database.

![screenshot](/images/name_input_sceenshot.png?raw=true)

![screenshot](/images/results_screenshot.png?raw=true)

To create this application:

* Create a file called requirements.txt
* Add the following in the new file:

![screenshot](/images/requirements_screenshot.png?raw=true)

* In the terninal cd to working directory and run:

```bash
pip install -r requirements.txt
```

* To start a Django project run:

```bash
django-admin startproject django_search
```

* Move in to the project's directory.

* In the project's dir run this to create an application inside your project.

```python
python manage.py startapp search_engine
```

* Include the application in the settings.py and base urls.py files in the projects configuration folder which by default has the same name as the project.

* In the applications models.py file create a model with database contents.

* Add the model to admin.py file to access it from the default admin page.

* Import the model to views.py file together with the render. Here we have two methods, one that renders the search page template, this is the home page of the application, and the other that renders the results template. This two templates have the index template as their base. The index() method in views.py checks if the database has any content, if not it uses a names module to generate random names and saves it in the database.

* The search page renders a form with a single input with the post action url at search_results function. Once the submit button is clicked search results method is called through its url defined at url.py. The method then gets the user input from the request.POST then querys the model. If the input is empty it returns all the db contents then it renders the results page which displays the results in any or a *No results* notification if none.

This application requires the following components to run successfully:

1. Django Application.

1. uWSGI.

1. Nginx.

1. Docker.

Docker runs the django app, nginx and postgres in containders.

To run the application:

* Install docker by following docker [documentation](https://docs.docker.com/get-docker/) online.

* Create a file called Dockerfile at the base of your working directory. The file should contain the image name and env path for executable scripts. Copy requirements.txt to the image, install all dependancies required by the libries declared in the requirements, install all requirements create a working directory and copy the project. Copy the scripts folder then make the scripts executable, create a folder for static files then create a news user, give the user access to the vol folder then make the new user created as the image operator. This is to __avoid root operations__. Finally run command *entrypoint.sh*.

* Create a scripts folder with a file *entrypoint.sh* containing scripts to collect static files and run database migrations then it starts the uwsgi.

```bash
uwsgi --socket :8000 --master --enable-threads --module search.wsgi
```

* We then create a proxy folder for **nginx** with three files.

  1. A **default.conf** file that tells nginx to listen at port 8080 and to serve static files from */vol/static* otherwise pass all other requests to uwsgi with module and port number. It also includes a file with uwsgi params.

  1. This **uwsgi_params** contains wsgi params.

  1. A **Dockerfile** that runs a nginxinc/nginx-unprivileged:1-alpine image that serves static files.

* Finally create a docker-compose.yml file. This file describes Three services.

  1. App service that builds the django Dockerfile. It declares the ports to listen to from inside the container and out. It also sets the ENVIRONMENT variables that is used in the django settings file. Finally this service declares that it depends on the db service.

  1. A db service that runs a postgres image.

  1. A proxy service running the nginx image which serves static files.

To start this app run this at the base working directory:

```docker
docker-compose up --build
```
