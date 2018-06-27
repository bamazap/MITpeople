import argparse
from MITpeople import get_people

parser = argparse.ArgumentParser(description="Access the MIT People Directory")

parser.add_argument("query", type=str,
    help="The name, kerberos, number, or last name pronunciation to query.")

options = parser.add_mutually_exclusive_group()
options.add_argument("-g", "--general", action="store_const", dest="options",
    const="general", help="Search by name or kerberos.")
options.add_argument("-p", "--phone", action="store_const", dest="options",
    const="phone", help="Search by ten-digit phone number.")
options.add_argument("-l", "--lastnamesx", action="store_const", dest="options",
    const="lastnamesx", help="Search by last name sounds like.")
parser.set_defaults(options="general")

parser.add_argument("-r", "--recurse", action="store_true",
        help="Follow links to get all data.")

args = parser.parse_args()

key_indexes = {
    "name": 0,
    "email": 1,
    "phone": 2,
    "address": 3,
    "department": 4,
    "title": 5,
    "url": 6,
    "school": 7,
    "year": 8,
}

def get_key_idx(key):
    return key_indexes.get(key, 9)

people = get_people(args.query, args.options, args.recurse)
for person in people:
    keys = person.keys()
    keys.sort(key=get_key_idx)
    for key in keys:
        print(key+": "+person[key]) # works in python 2 or 3:
    print("") # space between results
