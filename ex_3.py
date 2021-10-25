from shutil import copytree, rmtree
from os import walk, listdir
from os.path import join as join_path, exists

project_name = 'my_project'

if exists(join_path(project_name, 'templates')):
    rmtree(join_path(project_name, 'templates'))

for root, dirs, files in walk(project_name):
    if 'templates' in dirs and root != project_name:
        for entry in listdir(join_path(root, 'templates')):
            copytree(join_path(root, 'templates', entry), join_path(project_name, 'templates', entry))
