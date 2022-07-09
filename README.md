# Inbox System
Custom inbox system that receives and responds to messages.
Through the front end it is possible to send messages and on the back end the option to respond to incoming emails.

# Cloning the repository
--> Clone the repository using the command below :

    git clone https://github.com/preciousimo/inbox
--> Move into the directory where we have the project files :

    cd inbox

# Create a virtual environment
--> Install virtualenv first:

    pip install virtualenv
--> Create virtual environment:

    virtualenv envname
--> Activate the virtual environment :

    envname\scripts\activate

# Install the requirements :
    pip install -r requirements.txt

# Migrate Database
    python manage.py migrate

# Create Super User
    python manage.py createsuperuser

# To run the App, use :
    python manage.py runserver
Then, the development server will be started at http://127.0.0.1:8000/
    
⚠ Please note that this setup is for windows

## Documentation
You can check up django documentation page for any further information.
[Django Docs](https://docs.djangoproject.com/en/4.0/)
