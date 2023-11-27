## [0.1.2] (2022/11/01) - Alpha 3
### Changes
- Added iteration through datapacks workspaces.
- Moved the version variable to the main `__init__.py` file.
- Started using Mojang's API to keep the datapacks pack version up to date.
- Updated the changelog format.
- Updated the `setup.py` file for better flexibility.
- Updated the `verify_setup.py` file to match the format change of the `README.md` file.
- Updated the main `__init__.py` file for better flexibility. 

## [0.1.1] (2022/03/04) - Alpha 2
### Changes
- Added every 1.17 entity in the selector class.
- Improved modules imports.
- Updated Datapack generation.
- Updated directory and files generation.

### Fixes
- Fixed automatic version names.

## [0.1.0] (2021/10/20) - Alpha 1
### Changes
- Updated the `README.md`.

### Fixes
- Fixed Workspaces.

## [0.0.16] (2021/10/18)
### Changes
- Added easy-to-use ray trace function.
- Added scripts to ease Python package update.
- Updated the way Workspaces work.

## [0.0.15] (2021/10/13)
### Changes
- Added importation function.
- Added a default Minecraft functions library to import from.

## [0.0.14] (2021/10/06)
### Changes
- Added `load.json` and `tick.json` generation.

## [0.0.13] (2021/09/25)
### Changes
- Added `pack.mcmeta` generation.

## [0.0.12] (2021/08/08)
### Changes
- Added sub-workspaces.

## [0.0.11] (2021/08/06)
### Changes
- Added a check to verify whether the Minecraft Workspace can be automatically created.
- Added a function to remove directories.
- Added `__format__` representation for Datapack objects.
- Changed code encryption from `utf-8` to `ascii`.
- Changed the way the Datapack folder is ziped.
- Changed replacement of older versions of the Datapack folder.
- Changed the Font class to a dataclass.
- Updated the `.gitignore` file to ignore the generated test files.
- Removed unused import in `datapack.py`.

## [0.0.10] (2021/07/31)
### Changes
- Added `utility.py` to the library for tools that can be useful for other modules.
- Made the Datapack compilation delete the old Datapack folder if authorized.
- Made the library inform the user where the Datapack folder by default is.
- Changed `ansi_escape_sequence.py` into `utility.py`.

## [0.0.9] (2021/07/30)
### Changes
- Added many more tests to `datapack.py`.
- Made Datapacks iterable by going through their Workspaces.
- Updated `CHANGELOG.md` way of displaying additions *(`+`)*, changes *(`*`)* and removals *(`-`)*.
- Updated the way to do the tests.

## [0.0.8] (2021/07/30)
### Fixes
- Fixed library import issues - `datapack.py` was not importing `workspace.py` with relative imports.

## [0.0.7] (2021/07/30)
### Changes
- Added `requests==2.26.0` to `REQUIREMENTS.txt`.
- Added `tests.py` in which unit tests are and will be written.
- Added `workspace.py` to create the class `Workspace` which handles the `Datapack` workspaces.
- Wrote several tests for the `Datapack` class (`datapack.py`).
- Improved the `README.md`.
- Improved the `Datapack`'s `workspaces` default attribute.
- Removed `test.py`.

## [0.0.6] (2021/07/29)
### Changes
- Now printing the library version when imported.

### Fixes
- Fixed previous version failing to import sub-modules imports by using relative imports.

## [0.0.5] (2021/07/29)
### Changes
- Updated `verify_setup.py` to check if the display format is correct.

### Fixes
- Fixed previous version by removing inputs in `setup.py`.

## [0.0.4] (2021/07/29)
### Changes
- Added ANSI escape sequences to the output for prettier messages (`ansi_escape_sequences.py`).
- Added an automatic version code for Datapacks with unspecified versions.
- Added `verify_setup.py` to check if the package can be created.
- Changed warnings to be easier to read.
- Version **0.0.3** did not work so MCWPy will be developed without subfolders.

## [0.0.3] (2021/07/29)
### Notes
- Attempt to use subfolders...
- If creating a Datapack using the MCWPy library works then it is a success.

## [0.0.2] (2021/07/28)
### Changes
- Made the library check if is running on [Python](https://www.python.org/downloads/) **3.9.5** or above.

## [0.0.1] (2021/07/28)
### Fixes
- Fixed (or tried to) `CHANGELOG.md`, `LICENSE` and `README.md` looks on [pypi.org](https://pypi.org/project/mcwpy/).

## [0.0.0] (2021/07/28) - Initial commit
### Changes
- Created a `setup.py` file to setup the library.
- Created two functions to add or substract numbers together.
- Created `mcwpy\__init__.py`.
- Created `REQUIREMENTS.txt`.
- Wrote `LICENSE`.
- Wrote `MANIFEST.md`.
- Wrote `README.md`.

### Notes
- Used `python3 setup.py sdist` in a terminal to create the library's first package.
- Used `twine upload --repository-url https://upload.pypi.org/legacy/ dist/*` to upload the library's first package on pypi.
