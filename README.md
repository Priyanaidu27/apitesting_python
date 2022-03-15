# apitesting_python
Pytest is a mature full-featured Python testing frame that helps you write and run tests in Python.
The requests module allows you to send HTTP requests using Python.
Getting started
To download and install pytest, run this command from the terminal : pip install pytest
To download and install requests, run this command from the terminal : pip install requests
To ensure all dependencies are resolved in a CI environment.

Then run the following command :  pytest .\test_pet_order.py
By default pytest only identifies the file names starting with test_ or ending with _test as the test files.

In this we are testing the Pet swagger API. Below are two scenerios we covered:
1)test_create_delete_pet and test_Get_pet 
2)test_create_petorder_get_petorder
