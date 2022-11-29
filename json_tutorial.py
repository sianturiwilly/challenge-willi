# JSON: JavaScript Object Notation

import json 

json_string = '''
    {
        "students": [
            {
                "id": 1,
                "name": "Willi",
                "age": 29,
                "full-time": true
            },
            {
                "id": 2,
                "name": "Joe",
                "age": 33,
                "full-time": false
            }
        ]
    }
'''

data = json.loads(json_string)
# print(data)
print(data['students'][0])
# data['test'] = True

# new_json = json.dumps(data, indent=4, sort_keys=True)
# print(new_json)