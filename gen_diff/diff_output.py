import argparse  # pragma: no cover
from gen_diff import engine  # pragma: no cover
from gen_diff.formatters import (str_view,
                                 text_view, json_view)  # pragma: no cover


def turn(argument):   # pragma: no cover
    if argument == 'plain':
        return text_view.make_format
    elif argument == 'json':
        return json_view.make_format
    else:
        return str_view.make_format


parser = argparse.ArgumentParser(
    description='Generate diff')  # pragma: no cover
parser.add_argument('first_file', type=str)  # pragma: no cover
parser.add_argument('second_file', type=str)  # pragma: no cover
parser.add_argument(
      '-f', '--format', choices=['plain', 'json'],
      default=0, help='set format of output')  # pragma: no cover
args = parser.parse_args()  # pragma: no cover
diff = engine.generate_diff(
     args.first_file,
     args.second_file,
     turn(args.format)
     )  # pragma: no cover
