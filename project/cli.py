import click

""" Command line placeholder. """

@click.group()
def cli():
    pass

@cli.command(name = 'hello')
def hello_world():
    click.echo('Hello World')

@cli.command(name = 'plot-variance')
def plot_variance():
    click.echo('Plotting variance')
    import scripts.plot_variance
    
@cli.command(name = 'plot-seed')
def plot_seed():
    click.echo('Plotting seed data PCA 2 components.')
    import scripts.plot_seed
