import warnings


data_types = ['advancements', 'dimension_type', 'dimension', 'item_modifiers‌', 'loot_tables', 'functions', 'predicates', 'recipes']


class Workspace():
    """
    A Workspace is where the content of the Datapack will be written.
    A Datapack may countain several Workspaces.
    """
    def __init__(self, title: str='mcwpy', content: dict=None):
        """
        Initialisation of the Workspace.

        :param content:     The content of this Workspace.
        :param title:       The title of this Workspace.
        """
        self.title      = title.replace(' ', '_').lower() if title is not None and len(title) > 1 else 'mcwpy'
        self.content    = dict() if content == None else content

        if not self.title == title:
            warnings.warn('Workspace titles has to be strings without capital letters.', SyntaxWarning)

    def add(self, file_name: str=None, file_format: str=None, content: (list, str)=None) -> None:
        name = file_name if file_name != None else f'function{len(self.content)}'
        data = str(file_format if file_format[-1] == 's' else f'{file_format}s') if file_format != None else 'functions'
        cntt = content if content != None and isinstance(content, list) else [content]
        
        if not data in self.content:
            self.content[data] = dict()
        
        if name in self.content[data]:
            for line in [e for e in cntt if e != None]:
                self.content[data][name].append(line)
        else:
            self.content[data][name] = cntt

    def read(self) -> dict:
        return self.content
