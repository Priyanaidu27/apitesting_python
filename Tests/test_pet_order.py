import requests
import json
import pytest
import time
baseUrl = "https://petstore.swagger.io/"
print("pet order endpoint tests")


def test_create_petorder_get_petorder():
    # read test data
    file = open('../Test_data/pet_order.json', "r")
    inputData = json.loads(file.read())
    # pet endpoint
    path = "v2/store/order"
    response = requests.post(url=baseUrl + path, json=inputData)
    print(response.text)
    responseJson = response.json()
    json_object = response.json()
    print(json_object)
    assert response.status_code == 200
    assert responseJson["id"] == inputData["id"]
    print("response.status_code 1", response.status_code)

    ##Get test data
    id = inputData['id']
    response = requests.get(url=baseUrl + path + '/' + str(id))
    responseJson = response.json()
    print("response.json()",response.json())
    if response.status_code == 200:
        assert response.status_code == 200
        assert responseJson["id"] == inputData["id"]
        assert responseJson["petId"] == inputData["petId"]
        assert responseJson["quantity"] == inputData["quantity"]
        print("response.status_code 2", response.status_code)
  ##Delete Order  
        response = requests.delete(url=baseUrl + path + '/' + str(id))
        print(baseUrl + path + '/' + str(id))
        print(response.text)
        print(response.status_code)
        assert response.status_code == 200
        responseJson = response.json()
        print("response.status_code 3", response.status_code)
    else:
        print("Skipped other assertions as GET was not succssful")

test_create_petorder_get_petorder()


