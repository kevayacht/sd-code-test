import argparse 
import sys
import fileinput

def read_piped_input():
    return [line.rstrip('\n') for line in fileinput.input()]

def read_file(input_file_path):
    with open(input_file_path) as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

def input_handler(argparser):
    args = argparser.parse_args()
    if args.input_file_path:
        return read_file(args.input_file_path)
    elif not sys.stdin.isatty():
        return read_piped_input()
    else:
        argparser.print_help()
        exit()  

def get_input():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('input_file_path', nargs='?', help='The path to the input data file')
    return input_handler(argparser)