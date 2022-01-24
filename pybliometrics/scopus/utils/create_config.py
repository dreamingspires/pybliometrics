from typing import List, Optional
from pybliometrics.scopus.utils.constants import DEFAULT_PATHS
from pybliometrics.scopus.utils.startup import CONFIG_FILE, config


# Edited from pybliometrics
def create_config(keys: List[str] =[], insttoken: Optional[str] = None):
    """Initiates process to generate configuration file."""
    assert len(keys) >=1
    key = keys[0]
    # Set directories
    if not config.has_section('Directories'):
        config.add_section('Directories')
    
    for api, path in DEFAULT_PATHS.items():
        config.set('Directories', api, str(path))
    # Set authentication
    if not config.has_section('Authentication'):
        config.add_section('Authentication')
    config.set('Authentication', 'APIKey', key)
    if insttoken:
        config.set('Authentication', 'InstToken', insttoken)
    # Write out
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w+") as ouf:
        config.write(ouf)
    return config