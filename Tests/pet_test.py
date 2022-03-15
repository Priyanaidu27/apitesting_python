import requests
import json
import pytest
import time

baseUrl = "https://petstore.swagger.io/"
print("pet endpoint tests")


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


def test_Get_pet():
    path = "v2/pet"
    file = open('../Test_data/pet_data.json', "r")
    inputData = json.loads(file.read())
    id = inputData[1]['id']
    response = requests.get(url=baseUrl + path + '/' + str(id))
    responseJson = response.json()
    assert response.status_code == 200
    assert responseJson["name"] == inputData[1]["name"]
    assert responseJson["id"] == inputData[1]["id"]

    print("response.status_code 4", response.status_code)

    id = inputData[1]['id']
    response = requests.delete(url=baseUrl + path + '/' + str(id))
    assert response.status_code == 200
    responseJson = response.json()
    print(responseJson)
    print("response.status_code 5", response.status_code)


test_create_delete_pet()
test_Get_pet()
