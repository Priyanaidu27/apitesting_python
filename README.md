# apitesting_python
Pytest is a mature full-featured Python testing frame that helps you write and run tests in Python.
The requests module allows you to send HTTP requests using Python.
Getting started
To download and install pytest, run this command from the terminal : pip install pytest
To download and install requests, run this command from the terminal : pip install requests
To ensure all dependencies are resolved in a CI environment.

Then run the following command :  pytest .\test_pet_order.py
By default pytest only identifies the file names starting with test_ or ending with _test as the test files.

Pytest requires the test method names to start with test. All other method names will be ignored even if we explicitly ask to run those methods.

A sample test below :
def test_create_delete_pet():
    # read test data
    file = open('../Test_data/pet_data.json', "r")
    inputData = json.loads(file.read())
    # pet endpoint
    path = "v2/pet"
    response = requests.post(url=baseUrl + path, json=inputData[0])
    print(response.text)
    responseJson = response.json()
    json_object = response.json()
    print(json_object)
    assert response.status_code == 200
    assert responseJson["name"] == inputData[0]["name"]
    print("response.status_code 1", response.status_code)

    response = requests.post(url=baseUrl + path, json=inputData[1])
    responseJson = response.json()
    print(response.text)
    assert response.status_code == 200
    print("response.status_code 2", response.status_code)
    assert responseJson["name"] == inputData[1]["name"]

    id = inputData[0]["id"]
    print(id)
    response = requests.get(url=baseUrl + path + '/' + str(id))
    responseJson = response.json()
    print(response.status_code)
    if response.status_code == 200:
        response = requests.delete(url=baseUrl + path + '/' + str(id))
        print(baseUrl + path + '/' + str(id))
        print(response.text)
        print(response.status_code)
        assert response.status_code == 200
        responseJson = response.json()
        print("response.status_code 3", response.status_code)
