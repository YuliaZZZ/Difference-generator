import argparse
from gen_diff import generate_diff
from gen_diff.formatters import str_dict, plain, to_json


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument(
      '-f', '--format', choices=['plain', 'json'],
      default=str_dict.to_format, help='set format of output')
args = parser.parse_args()
if args.format == 'plain':
    args.format = plain.to_format
if args.format == 'json':
    args.format = to_json.to_format
print(generate_diff.engine(args.first_file, args.second_file, args.format))
