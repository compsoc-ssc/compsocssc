printf "######### STARTING SETUP #########\n"
printf "#################################\n"
printf "\nCreating and activating a virtual environment\n"
printf "#################################\n"
virtualenv -p python3 django
source ./django/bin/activate
printf "\nInstalling dependencies\n"
printf "#################################\n"
pip3 install -r requirements.txt
printf "\nSetting up the database\n"
printf "#################################\n"
touch website/settings/local.py
python manage.py makemigrations && python manage.py migrate
printf "\nCreate a superuser -\n"
python manage.py createsuperuser
printf "#################################"
printf "\nSetup complete :)"
printf "\nStarting a development server...\n"
python manage.py runserver

