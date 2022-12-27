# FullStack

A project that lets an admin user create questions in question groups to be viewed later by users.


## Setup to run Locally
Requirements : NPM, Python, Internet Connection

Install webpack with `npm install webpack webpack-cli --save-dev`. Then
run `npm run dev` in a terminal and create a virtual enviorment for this project. Then install the dependencies reuqired by requirements.txt. Once all of the following is done activate the virtual enviorment. 

Then run `python manage.py migrate`. It is recommended to create a super user by running `python manage.py createsuperuser` and following the steps indicated.  After this you can start the website by running `python manage.py runserver`. Congratulations you have now set up this webpage locally.