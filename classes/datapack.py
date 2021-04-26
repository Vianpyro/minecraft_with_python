from .workspace import Workspace
from ..utilities.create_file import *
from ..utilities.create_pack_meta import *
from ..utilities.make_directory import *
from shutil import rmtree
from time import time
import os


data_types = ['advancements', 'dimension_type', 'dimension', 'item_modifiers‌', 'loot_tables', 'functions', 'predicates', 'recipes']


class Datapack:
    """
    Datapacks can be placed in the .minecraft/saves/(world)/datapacks folder of a world. Each data pack is either a sub-folder or a .zip file \
        within the datapacks folder. After it is in the folder, a data pack is enabled for that world when the world is reloaded or loaded.

    Data packs load their data based on the load order. This order can be seen and altered by using the /datapack command and is stored in the \
        level.dat file.
    
    The player can also select data packs at the world creation screen by clicking the Data Packs button and dragging-and-dropping their data \
        pack folders/zip-files there. This is similar to the Resource Pack selection screen, and allows the player to enable data packs before \
        the world is generated, and easily customize the load order too.
    """
    def __init__(
        self, title: str='MyAmazingDatapack', path: str=os.getcwd(),
        author:str='MCWPY', pack_meta: dict=None, workspaces: (Workspace, list)=None, 
        auto_compile: bool=False, compile_as_zip: bool=False, auto_replace: bool=False
    ):
        """
        Initialisation of the Datapack.
        Datapacks can be used to override or add new advancements, dimensions, functions, loot tables, predicates, recipes, structures, tags, \
            world generation settings, and biomes without any code modification.

        :param author:          The author of the datapack.
        :param auto_compile:    Should the Datapack be compiled automatically when it is defined?
        :param auto_replace:    Should the Datapack automatically replace a previous version?
        :param compile_as_zip:  Should the Datapack be compiled into a zip file?
        :param pack_meta:       The content of the "pack.mcmeta".
        :param path:            The title where the datapack should be generated.
        :param title:           The title of the datapack.
        :param workspaces:      The content of the Datapack.
        """
        self.author         = author
        self.auto_compile   = auto_compile
        self.auto_replace   = auto_replace
        self.compile_as_zip = compile_as_zip
        self.pack_meta      = pack_meta
        self.path           = '' if path in ['', None] else str(str(path[:-1] + os.path.sep) if path[-1] in [os.path.sep, '/'] else path + os.path.sep)
        self.title          = title
        self.workspaces     = [workspaces] if not isinstance(workspaces, list) else workspaces

        # Test if this Datapack exists already.
        self.exists = os.path.exists(self.path + self.title)

        if self.exists and not self.auto_replace:
            self.auto_replace = input(f'{self.title} already exists, do you want to replace it? [yes/no]: ')[0].lower() == 'y'

        # Test if every element of the workspaces list is a Workspace.
        if not all(isinstance(w, Workspace) or w == None for w in self.workspaces):
            raise TypeError('Workspaces has to be instances of the Workspaces class!')

        if self.auto_compile:
            self.compile()
            
    def generate(self) -> None:
        time_stamp = time()
        print(f'Compiling the Datapack in "{self.path}" as "{self.title}" this might take a few seconds...')
        self.compile()
        print(f'Successfuly generated the datapack in {time() - time_stamp:0.1} seconds :)')

    def compile(self) -> None:
        """
        This method compiles the data entered by the user to create a Minecraft Datapack.

        :return: None or Error
        """
        # Remove the old Datapack.
        if self.exists:
            if self.auto_replace:
                rmtree(self.path + self.title)
                print(f'Successfuly removed the Datapack "{self.title}"')
            else:
                print(f'Failed to remove the Datapack "{self.title}"')

        # Generate the new Datapack.
        if not self.exists or self.auto_replace:
            make_directory(self.title, self.path) # Create the Datapack's folder.

            if all(w == None for w in self.workspaces):
                print('No content was generated!')
            else:
                make_directory('data', f'{self.path}{self.title}/')
                main_function_list = list()
                for workspace in [w for w in self.workspaces if w is not None]:
                    ws = workspace.read()

                    # Create a new directory for this workspace.
                    make_directory(workspace.title, f'{self.path}{self.title}/data/')

                    for key in ws:
                        directory_name = f'{self.path}{self.title}/data/{workspace.title}/{key}/'
                        if key in data_types and ws[key] != None:
                            # Create the key folder.
                            make_directory(key, f'{self.path}{self.title}/data/{workspace.title}/')

                            if key == 'functions':
                                for function_file_name in ws[key]:
                                    create_file(
                                        f'{function_file_name}.mcfunction', directory_name,
                                        ws[key][function_file_name]
                                    )
                            else:
                                print('Be careful, this kind of file is not verified by this program and may contain some errors:', key)
                                for json_file_name in ws[key]:
                                    create_file(
                                        f'{json_file_name}.json', directory_name,
                                        ws[key][json_file_name]
                                    )
                            print(f'Successfuly generated {key} files.')
                        elif key == 'tags':
                            make_directory(directory_name)

                            for e in ws[key]:
                                if e in ['blocks', 'entity_types', 'fluids', 'game_events', 'items']:
                                    make_directory(e, directory_name)
                                    for f in ws[key][e]:
                                        create_file(
                                            f'{f}.json', f'{directory_name}/{e}/',
                                            ws[key][e][f]
                                        )
                        elif ws[key] == None:
                            print(f'No file was generated for "{key}".')
                        else:
                            print(f'Failed to create {key} files: {key} is not supported (yet?).')
                            
                # Create the main(tick) and load files.
                if not os.path.exists(f'{self.path}{self.title}/data/minecraft/'):
                    make_directory('minecraft', f'{self.path}{self.title}/data/')
                if not os.path.exists(f'{self.path}{self.title}/data/minecraft/tags/'):
                    make_directory('tags', f'{self.path}{self.title}/data/minecraft/')
                if not os.path.exists(f'{self.path}{self.title}/data/minecraft/tags/functions/'):
                    make_directory('functions', f'{self.path}{self.title}/data/minecraft/tags/')

                # Create the load and tick files.
                if os.path.exists(f'{self.path}{self.title}/data/{workspace.title}/functions/load.mcfunction'):
                    create_file(
                        'load.json', f'{self.path}{self.title}/data/minecraft/tags/functions/',
                        f'{{"values": ["{workspace.title}:load"]}}'
                    )
                if os.path.exists(f'{self.path}{self.title}/data/{workspace.title}/functions/main.mcfunction'):
                    create_file(
                        'tick.json', f'{self.path}{self.title}/data/minecraft/tags/functions/',
                        f'{{"values": ["{workspace.title}:main"]}}'
                    )

            # Create the "pack.mcmeta" file.
            if self.pack_meta == None:
                print('No "pack.mcmeta" was generated!')
            else:
                create_file(
                    'pack.mcmeta', f'{self.path}{self.title}{os.path.sep}',
                    str(create_pack_meta(
                        self.pack_meta['minecraft_version'],
                        self.pack_meta['description'],
                        self.author
                    ))
                )
