from typing import Dict, List, Optional
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass
import pickle

@dataclass
class Vault:
    name: str
    vault_keeper: str
    started_at: datetime
    items: Dict[str, str]

    def __str__(self) -> str:
        return (f'Vault: {self.name} \n'
               f'Keeper: {self.vault_keeper} \n\n'
               f'Items: {[key for key in self.items]}')

    def add_gem(self, key: str, gem: str) -> bool:
        check_gem = self.items.get(key)
        if check_gem:
            return False

        self.items[key]=gem
        return True

def save_vault(vault_path: Path, vault: Vault) -> bool:
    try:
        with open(vault_path, 'wb') as vault_handler:
            pickle.dump(vault, vault_handler)
    except FileNotFoundError:
        return False

def load_vault(vault_path: Path) -> Optional[Vault]:
    try:
        with open(vault_path, 'rb') as vault_handler:
            return pickle.load(vault_handler)
    except FileNotFoundError:
        return None
