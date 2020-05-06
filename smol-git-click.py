#! /usr/bin/env python3

''' An example of creating a CLI via click '''

import click

@click.group("smol-git")
@click.version_option("0.1.0")
def cli(*args, **kwargs):
    ''' smol-git - the stupid content tracker '''
    pass

@cli.command()
@click.argument("src")
@click.argument("dest", requred=False)
def clone(src, dest):
    with click.progressbar(files) as _files:
        for file in _files:
            sleep(5)

@cli.command()
@click.argument("key")
@click.argument("value")
def config(key, value):
    app_dir = click.get_app_dir("smol_git")
    if not os.path.exists(app_dir):
        os.makedirs(app_dir)
    cfg = os.path.join(app_dir, "config")
    print(f"config: {cfg}")

@cli.command()
def log():
    click.echo_via_pager(log_string)

@cli.command()
def status():
    for file in files:
        file_status = "new file" if file.added else "modified "
        status_string += click.style(
                f"\t{file_status}: {file.name}\n",
                fg="green",
                bold=True)
        click.echo(status_string)

@cli.command()
@click.option("-m", "--message", help="The commit message.")
def commit(*args, **kwargs):
    if kwargs["message"] is None:
        commit_message = click.edit()
    else:
        commit_message = kwargs["message"]
    print(f"commit: {commit_message}")

@cli.command()
@click.argument("repository")
@click.argument("branch")
def push(repository, branch):
    username = click.prompt("Username for https://github.com: ")
    password = click.prompt(f"Password for https://{username}@github.com: ",
            hide_input=True)
