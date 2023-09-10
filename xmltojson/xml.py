

import xmltodict

import pprint

import json

 

with open('person.xml') as fd:

   my_dict = xmltodict.parse(fd.read())

fd.close()

 

pp = json.dumps(my_dict)

print(pp)
