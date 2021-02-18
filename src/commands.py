import click
import pickle
import uuid

from src.vault import Vault
from src.vault import load_vault
from src.vault import save_vault

from datetime import datetime
from pathlib import Path

@click.group()
def actions():
    pass

@click.command()
@click.argument('name')
@click.argument('keeper')
def generate_vault(name: str, keeper: str):
    new_vault = Vault(
        name=name,
        vault_keeper=keeper,
        started_at=datetime.now(),
        items={}
    )
    file_path = f'./{uuid.uuid4()}.vault'
    save_vault(file_path, new_vault)
    click.secho(f'Vault created at: ', fg='green')
    click.secho(f'{file_path}')

@click.command()
@click.argument('path')
def store_gem(path: str):
    vault_path = Path(path)
    vault = load_vault(vault_path)
    if not vault:
        raise Exception("Vault")

    click.echo('Vault loaded!\n\n', color=True)
    click.echo('Input name of key:')
    key = input()
    click.echo('Input gem value:')
    gem = input()

    if key and gem:
        gem_added = vault.add_gem(key, gem)
        if gem_added:
            save_vault(vault_path, vault)
            click.secho('Gem added', fg='green')
        else:
            click.secho('Gem was not added', fg='red')


@click.command()
@click.argument('path')
@click.argument('gem')
def get_gem(path: str, gem: str):
    vault_path = Path(path)
    if not vault_path.exists() or not vault_path.is_file():
        click.echo("Cannot access this vault path")
    else:
        vault = load_vault(vault_path)
        click.echo(vault.items.get(gem, 'None'))


actions.add_command(generate_vault)
actions.add_command(store_gem)
actions.add_command(get_gem)
