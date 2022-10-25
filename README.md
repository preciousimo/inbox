# Inbox System
Custom inbox system that receives and responds to messages.
Through the front end it is possible to send messages and on the back end the option to respond to incoming emails.

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/preciousimo/inbox.git

```

--> Move into the directory where we have the project files : 
```bash
cd inbox

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment :
```bash
envname\scripts\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

--> Migrate Database
```bash
python manage.py migrate

```

--> Create Super User
```bash
python manage.py createsuperuser

```

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#

### App Preview :

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Inbox Home Page
</p>
<img src="https://user-images.githubusercontent.com/47305153/186627557-c4d7d7f4-a5a2-4152-a985-1e6af0a26718.PNG">
</td> 
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Send Inbox
</p>
<img src="https://user-images.githubusercontent.com/47305153/186627576-cb9fb3ca-b5a5-43e3-805e-842a9e2c6615.PNG">
</td> 
</tr>
</table>

<table width="100%"> 
<tr>
<td width="50%">
<br>
<p align="center">
  Login Page
</p>
<img src="https://user-images.githubusercontent.com/47305153/186627573-870119c0-8346-4309-9a01-c0c478dcb394.PNG">  
</td>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Inbox
</p>
<img src="https://user-images.githubusercontent.com/47305153/186627540-1ab1fddb-83dc-40d3-ba3d-dae00d1a25b5.PNG">
</td> 
</tr>
</table>

<table width="100%"> 
<tr>
<td width="100%">      
&nbsp; 
<br>
<p align="center">
  Inbox Reply
</p>
<img src="https://user-images.githubusercontent.com/47305153/186627584-25a01334-be97-4bff-933d-2a42c20cb564.PNG">
</td> 
</table>

## Documentation
You can check up django documentation page for any further information.
[Django Docs](https://docs.djangoproject.com/en/4.0/)
