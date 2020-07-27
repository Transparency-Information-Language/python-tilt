# python-tilt | Transparency Information Language and Toolkit

## What is the Transparency Information Language and Toolkit?
With this proposed schema for transparency information with regards to data privacy, an essential step towards a sophisticated ecosystem shall be made by introducing a transparency enhancing toolkit based on a formal language model describing transparency information in the context of multi-service environments and latest legal requirements (EU General Data Protection Regulation). The desired results of the work should be suitable as ready-to-use privacy engineering solutions for developers and serve as a starting point for further research in this area. Eventually, data subjects should (be able to) understand what happens to data relating to them by using the interfaces of the toolkit.

## What is python-tilt?
*tilt* is a Python based language binding for the _Transparency Information Language and Toolkit_.

## Installation
Install the python client library using pip. See the [project page](https://pypi.org/project/tilt/).


```console
foo@bar:~$ pip3 install tilt
Collecting tilt
  Using cached tilt-0.0.1-py3-none-any.whl (22 kB)
Installing collected packages: tilt
Successfully installed tilt-0.0.1
```

## Basic usage

```info
See here for an [interactive playground]().
```

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



## Author
Elias Grünewald

## License
GNU General Public License, Version 3
