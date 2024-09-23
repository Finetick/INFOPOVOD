#Напишите скрипт, который по введенному пользователем числу от 1 до 12, будет выводить на экран сообщение в виде названия месяца и времени года.
#  Если пользователь введет недопустимое число, программа должна выдавать сообщение об ошибке

monthNumber = input("Введите число от 1 до 12")

if not monthNumber.isdigit():
    print("Вы ввели не число")
else:
    monthNumber = int(monthNumber)

    if monthNumber < 1 or monthNumber > 12:
        print("Ваше число больше 12 или меньше 1")
    else:
        season = ""

        if monthNumber >= 3 and monthNumber <= 5:
            season = "Весна"
        elif monthNumber >= 6 and monthNumber <= 8:
            season = "Лето" 
        elif monthNumber >= 9 and monthNumber <= 11:
            season = "Осень"
        else:
            season = "Зима"

        month = ""

        if monthNumber == 1:
            month = "Январь"
        elif monthNumber == 2:
            month = "Февраль"
        elif monthNumber == 3:
            month = "Март"
        elif monthNumber == 4:
            month = "Апрель"
        elif monthNumber == 5:
            month = "Май"
        elif monthNumber == 6:
            month = "Июнь"
        elif monthNumber == 7:
            month = "Июль"
        elif monthNumber == 8:
            month = "Август"
        elif monthNumber == 9:
            month = "Сентябрь"
        elif monthNumber == 10:
            month = "Октябрь"
        elif monthNumber == 11:
            month = "Ноябрь"
        else:
            month = "Декабрь"

        print("Время года: ", season)
        print("Месяц: ", month)