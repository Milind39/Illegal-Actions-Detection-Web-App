from set_path import *

# Define Label
labels = [{'name': 'Hello', 'id': 1}, {'name': 'iloveu', 'id': 2},{'name': 'no', 'id': 3}, {'name': 'thanks', 'id': 4}, {'name': 'yes', 'id': 5},{'name': 'smoking', 'id': 6}]

# Create label_map.pbtxt
with open(ANNOTATION_PATH + '\label_map.pbtxt', 'w') as f:
    for label in labels:
        f.write("item {\n")
        f.write("name: \"{}\"\n".format(label['name']))  # Use double quotes
        f.write("id: {}\n".format(label['id']))
        f.write("}\n")