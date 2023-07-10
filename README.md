# SciSoc AIIMS Delhi


A Django & Django Template Language based web-application to serve the online requirements of Scisoc AIIMS Delhi. Allows users to authenticate themselves & register for various events being conducted by the society.
Admins/Secretaries can manage their part of work completely seperated & perform CRUD operations on the content to be shown.

## Installation
This app requires python to run on your server/localhost.

#### 1. Clone the project on your local computer.

```sh
git clone https://github.com/Aayush5sep/Scisoc-AIIMS-Delhi
```

### 2. Install the dependencies and devDependencies.

```sh
pipenv install -r requirements.txt
pipenv shell
```
>Any other virtual environments may also work. 
>The requirements.txt file contains all the packages that need to be installed.

### 3. Generate  a Secret Key & other credentials.

- Create a new secret key for django with a secret key generator, like [Djecrety](https://djecrety.ir/).
- Set this secret key value for `DJANGO_KEY` in .env file.
> Optional: Register on Razorpay to set values of `RAZORPAY_KEY_ID` & `RAZORPAY_KEY_SECRET`.
> `EMAIL_HOST_USER` & `EMAIL_HOST_PASSWORD` may be generated from Gmail API if you want to use SMTP for mails.

### 4. Migrate the project.
Run the following commands in terminal.
```sh
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the project.
Run the following command in terminal to start the server.
```sh
python manage.py runserver
```


> Check out more projects by `Aayush Goyal` at [Aayush5sep][aayush]




[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen)

   [git-repo]: <https://github.com/Aayush5sep/UserAuthAPI>
   [aayush]: <https://github.com/Aayush5sep>
