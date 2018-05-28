from pathlib import Path

print('''
Задание №3. Задан путь к директории с музыкальными файлами (в названии
             которых нет номеров, а только названия песен) и текстовый файл,
             хранящий полный список песен с номерами и названиями в виде строк
             формата «01. Freefall [6:12]». Напишите скрипт, который корректирует
             имена файлов в директории на основе текста списка песен.
''')


def fix_names(folder, textfile):
    path = Path(folder)
    mask = '*.mp3'
    names = Path(textfile)
    tracks = {}
    with names.open() as f:
        for line in f:
            s = line.split('[')[0]
            tracks[s.split('.')[1].strip()] = s.strip()
    print(tracks)
    for f in path.glob(mask):
        name = f.name.replace(f.suffix, '')
        try:
            f.rename(str(f).replace(name, tracks.get(name)))
        except TypeError:
            continue


fix_names("music", "names.txt")