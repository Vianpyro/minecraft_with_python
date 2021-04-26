def create_pack_meta(minecraft_version: str = '1.6.1', description: str = None, author: str = None) -> str:
    '''
    This function helps with creating the string of a "pack.mcmeta" file ready to be written.
    
    :param minecraft_version:   The version of Minecraft in which the user's server runs.
    :param description:         A short description of the uses of the Datapack the user wants to make.
    :param author:              The user's name to write into the "pack.mcmeta".
    :return:                    String of a "pack.mcmeta" file.
    '''
    default_pack_format = 7
    minecraft_version_to_pack_format = {
        '1.6.1': 1, '1.6.2': 1, '1.6.4': 1,
        '1.7.2': 1, '1.7.4': 1, '1.7.5': 1, '1.7.6': 1, '1.7.7': 1, '1.7.8': 1, '1.7.9': 1, '1.7.10': 1,
        '1.8': 1, '1.8.1': 1, '1.8.2': 1, '1.8.3': 1, '1.8.4': 1, '1.8.5': 1, '1.8.6': 1, '1.8.7': 1, '1.8.8': 1, '1.8.9': 1,
        '1.9': 2, '1.9.1': 2, '1.9.2': 2, '1.9.3': 2, '1.9.4': 2,
        '1.10': 2, '1.10.1': 2, '1.10.2': 2,
        '1.11': 3, '1.11.1': 3, '1.11.2': 3,
        '1.12': 3, '1.12.1': 3, '1.12.2': 3,
        '1.13': 4, '1.13.1': 4, '1.13.2': 4,
        '1.14': 4, '1.14.1': 4, '1.14.2': 4, '1.14.3': 4, '1.14.4': 4,
        '1.15': 5, '1.15.1': 5, '1.15.2': 5,
        '1.16': 5, '1.16.1': 5,
        '1.16.2': 6, '1.16.3': 6, '1.16.4': 6, '1.16.5': 6,
        '1.17': 7, '1.17+': 7
    }

    if minecraft_version in minecraft_version_to_pack_format:
        pack_format = minecraft_version_to_pack_format[minecraft_version]
    else:
        raise Warning(
            f'This version of Minecraft seems to have no pack format defined:\nSet to {default_pack_format} by default.')

    description = description
    author = author

    return str(
        {
            "pack": {
                "author": author,
                "description": description,
                "pack_format": pack_format
            }
        }
    ).replace("'", '"')
