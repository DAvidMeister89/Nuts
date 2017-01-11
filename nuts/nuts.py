#!/usr/bin/env python2
import os
import sys
import argparse
import logging
import datetime
from src.application.Logger import Logger

from src.application.ValidationController import ValidationController
from src.application.TestController import TestController


def main(argv):
    logger = Logger()
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Start with a Testfile and a Devicefile", nargs=2)
    parser.add_argument("-v", "--validate", help="Validates Testcase and Device File", nargs=2, )
    parser.add_argument("-vt", "--validatetest", help="Validates Testcase File", nargs=1, )
    parser.add_argument("-vd", "--validatedevice", help="Validates Device File", nargs=1, )

    args = parser.parse_args()
    if args.input:
        tester = TestController(os.getcwd() + "/" + args.input[0], os.getcwd() + "/" + args.input[1])
        tester.logic()
    elif args.validate:
        validator = ValidationController(os.getcwd() + "/" + args.validate[0], os.getcwd() + "/" + args.validate[1])
        validator.logic()
    elif args.validatetest:
        validator = ValidationController(os.getcwd() + "/" + args.validatetest[0], "T")
        validator.logic()
    elif args.validatedevice:
        validator = ValidationController(os.getcwd() + "/" + args.validatedevice[0], "D")
        validator.logic()

if __name__ == "__main__":
        main(sys.argv[1:])