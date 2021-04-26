import os


def make_directory(name, path: str='') -> None:
    """
    This functions creates a directory.

    :param name:    The name of the directory to create.
    :param path:    The path where the directory has to be created.
    :return:        None or OS-Error if the directory could not be created.
    """
    try:
        os.mkdir(f'{path}{name}')
    except OSError:
        raise OSError(f'Failed to create the directory "{name}".')
    else:
        print(f'Successfuly created the directory "{name}".')
