# hierarchy
[![Python application](https://github.com/mperov/hierarchy/workflows/Python%20application/badge.svg?branch=master)](https://github.com/mperov/hierarchy/actions/workflows/python-app.yml)

Project allows to clone directory hierarchy from server

## Requirements
At first get project:
```console
$ git clone https://github.com/mperov/hierarchy.git
$ cd hierarchy/
```
The second I recommend to create special Python virtual enviroment by
```console
$ sudo apt-get install python3-venv -y
$ python3 -m venv hierarchy
$ source hierarchy/bin/activate
```

Next install some Python modules - `pip3 install -r requirements` or `python3 -m pip install -r requirements`  
If you don't have pip3 then you may install it [how described here](https://pip.pypa.io/en/stable/installation/)

## Usage
```console
usage: hierarchy.py [-h] [-d /path/to/directory] [-rd N] [-s ip address or hostname] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -d /path/to/directory, --dir /path/to/directory
                        path to directory. This argument is main!
  -rd N, --recursion-depth N
                        The maximal number of nested calls. By default recursion is unlimited.
  -v, --verbose         this option enables debug mode
```
