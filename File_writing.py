из  User_interface  импортируйте  get_info  как  gi

gi = info()
writing_scv def ():
    файл = 'Телефонная книга.csv'
    открыть  с помощью (file, 'a', encoding = 'utf-8') в качестве  данных:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

writing_txt  определение ():
    файл = 'Phonebook.txt '
    открыть  с помощью (file, 'a', encoding = 'utf-8') в качестве  данных:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')