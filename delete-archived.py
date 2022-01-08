import sys
import ast
import json

read_file = open(sys.argv[1], 'r')

# Reading from json file
json_object = json.loads(read_file.read())
read_file.close()

archive = json_object['taskArchive']

for i in archive["ids"]:
    del archive["entities"][i]
archive["ids"] = []

with open(sys.argv[1], 'w') as json_file:
  json.dump(json_object, json_file)