from parser.parse import *
from parser.get_day_of_week import *

helpMenu = """
/help - shows this menu
/update_group - set new group for you
/my_group - prints you gruop
/today - prints schedule for today
"""

lessons = { "BISO-01-22":get_lessons("БИСО-01-22"),
	        "BISO-02-22":get_lessons("БИСО-02-22"),
	        "BISO-03-22":get_lessons("БИСО-03-22"),} 

days = ["Monday", "Tuesday", "Wednesday", "Thursday ", "Friday", "Saturday", "Sundat"]
pares = ["no pares!!!!","only one pare","two pares","three pares","four pares","five pares:(","six pares :(((("]
week = ["odd", "even"]

# Выдает расписание конкретного дня в расписании
def create_output(group, day_num, week_num=-1):
	count_lessons = 1
	day_lessons = lessons[group][day_num]
	output_str = f"{days[day_num%7]}, {week[day_num//7]} week.\n\nYou've got {pares[len(day_lessons)-day_lessons.count('')]}:\n\n"
	if week_num != -1:
		output_str = f"________Week number {week_num}_________\n" + output_str

	for i in range(len(day_lessons)):
		if type(day_lessons[i]) == type([]):
			output_str = output_str + f"->   Pare {count_lessons}: {' '.join(day_lessons[i])}\n\n"
		count_lessons+=1
	return output_str