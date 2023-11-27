# -*- coding: ascii -*-
from dataclasses import dataclass
from PIL import Image
import json
import os
import requests
import shutil
import zipfile


__all__ = [
    'Datapack_Namespaces', 'Font',
    'create_file', 'create_icon_from_string', 'get_latest_minecraft_version', 'get_minecraft_pack_version', 
    'get_mojang_versions_manifest', 'import_from_file', 'make_directory', 'remove_directory'
]

@dataclass
class Datapack_Namespaces:
    ADVANCEMENTS = 'advancements'
    DIMENSION = 'dimension'
    DIMENSION_TYPE = 'dimension_type'
    FUNCTIONS = 'functions'
    LOOT_TABLES = 'loot_tables'
    PREDICATES = 'predicates'
    RECIPES = 'recipes'
    STRUCTURES = 'structures'
    TAGS = 'tags'
    WORLDGEN = 'worldgen'

@dataclass
class Font:
    BOLD = '\033[1m'
    END = '\033[0m'
    ERROR = '\033[91m'
    FINAL_INFO = '\033[94m'
    HEADER = '\033[95m'
    OK_GREEN = '\033[92m'
    UNDERLINE = '\033[4m'
    VARIABLE_INFO = '\033[96m'
    WARN = '\033[93m'


def create_file(name, path: str='', content: object='') -> None:
    """
    Create a file with the given name and content.

    :param name: Name of the file to create.
    :param path: Path to the file to create.
    :param content: Content to write to the file.
    """
    if not os.path.exists(path):
        make_directory(path)

    with open(os.path.join(path, name), 'w+', encoding='utf-8') as f:
        if isinstance(content, str):
            f.write(content)
        elif isinstance(content, list):
            for line in content:
                f.write(f'{line}\n')
        elif isinstance(content, dict):
            f.write(json.dumps(content, indent=4, sort_keys=True))
        else:
            raise TypeError(f'{Font.ERROR}Argument "content" must be of type "str" or "list" not {type(content)}!{Font.END}')

    directory_name = f'{path[len(os.getcwd()) + 1:]}{os.path.sep}{Font.END}{name}{Font.OK_GREEN}'
    print(f'{Font.OK_GREEN}Successfuly created the file "{directory_name}".{Font.END}')

def create_icon_from_string(string: str, path: str) -> None:
    """
    Create an image from a string and saves it to the given path.

    :param string: "Seed" string from which the image will be generated.
    :param path: Path where the image will be saved (must contain the image name and format)
    """
    colors_list = [ord(c) % 255 for c in string]
    cl_len = len(colors_list)
    cl_div = sum([int(v) for v in f'{cl_len:b}'])
    img = Image.new(mode='RGB', size=(64, 64), color=(0, 0, 0))
    img.putdata([(colors_list[(i // cl_div) % cl_len], colors_list[((i // cl_div) + 1) % cl_len], colors_list[((i // cl_div) + 2) % cl_len]) for i in range (64 * 64)])
    img.save(path)

def get_latest_minecraft_version(is_snapshot: bool=False) -> str:
    """Return the latest Minecraft version using Mojang's API."""
    return get_mojang_versions_manifest()['latest']['snapshot' if is_snapshot else 'release']

def get_minecraft_pack_version(minecraft_version: int|str='latest') -> str:
    """
    Get a Minecraft datapack pack version (for the pack.mcmeta) using mojang's API.
    :param minecraft_version: The Minecraft version the user wants to retrieve the datapack pack version information for.
    """
    if isinstance(minecraft_version, int):
        return minecraft_version

    manifest = get_mojang_versions_manifest()

    if minecraft_version in ['latest', 'latest_release', None]:
        minecraft_version = manifest['latest']['release']
    elif minecraft_version == 'latest_snapshot':
        minecraft_version = manifest['latest']['snapshot']

    if any(e['id'] == minecraft_version for e in manifest['versions']):
        for version in manifest['versions']:
            if not version['id'] == minecraft_version:
                continue

            temporary_folder_path = os.path.join(os.getcwd(), 'temporary_folder')
            client_jar_url = dict(requests.get(version['url']).json())['downloads']['client']['url']
            path_to_jar = os.path.join(temporary_folder_path, 'client.jar')
            path_to_version_json = os.path.join(temporary_folder_path, 'version.json')

            if not os.path.exists(temporary_folder_path):
                make_directory(temporary_folder_path)

            with requests.get(client_jar_url, stream=True) as r:
                r.raise_for_status()
                with open(path_to_jar, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

            with zipfile.ZipFile(path_to_jar, 'r') as zf:
                zf.extract('version.json', temporary_folder_path)

            data = import_from_file(path_to_version_json)
            remove_directory(temporary_folder_path)

            if isinstance(data['pack_version'], dict):
                return data['pack_version']['data']

            return data['pack_version']

    raise ValueError(f'Unable to find Minecraft version "{minecraft_version}".')

def get_mojang_versions_manifest() -> dict:
    """Retrieve Mojang's Minecraft versions manifest online."""
    return dict(requests.get('https://piston-meta.mojang.com/mc/game/version_manifest.json', timeout=3).json())

def import_from_file(path: str) -> dict | list:
    """
    Import a file from the given path.

    :param path: Path to the file to import.
    :return: The content of the file.
    """
    with open(path, 'r') as f:
        return json.load(f) if path.endswith('.json') else f.readlines()

def make_directory(path: str=None) -> None:
    """
    Create directories with the given path.

    :param path: Path to create.
    """
    if path is not None:
        os.makedirs(path)
        print(f'{Font.OK_GREEN}Successfuly created the directory "{Font.END}{path}{Font.OK_GREEN}".{Font.END}')

def remove_directory(path: str='') -> None:
    """
    Remove a directory even if it contains files.

    :param path: The path of the file to remove.
    """
    directory_name = path.split(os.path.sep)[-1]
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
            print(f'{Font.FINAL_INFO}Successfuly removed the directory "{Font.END}{directory_name}{Font.FINAL_INFO}".{Font.END}')
        except OSError:
            print(f'{Font.ERROR}Could not remove the directory "{Font.END}{directory_name}{Font.ERROR}".{Font.END}')
    else:
        print(f'{Font.WARN}Directory "{directory_name}".{Font.END}" does not exist!{Font.END}')

def remove_file(path: str='') -> None:
    """
    Remove a file.

    :param path: The path of the file to remove.
    """
    os.remove(path)
