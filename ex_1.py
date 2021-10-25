from os import mkdir
import os.path as path

dir_structure = {
    'my_project': {
        'settings': {},
        'mainapp': {},
        'adminapp': {},
        'authapp': {},
    }
}


def check_structure(dir_structure: dict) -> (bool, dict):
    result = True
    crossed = []

    for directory in dir_structure.keys():
        if path.exists(directory):
            if result:
                result = False
            crossed.append(directory)

    return result, crossed


def create_project(dir_structure: dict, joined=''):
    for directory in dir_structure.keys():
        if directory != '__files__':
            mkdir(path.join(joined, directory))
            create_project(dir_structure[directory], path.join(joined, directory))
        else:
            for name in dir_structure['__files__']:
                open(path.join(joined, name), 'w').close()


if __name__ == '__main__':
    valid, problems = check_structure(dir_structure)
    if valid:
        create_project(dir_structure)
        print('Структура проекта создана!')
    else:
        print('Структура проекта не создана.\n\tПроблемные файлы:')
        for f in problems:
            print(f'\t\t{f}')
