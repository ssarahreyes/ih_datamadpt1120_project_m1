import argparse
from p_acquisition import m_acquisition as mac
import pandas as pd

# here i need to clean de data,

def argument_parser():
    """"
    parse arguments to script
    """
    parser = argparse.ArgumentParser(description='Args')
    parser.add_argument("-p", "--path", help="specify the path of the database.", type=str, required=True)

    args = parser.parse_args()

    return args

def main(arugments):

    print('starting process')
    print(arguments.path)

    path = arguments.path
    # api_key = arguments.key

    data = mac.acquire(arguments.path)
    # here i need a variable but i don't know why.

    print('Process done!')

if __name__ == '__main__':
    print('hola')