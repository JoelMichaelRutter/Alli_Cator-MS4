# **Alli_Cator Workspace Preparation & Deployment**
When deploying this application, I deployed very early on in the development stages to ensure that I had a solid platform to work on and to ensure that I didn’t run in to any problems towards the project submission. If you wish to use this code as a starting point for your own project, I recommend adopting the same philosophy.

Within this section I will detail the steps that I took towards the initial deployment of the application and the very important steps I took for the final deployment which must be completed when the app is moving out of the production environment and into a live space.
## **Deployment Preparation**
To start the development and deployment process, I installed several packages into the workspace. I will list the packages, their purposes and the commands required to install them below:
1. **Django & Gunicorn** – Installed with “pip3 install django gunicorn”
    * **Django** – This is the framework I used for the project. It is a high-level python framework with lots of pre-installed and pre-coded functionality which is very useful for rapid development. You’ll find more information in the README file within the technologies section.
    * **Gunicorn** – Abbreviated from “Green Unicorn”. This is a Web Services Gateway Interface HTTP server which is commonly used to run Python web applications.
2. **Dj_database_url & psycopg2** – Installed with “pip3 install dj_database_url psycopg2”
    * **Dj_database_url** – This Django library allows us to connect to an external database which in our case will be hosted on Heroku.
    * **Psycopg2** – This package is one of the most popular database adapters for the python programming language which allows us to utilise a PostgreSQL database. It allows us to write database commands in a pythonic fashion and to a higher level of abstraction than raw SQL commands.
3. **Cloudinary** – Installed with “pip3 install dj3-cloudinary-storage”. Cloudinary is a Django package that facilitates integration with the Cloudinary static and media file hosting service via an API. More steps are required to implement this package properly and is covered later in this section.

At this stage, all of the libraries that are required for the application to run have been installed. In terms of meeting user functionality requirements, further libraries were installed as part of the development process which will be covered in this section. Whenever a library or package is installed, we must ensure that we have a requirements.txt file as this is the file that Heroku; our cloud hosting service, can install the relevant dependencies upon deployment.

Any time that you install an external library or package, run the following command to create/update the requirements.txt file
“pip3 freeze –local > requirements.txt”

**IMPORTANT** - If you clone my repository, you will have a copy of my requirements.txt file. To make things easier in terms of installing all of the libraries I used, please enter the following command into the terminal "pip3 install -r requirements.txt". This will install all the dependencies in the requirements.txt file.

## Heroku Setup
1. Go to [Heroku](https://id.heroku.com/login) and signup for an account if you don’t already have one. If you do, sign in so that you can see the Heroku dashboard. 
5. Click the new button in the top right hand section and select “Create New App”
6. Give the application a name and select the region. When selecting a region, select the option that is closest to you. 
7. Click the “Create App” button at the bottom of the form.
8. Once the app is created, select it by clicking the application name.


