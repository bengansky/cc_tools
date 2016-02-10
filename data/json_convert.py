import json
import cc_data
import sys


for json_cc_level in json_cc_level_data:
    title = (json_cc_level["title"])
    year = (json_cc_level["year"])

    real_data = None
     if field_type == "1":

print (sys.argv)
input_file = sys.argv[1]
output_file = sys.argv[2]

json_reader = open(input_file, "r")
json_data = json.load(json_reader)
json_reader.close()
