import os
from pathlib import Path


def delete_nums(folder):
    path = Path(folder)
    for file in path.glob("*.mp3"):
        try:
            name = str(file).replace(".mp3", '').split('.')[1].strip()
        except IndexError:
            continue
        else:
            file.rename(folder+os.path.sep+name+".mp3")


delete_nums('music')