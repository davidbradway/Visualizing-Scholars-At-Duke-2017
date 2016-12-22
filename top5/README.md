
virtualenv -p /usr/bin/python3.3 venv
source venv/bin/activate
pip install flask
pip install WTForms
pip freeze > requirements.txt
deactivate


