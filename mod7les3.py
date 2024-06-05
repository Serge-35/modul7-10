team1 ='Мастера кода'
team2 ='Волшебники данных'
team1_num = 5
team2_num = 6
print('В команде %s участников: %s!' % (team1, team1_num))
print('В команде %s участников: %s!' % (team2, team2_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
score_1 = 40
score_2 = 42
tasks_total = score_1 + score_2
print('Команда {} решила задач: {}!'.format(team1, score_1))
print('Команда {} решила задач: {}!'.format(team2, score_2))
team1_time = 1552.512
team2_time = 2153.31451
time_avg = (team1_time + team2_time) / tasks_total
print('{} решили задачи за {} с !'.format(team1, team1_time))
print('{} решили задачи за {} с !'.format(team2, team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = (f'Результат битвы: победа команды {team1}!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = (f'Результат битвы: победа команды {team2}!')
else:
    challenge_result = 'Ничья!'
print(challenge_result)
print(f'Сегодня было решенно {tasks_total} задачи, в среднем по {round(time_avg,2)} секунды на задачу!.')


