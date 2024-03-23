Team_1 = 'Волшебники данных'
Team_2 = 'Мастера кода'
team1_num = 6
team2_num = 5
score_1 = 40
score_2 = 42
tasks_total = score_1 + score_2
team1_time = 1552.512
team2_time = 2153.31451
time_avg = (team1_time + team2_time) / tasks_total
if score_1 > score_2:
    challenge_result = Team_1
elif score_1 < score_2:
    challenge_result = Team_2
else:
    challenge_result = 'Ничья'

print('-------------Использование %:-**-----------')
print('В команде %s участников: %s !' % (Team_1, team1_num))
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

print('{:-^43}'.format('Использование format():'))
print('Команда {} решила задач: {}'.format(Team_2, score_2))
print('Команда {} решила задачи за: {} секунд'.format(team1_time, team2_num))

print(f'{'Использование f-строк:':-^43}')
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: победа команды {challenge_result}')
print(f'Сегодня было решенно {tasks_total} задач, в среднем по {time_avg:5.2f} секунды на задачу')