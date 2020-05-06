#! /usr/bin/env python3

''' Demonstrate argparse by implementing an interface similar to pip '''

import argparse

parser = argparse.ArgumentParser(
        description="Pip Installs Packages.")
parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="0.1.0")
subparsers = parser.add_subparsers(dest="subparser_name")
install = subparsers.add_parser("install")
install.add_argument(
        "-u",
        "--upgrade",
        action="store_true",
        help="Upgrade package to the newest available version.")
install.add_argument("package_name")
rem = subparsers.add_parser("remove")
rem.add_argument("package_name")


if __name__ == "__main__":
    arguments = parser.parse_args()
    print(arguments)

    if arguments.subparser_name == "install":
        print(f"Installing {arguments.package_name}")
    elif arguments.subparser_name == "remove":
        print(f"Removing {arguments.package_name}")
    else:
        raise ValueError("Unknown subcommand.")
