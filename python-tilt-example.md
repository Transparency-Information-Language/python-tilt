
## Installation
Install the python client library using pip. See the [project page](https://pypi.org/project/tilt/).


```python
!pip3 install tilt
```

    Requirement already satisfied: tilt in /usr/local/lib/python3.8/site-packages (0.0.1)


## Basic usage

1) Import the transparency information language binding/library.
2) Create your first object, e.g. a Data Protection Officer with their contact details.
3) Continue creating your objects, i.e. a Controller and its Representative.
4) ... (add all other fields, not shown in here) ...


```python
from tilt import tilt

dpo = tilt.DataProtectionOfficer(name='Max Ninjaturtle', address='21 Jump Street', country='DE', email='jane@mycompany.com', phone='0142 43333')
print(dpo.to_dict())
# {'address': '21 Jump Street', 'country': 'DE', 'email': 'jane@mycompany.com', 'name': 'Max Ninjaturtle', 'phone': '0142 43333'}


r = tilt.ControllerRepresentative(name='Maxi Müller', email='maxi@mail.com', phone=None)
c = tilt.Controller(name='MyCompany', address='Straße des 17. Juni', country='DE', division='Main', representative=r)
print(c.to_dict())
# {'address': 'Straße des 17. Juni', 'country': 'DE', 'division': 'Main', 'name': 'MyCompany', 'representative': {'email': 'maxi@mail.com', 'name': 'Maxi Müller', 'phone': None}}
```

    {'address': '21 Jump Street', 'country': 'DE', 'email': 'jane@mycompany.com', 'name': 'Max Ninjaturtle', 'phone': '0142 43333'}
    {'address': 'Straße des 17. Juni', 'country': 'DE', 'division': 'Main', 'name': 'MyCompany', 'representative': {'email': 'maxi@mail.com', 'name': 'Maxi Müller', 'phone': None}}


## Import existing documents
In order to import exisiting tilt documents (we call them instances), you can use your favorite HTTP client or load from your local disk. Then you can use the native python objects and do any manipulations as you like.[](http://)


```python
import json
import requests

file = requests.get('https://raw.githubusercontent.com/Transparency-Information-Language/schema/master/tilt.json')
instance = tilt.tilt_from_dict(json.loads(file.content))

print(instance.controller.to_dict())
# {'address': 'Wolfsburger Ring 2, 38440 Berlin', 'country': 'DE', 'division': 'Product line e-mobility', 'name': 'Green Company AG', 'representative': {'email': 'contact@greencompany.de', 'name': 'Jane Super', 'phone': '0049 151 1234 5678'}}

for element in list(instance.data_disclosed):
    for recipient in element.recipients:
        print(recipient.category)
# Marketing content provider
# Responsible Statistical Institutes


instance.controller.name = 'Yellow Company Ltd.'
print(instance.controller.to_dict())
# {'address': 'Wolfsburger Ring 2, 38440 Berlin', 'country': 'DE', 'division': 'Product line e-mobility', 'name': 'Yellow Company Ltd.', 'representative': {'email': 'contact@greencompany.de', 'name': 'Jane Super', 'phone': '0049 151 1234 5678'}}
```

    {'address': 'Wolfsburger Ring 2, 38440 Berlin', 'country': 'DE', 'division': 'Product line e-mobility', 'name': 'Green Company AG', 'representative': {'email': 'contact@greencompany.de', 'name': 'Jane Super', 'phone': '0049 151 1234 5678'}}
    Marketing content provider
    Responsible Statistical Institutes
    {'address': 'Wolfsburger Ring 2, 38440 Berlin', 'country': 'DE', 'division': 'Product line e-mobility', 'name': 'Yellow Company Ltd.', 'representative': {'email': 'contact@greencompany.de', 'name': 'Jane Super', 'phone': '0049 151 1234 5678'}}


## Create new documents from scratch
In the example below we are using standard libraries (e.g. sha256 or datetime) in order to create formatted strings. All objects have `from_dict()` and `to_dict()` functions which help you to build or export them.


```python
from hashlib import sha256
from datetime import datetime

result = {}
result["_hash"] = sha256('<insert hashable content here>'.encode('utf-8')).hexdigest()
result["_id"] = '<your-id-01>'
result["created"] = '2020-10-02T22:08:12.510696'
result["language"] = 'en'
result["modified"] = datetime.now().isoformat()
result["name"] = 'Green Compancy SE'
result["status"] = 'active'
result["url"] = 'https://greencompany.implementation.cloud'
result["version"] = 42

meta = tilt.Meta.from_dict(result)

print(meta)
# <tilt.tilt.Meta object at 0x7fef287928d0>

print(meta.to_dict())
# {'_hash': 'bd8f3c314b73d85175c8ccf15b4b8d26348beca96c9df39ba98fa5dda3f60fcc', '_id': '<your-id-01>', 'created': '2020-10-02T22:08:12.510696', 'language': 'en', 'modified': '2020-07-27T15:14:35.689606', 'name': 'Green Compancy SE', 'status': 'active', 'url': 'https://greencompany.implementation.cloud', 'version': 42}
```

    <tilt.tilt.Meta object at 0x10e7021f0>
    {'_hash': 'bd8f3c314b73d85175c8ccf15b4b8d26348beca96c9df39ba98fa5dda3f60fcc', '_id': '<your-id-01>', 'created': '2020-10-02T22:08:12.510696', 'language': 'en', 'modified': '2020-07-28T22:28:49.794345', 'name': 'Green Compancy SE', 'status': 'active', 'url': 'https://greencompany.implementation.cloud', 'version': 42}


## Validate documents
See the following example code on how to validate documents using [fastjsonschema](https://horejsek.github.io/python-fastjsonschema/).


```python
import fastjsonschema
import json

import requests

# Load schema to validate against
file = requests.get('https://raw.githubusercontent.com/Transparency-Information-Language/schema/master/tilt-schema.json')
schema = json.loads(file.content)

# Load instance/document to validate;
# you may use your own tilt object with .to_dict() here
file = requests.get('https://raw.githubusercontent.com/Transparency-Information-Language/schema/master/tilt.json')
instance = json.loads(file.content)

# Compile schema
validate_func = fastjsonschema.compile(schema)

# Validate instance against schema
validate_func(instance)
## {'meta': {'_id': 'f1424f86-ca0f-4f0c-9438-43cc00509931', 'name': 'Green Company', 'created': '2020-04-03T15:53:05.929588', 'modified': '2020-04-03T15:53:05.929588',...
## => document is valid


# Load another example
file = requests.get('https://raw.githubusercontent.com/Transparency-Information-Language/schema/master/tilt-NOT-valid.json')
instance = json.loads(file.content)

# Validate another example
validate_func(instance)
## JsonSchemaException: data.controller must contain ['name', 'address', 'country', 'representative'] properties
## => document is invalid
```


    ---------------------------------------------------------------------------

    JsonSchemaException                       Traceback (most recent call last)

    <ipython-input-7-ef961cb89b42> in <module>
         27 
         28 # Validate another example
    ---> 29 validate_func(instance)
         30 ## JsonSchemaException: data.controller must contain ['name', 'address', 'country', 'representative'] properties
         31 ## => document is invalid


    <string> in validate_https___github_com_transparency_information_language_schema(data)


    JsonSchemaException: data.controller must contain ['name', 'address', 'country', 'representative'] properties

