import argparse
import sys
from MITpeople import get_people

parser = argparse.ArgumentParser(description="Access the MIT People Directory")
parser.add_argument("query", type=str,
    help="The name, kerberos, number, or last name pronunciation to query.")
parser.add_argument("-o", "--options", help="The type of query to run.",
        default="general")
parser.add_argument("-r", "--recurse", help="Follow links to get all data.",
    action="store_true")
                                      
args = parser.parse_args()
print(get_people(args.query, args.options , args.recurse)) # works in v2 or v3
