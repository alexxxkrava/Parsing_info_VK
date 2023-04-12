from main import *

with open('токен_вк.txt', 'r', encoding='UTF-8') as file:
    TOKEN = file.read().strip()

if __name__ == '__main__':
    person = VkUser(TOKEN)
    id = input('Введите id пользователя: ')
    # isarkisians

    person.get_json(id)
    person.get_photo(id)

    with open('user_info.md', 'w', encoding='UTF-8') as f:
        f.write(f'![](user_photo.jpg) \n')
        f.write(f'# {person.user_info(id)["response"][0]["first_name"]} {person.user_info(id)["response"][0]["last_name"]} \n')
        f.write(f'#### Числовой идентификатор: \n * {person.user_info(id)["response"][0]["id"]} \n')

        if person.user_info(id)["response"][0]["sex"] == 1:
            sex = 'Женщина'
            word = 'родилась'
        else:
            sex = 'Мужчина'
            word = 'родился'

        f.write(f'## {sex}, {word}: {person.user_info(id)["response"][0]["bdate"]} \n')
        f.write(f'## Карьера: \n')
        if person.user_info(id)["response"][0]["career"] == []:
            career = 'Нет данных'
        else:
            career = person.user_info(id)["response"][0]["career"][0]
            for i in career:
                for key, val in i.items():
                    f.write(f'## {key}:{val} \n')

        if person.user_info(id)["response"][0]["online"] == 0:
            status = 'не в сети'
        else:
            status = 'в сети'

        f.write(f'## На данный момент сейчас {status}')




