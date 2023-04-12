### This is an example of the UI testing framework with Python+Selenium+pytest+docker ready tests for SWAG LABS
------------
#### There are several options to run the tests:
1. Creating 5 containers in the docker: 1 for tests, 1 for selenium hub and 3 for nodes with browsers: edge, firefox, chrome. (**simple and quick - just need docker**)
2.  Running without containers (**slower as you need to install packages manually**)
------------
#### Instructions to run in docker:
Requirements to run in docker: 
1. **docker** latest version https://www.docker.com/

------------
- Copy this project to your folder:

```
git clone https://github.com/jenkinsCodeWorks/UI_test_framework.git
```

- Run selenium-hub and three nodes with chrome/edge/firefox browsers:

```
 docker-compose -f docker-compose_123.yml up -d
```
- Run the tests:

```
docker compose docker-compose-tests.yml up
```
> screenshots will be saved in the /screenshots folder of this project

------------
#### Instructions to start without docker:
Requirements to run without a docker: 
1. Python - latest version https://www.python.org/downloads/
2. At least 1 browser, for example Google Chrome https://www.google.com/intl/ru_ru/chrome/
3. Browser web driver, e.g. for Google Chrome https://chromedriver.chromium.org/home

------------
- Copy this project to a folder:

```
git clone https://github.com/jenkinsCodeWorks/UI_test_framework.git
```
- Go to the directory with the tests and run the command:


```python
For windows:
python pip install --no-cache-dir -r requirements.txt
```
```
For Linux:
python3 pip install --no-cache-dir -r requirements.txt
```


Use the command to run the tests:
```python
For windows:
python -m pytest TestRunner.py
```
```python
For Linux:
python3 -m pytest TestRunner.py
```
> screenshots will be saved in the /screenshots folder of this project

------------

