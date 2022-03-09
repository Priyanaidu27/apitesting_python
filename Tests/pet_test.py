import requests
import json
import jsonpath
import pytest

baseUrl = "https://petstore.swagger.io/"
print("pet endpoint tests")

def test_create_delete_pet() :
    file = open('../Test_data/pet_data.json',"r")
    path = "v2/pet/"
    inputData = json.loads(file.read())
    response = requests.post(url=baseUrl+path,json=inputData[0])
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson,'$.name') == inputData[0]["name"]
    print("response.status_code 1",response.status_code)
    response = requests.post(url=baseUrl+path,json=inputData[1])
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    print("response.status_code 2",response.status_code)
    assert jsonpath.jsonpath(responseJson,'$.name') == inputData[0]["name"]
    id = jsonpath.jsonpath(responseJson,'$.id')
    response = requests.delete(url=baseUrl+path+'/'+str(id))
    assert response.status_code == 200
    print("response.status_code 3",response.status_code)


def test_fetch_pet() :
    path = "v2/pet/"
    file = open('../Test_data/pet_data.json',"r")
    inputData = json.loads(file.read())
    id=inputData[0]['id']
    response = requests.get(url=baseUrl+path+'/'+str(id))
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    print("response.status_code 4",response.status_code)

    assert jsonpath.jsonpath(responseJson,'$.name')== inputData[0]['name']
    assert jsonpath.jsonpath(responseJson,'$.id') == inputData[0]['id']
    id=inputData[0]['id']
    response = requests.delete(url=baseUrl+path+'/'+str(id))
    assert response.status_code == 200
    print("response.status_code 5",response.status_code)
