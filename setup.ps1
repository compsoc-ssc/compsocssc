<#
This powershell script mimics the functionality of the setup.sh in the same folder for Windows users
Open the repository in Explorer, right click this file and click "Run with Powershell"
Some people might want to type "Set-ExecutionPolicy Unrestricted" in PowerShell(Run with administrator) before they run this script.
#>
Write-Output "############################"
Write-Output "Virtual Environment Initiation"
pip3 install virtualenv
virtualenv venv
.\venv\Scripts\activate
Write-Output "############################"
Write-Output "Installing Dependencies"
pip install -r requirements.txt
Write-Output "############################"
Write-Output "Handling Migrations"
New-Item website\settings\local.py -type file
python manage.py makemigrations
python manage.py migrate
Write-Output "############################"
Write-Output "Create Superuser"
python manage.py createsuperuser
Write-Output "############################"
Write-Output "Starting server"
python manage.py runserver
