import datetime as dt

FIRST_DAY = dt.date(2023,2,6) # Дата первого понедельника в учебном году, от которого будет рассчитываться расписание

# Функции вернут индекс дня в массиве из расписания (день недели в зависимости от даты) и номер недели

# Для сегодняшнего дня
def curent_day():
	now = dt.date.today()
	delta = now - FIRST_DAY
	return delta.days % 14,delta.days//7 + 1 

# Для любой даты
def any_date(str):
	date = list(map(int,str.split(".")))
	date = dt.date(date[2],date[1],date[0])

	delta = date - FIRST_DAY

	return delta.days % 14,delta.days//7 + 1  #  Индекс дня в массиве из расписания (день недели в зависимости от даты) и номер недели
