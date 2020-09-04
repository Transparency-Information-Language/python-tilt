from tilt import *
import json

with open('../tilt.json') as file:
	instance = json.load(file)
	
result = tilt_from_dict(instance)

print(result.controller.name)

for p in result.data_disclosed[0].recipients:
	print(p.category)


'''
r = ControllerRepresentative(name='Jane Doe', email='jane@MyCompany.de', phone='0151 12345678')
c = TheControllerSchema(name="MyCompany", address="My Street 3, 10587 Berlin", country="DE", division="MyCompany Europe", representative=r)

try:
    test1 = Tilt()
except TypeError:
    raise

try:
	transparency_information = Tilt(controller=c)
except TypeError:
	raise
'''