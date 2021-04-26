def import_from_file(path, extension='mcfunction') -> (str, None):
    '''
    This functions help with importing files instead of writing them.
    The files has to exist on the user's computer to be imported.

    :param path:        The path where the resource has to be find.
    :param extension:   The extension of the resource [e.g. ".mcfunction", ".json", ".dat"].
    :return:            None or OS-Error if the resource can not be found or read, a string containing the content of the imported file otherwise.
    '''
    try:
        with open(f'{path}.{extension}', 'r') as f:
            r = [line.replace('\n', '') for line in f if line not in ['', ' ', '\n']]
        return r
    except:
        raise ValueError(f'Could not read the file {path}.{extension}')
