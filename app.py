import click

@click.command()
@click.option("--name")
def hello(name):
    click.echo(f'Hello {name}! This is Altamash :)')

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    hello()
