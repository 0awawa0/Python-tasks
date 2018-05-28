print('''
Задание №16. Напишите скрипт, который на основе списка из 16 названий
              футбольных команд случайным образом формирует 4 группы по 4
              команды, а также выводит на консоль календарь всех игр (игры
              должны проходить по средам, раз в 2 недели, начиная с 14 сентября
              текущего года). Даты игр необходимо выводить в формате «14/09/2016,
              22:45». Используйте модули random и itertools.
''')
import random
import itertools
import datetime


teams = {'Физтех', 'Эконом', 'Мат. фак.', 'Хим.фак.',
         'Юр. фак.', 'Учфин.', 'ФИЯ', 'Ист. фак.',
         'Фил. фак.', 'Био. фак.', 'Mеж. фак.', 'Библ.',
         'Фак. доп. обр.', 'Проф. союз.', 'Медиацентр', 'Экон. кибер.'}
groups = {'group_1': set(), 'group_2': set(), 'group_3': set(), 'group_4': set()}
for group in groups.keys():
    groups[group] = set(random.sample(teams, 4))
    teams = set.difference(teams, groups[group])
print(groups)
del(teams)
games = {'group_1': list(itertools.combinations(groups['group_1'], 2)),
         'group_2': list(itertools.combinations(groups['group_2'], 2)),
         'group_3': list(itertools.combinations(groups['group_3'], 2)),
         'group_4': list(itertools.combinations(groups['group_4'], 2))}
game_date = datetime.datetime(2017, 9, 14, 22, 45)
delta = datetime.timedelta(days=14)
for i in range(6):
    for key in games:
        date = '{0:02d}/{1:02d}/{2} {3}:{4}'.format(game_date.day, game_date.month, game_date.year, game_date.hour, game_date.minute)
        print('{0}\tvs\t{1}, {2}'.format(games[key][i][0], games[key][i][1], date))
    game_date = game_date + delta