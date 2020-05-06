#! /usr/bin/env python3

''' Example of a CLI interface using click '''

import click

@click.group("pip")
@click.version_option("0.1.0")
def cli(*args, **kwargs):
    ''' Pip Installs Packages. '''
    pass

@cli.command("install")
@click.option(
        "-u",
        "--upgrade",
        is_flag=True,
        help="Upgrade package to the newest available version.")
@click.argument("package_name")
def install(*args, **kwargs):
    ''' Install packages. '''
    pass

if __name__ == "__main__":
    cli()
