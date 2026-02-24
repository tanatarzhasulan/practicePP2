import json

'''
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"]) # if json is string -> py 
'''

'''
x = {
    "name": "John",
    "age": 30, 
    "city": "New York"
}
y = json.dumps(x)
print(y) # dumps() → dict → JSON string
'''

