# -*- coding: utf-8 -*-

#
# Copyright (c) 2023 Maksim Perov <coder@frtk.ru>
#

import sys
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO

FILE_PLAYBOOK = "playbook.yml"

class CustomYAML(YAML):
    def dump(self, data, stream=None, **kw):
        inefficient = False
        if stream is None:
            inefficient = True
            stream = StringIO()
        YAML.dump(self, data, stream, **kw)
        if inefficient:
            return stream.getvalue()

def getHierarchyPlayBook(pathInfo):
    content = [
                {
                    'name'      : 'Create directory with necessary permissions.',
                    'hosts'     : 'all',
                    'become'    : 'yes',
                }
              ]
    tasks = []
    for path in pathInfo:
        task = {
                'name' : 'create ' + path,
                'ansible.builtin.file' : {
                            'path'          : path,
                            'owner'         : pathInfo[path]["uid"],
                            'group'         : pathInfo[path]["gid"],
                            'mode'          : pathInfo[path]["mask"],
                            'state'         : 'directory',
                         }
               }
        tasks.append(task)
    content[0].update({ 'tasks' : tasks })
    yaml = CustomYAML()
    yaml.explicit_start = True # --- at the beginning of yaml
    return yaml.dump(content)

def getPingPlayBook():
    content = [ # using list allows to prepend '-' (dash symbol)
                {
                    'name'  : 'Ping pong',
                    'hosts' : 'all',
                    'tasks' :
                    [ # using list allows to prepend '-' (dash symbol)
                        {
                            'name' : 'Ping',
                            'ping' : None,
                        }
                    ],
                }
              ]
    yaml = CustomYAML()
    yaml.explicit_start = True # --- at the beginning of yaml
    return yaml.dump(content)

def writePlayBook(playbook = getPingPlayBook()):
    try:
        with open(FILE_PLAYBOOK , "w") as f:
            f.write(playbook)
    except Exception as e:
        print("ERROR: " + FILE_PLAYBOOK + " isn't writable!")
        print(str(e))
        sys.exit(-1)
    print('YAML is successfully generating to ' + FILE_PLAYBOOK)
    print('This file should be in your current directory!')
