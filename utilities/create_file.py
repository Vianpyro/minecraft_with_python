def create_file(name, path:str='', content:(str, list, dict)='') -> None:
    '''
    This functions creates a file.

    :param name:    The name of the file to create.
    :param path:    The path where the file has to be created.
    :param content: The content to write in the created file.
    :return:        None or OS-Error if the file could not be created.
    '''
    with open(f'{path}{name}', 'w') as f:
        if isinstance(content, str):
            f.write(content)
        elif isinstance(content, list):
            for line in content:
                f.write(f'{line}\n')
        elif isinstance(content, dict):
            for line in str(content).replace("'", '"').lower():
                f.write(f'{line}')
        else:
            raise TypeError(f'Argument "content" must be of type "str" or "list" not {type(content)}!')
        print(f'Successfuly created the file "{name}".')
