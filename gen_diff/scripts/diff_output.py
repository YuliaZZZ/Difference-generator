import argparse
from gen_diff import engine
from gen_diff.formatters import str_view, text_view, json_view


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument(
      '-f', '--format', choices=['plain', 'json'],
      default=str_view.make_format, help='set format of output')
args = parser.parse_args()
if args.format == 'plain':
    args.format = text_view.make_format
if args.format == 'json':
    args.format = json_view.make_format
print(engine.generate_diff(args.first_file, args.second_file, args.format))
