import argparse
from gen_diff import generate_diff


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', type=str, help='set format of output')
args = parser.parse_args()
print(generate_diff.engine(args.first_file, args.second_file))
