import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--field_size', '-f', metavar='-f', type=int, help='Size of game field')
args = parser.parse_args()
print('Field size =',args.field_size)