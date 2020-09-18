#!/usr/bin/env python3
"""
test script
"""

import sys
import argparse

def main(argv):
    """ main function """
    parser = argparse.ArgumentParser(
        description="test script",
    )
    args = parser.parse_args(argv)

    print("hello")

    return 0
#comment - modified
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
#comment2
