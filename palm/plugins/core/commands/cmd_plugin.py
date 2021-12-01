from typing import Optional
from pathlib import Path
import click


@click.group(help="Palm plugin utilities")
def cli():
    pass

@cli.command()
@click.option("--name", multiple=False, required=True, help="Name of the plugin")
@click.pass_context
def new(ctx, name: str):
    """
    Generate a new plugin
    """
    default_target_dir = Path(Path.cwd().parent, name)
    target_dir = click.prompt("Where do you want to create the plugin?", default=default_target_dir)
    if not target_dir.exists():
        click.secho("Target directory does not exist", fg="yellow")
        create_target_dir = click.confirm("Do you want to create the target directory?", default=True)
        if not create_target_dir:
            click.secho("Aborting", fg="red")
            return
        target_dir.mkdir(parents=True)

    template_path = Path(Path(__file__).parents[1], "templates") / 'plugin'
    replacements = {
        'plugin_name': name,
        'plugin_class_name': f"{name.title().replace('_', '')}Plugin",
    }

    ctx.obj.generate(template_path, target_dir, replacements)
    click.secho(f'{name} plugin created in {target_dir}', fg='green')
    


@cli.command()
@click.option("--name", multiple=False, help="Name of the plugin")
@click.pass_context
def versions(ctx, name: Optional[str]):
    """
    Output plugin versions

    If the name option is provided, output the version for just that plugin
    """

    if name:
        try:
            plugins = [ctx.obj.plugin_manager.plugins[name]]
        except KeyError:
            click.secho(f"Plugin {name} not installed in this project", fg='red')
            return
    else:
        plugins = list(ctx.obj.plugin_manager.plugins.values())

    # Do not display core or repo 'plugins' since those are versioned with palm core
    excluded_plugins = ["core", "repo"]
    plugins = [p for p in plugins if p.name not in excluded_plugins]

    if not plugins and not name:
        click.secho("No plugins installed", fg="red")
        return

    for plugin in plugins:
        click.echo(f"{plugin.name}: {plugin.version}")


@cli.command()
@click.option("--name", multiple=False, required=True, help="Name of the plugin")
@click.pass_context
def update(ctx, name: Optional[str]):
    """
    Update a plugin

    If the name option is provided, update the specified plugin
    """
    excluded_plugins = ["core", "repo"]
    if name in excluded_plugins:
        click.secho(f"Plugin {name} is a core plugin and cannot be updated", fg='red')

    try:
        plugin = ctx.obj.plugin_manager.plugins[name]
    except KeyError:
        click.secho(f"Plugin {name} not installed in this project", fg='red')
        return

    click.echo(f"Updating {plugin.name}...")
    success, message = plugin.update()
    if success:
        click.secho(f"Plugin {plugin.name} updated successfully", fg='green')
    else:
        click.secho(f"Plugin {plugin.name} update failed: {message}", fg='red')
