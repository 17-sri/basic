# Create two virtual environments, install few packages in the first one. How do yo create a similar environment in the second one


'''
1. pip install virtualenv 
installing virtual environment
2. virtualenv env1
creating virtual environment env1
3. virtualenv env2
creating virtual environment env2
4. .\env1\Scripts\activate.ps1
activating virtual environment env1
5. pip install pandas
instaling pandas in env1
6. pip install pyjokes
installing pyjokes in env1
7. pip freeze > requirements.txt
creating a folder named requirements.txt
8. deactivate
deactivating env1
9. .\env2\Scripts\activate.ps1
activating virtual environment env2
10. pip install -r requirements.txt
install every package in requirement.txt


'''