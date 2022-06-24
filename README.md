## Entrada

### 24/06/2022

## Author

[Winston Musasia]

# Description

This as a web application where a user can be able to view interesting topics for educational purposes according to their interests.





## Live link


## User Story
The user should be able to:

* Sign in with the application to start using.
* Set up a profile.
* Find posts that have been created by me.
* Create Posts of own interest or expertise.




* 
## Setup and Installation

##### Clone the repository
```bash
git@github.com/BM-Winston/Entrada.git
```
##### Install requirements 
```bash
cd Entrada pip install -r requirements.txt
```
### Install and activate virtual environment
```bash
python3 -m venv virtual - source virtual/bin/activate
```
 ##### Database  
  SetUp your database. Add user and password, host then make migrations. 
 ```bash 
python manage.py makemigrations entrada
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```

##### Run the application  
 ```bash 
 python manage.py runserver 
``` 

##### Tests 
 ```bash 
 python manage.py test 
```

Open application at '127.0.0.1.8000' at your web browser



## Technologies Used

* Python
* Django
* Heroku
* HTML
* CSS

# Known Bugs

* No known bugs


## License


Authors Information

[musasiawinston@gmail.com]

Winston Musasia (c) 2022


[Go Back to the top](#Entrada)


