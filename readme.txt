#######       Author : Raheel Khan   #######
open terminal
select current directory as api
create virtual environment using command " python3 -m venv env "
activate virtual environment by command "source env/bin/activate"
the run following commands below
pip install --upgrade pip
pip install -r requirements.txt                                    ## install required packages
python manage.py makemigrations                                   ## create migrations for
python manage.py migrate                                          ## run first migration

python3 manage.py loaddata superuser_data.json
python3 manage.py loaddata font_data.json


python manage.py runserver                                       ## run the server

Run device and staff view query on database if needed(Consult with the developer).

NOTE: Perform the following task when deploying from the scratch.
create "public" folder inside the project folder.
