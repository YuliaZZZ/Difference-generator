import argparse


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--FORMAT')
args = parser.parse_args()
print(args.first_file)
