# -*- coding: ascii -*-
"""
- Use 'python3 setup.py sdist' in a terminal to create the package.  
- Use 'twine upload --repository-url https://upload.pypi.org/legacy/ dist/*' to upload the package on pypi.  
"""
from setuptools import setup, find_packages
from mcwpy import __version__, REQUIRED_PYTHON_VERSION


DEVELOPMENT_STATUS = '3 - Alpha'
CHANGELOG_FILE_NAME = 'CHANGELOG.md'
README_FILE_NAME = 'README.md'
REQUIREMENTS_FILE_NAME = 'REQUIREMENTS.txt'
"""
Development Status :: 1 - Planning
Development Status :: 2 - Pre-Alpha
Development Status :: 3 - Alpha
Development Status :: 4 - Beta
Development Status :: 5 - Production/Stable
Development Status :: 6 - Mature
Development Status :: 7 - Inactive
"""

classifiers = [
    f'Development Status :: {DEVELOPMENT_STATUS}',
    'Intended Audience :: Customer Service',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: End Users/Desktop',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    f'Programming Language :: Python :: {REQUIRED_PYTHON_VERSION.split(".")[0]}',
    f'Programming Language :: Python :: {REQUIRED_PYTHON_VERSION}'
]

setup(
    author='Vianpyro',
    author_email='vianney.veremme@gmail.com',
    classifiers=classifiers,
    description='A new way to create Minecraft datapacks',
    install_requires=open(REQUIREMENTS_FILE_NAME).read(),
    keywords=['Minecraft', 'Datapack', 'Function', 'MCFunction'],
    license='MIT',
    long_description=open(README_FILE_NAME).read() + '\n\n' + open(CHANGELOG_FILE_NAME).read(),
    long_description_content_type='text/markdown',
    name='mcwpy',
    packages=find_packages(exclude=['tests']),
    py_modules=['ansi_escape_sequences', 'datapack', 'workspace'],
    python_requires=f'>={REQUIRED_PYTHON_VERSION}',
    url='https://github.com/vianneyveremme/minecraft_with_python',
    version=__version__,
    zip_safe=False
)
