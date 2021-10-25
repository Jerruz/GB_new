from os import scandir
from collections import defaultdict

directory = 'some_data'

stat = defaultdict(lambda : 0)
with scandir(directory) as dir_gen:
    for entry in dir_gen:
        if entry.is_file():
            stat[10 ** len(str(entry.stat().st_size))] += 1

print(dict(stat))
