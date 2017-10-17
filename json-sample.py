import json

data = ''' {
    "name" : "arvind",
    "person" : {
        "age":2,
        "address" :"asdasdasdasd"
    }
}
'''


parsedData = json.loads(data)

print(parsedData["person"]["address"])