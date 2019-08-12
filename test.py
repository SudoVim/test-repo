#!/usr/bin/env python3
"""
test script
"""

import sys
import argparse

def helper_fcn():
    print("hello2")

def main(argv):
    """ main function """
    parser = argparse.ArgumentParser(
        description="test script",
    )
    args = parser.parse_args(argv)

    helper_fcn()

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

