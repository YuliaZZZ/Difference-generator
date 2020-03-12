import argparse
from gen_diff import engine
from gen_diff.formatters import str_view, text_view, json_view


def turn(argument):
    if argument == 'plain':
        return text_view.make_format
    elif argument == 'json':
        return json_view.make_format
    else:
        return str_view.make_format


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument(
      '-f', '--format', choices=['plain', 'json'],
      default=0, help='set format of output')
args = parser.parse_args()
diff = engine.generate_diff(
     args.first_file,
     args.second_file,
     turn(args.format)
     )
print(diff)
