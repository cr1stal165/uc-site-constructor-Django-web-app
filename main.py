import requests

print("hello world!")


def get_companies(users_id):
    #response = requests.get('https://reestrdoma.ru/api/companies?user_id={}'.format(users_id))
    #data = response.json()
    #return data
    return[
        {'id' : 123, 'inn' : '2345566776', 'name' : 'ООО "УК Лучшая в городе"', 'adress' : 'Воронеж Победы 2', 'ogrn' : '4646464646', 'director:' : "Иванов Иван Иванович"},
        {'id': 124, 'inn': '2345566777', 'name': 'ООО "УК Лучшая в городе"', 'adress': 'Воронеж Победы 3', 'ogrn': '4646554646', 'director:': "Дональд Трамп"}
    ]


def get_company(users_id, company_id):
    # response = requests.get('https://reestrdoma.ru/api/company?user_id={}&company_id={}'.format(users_id, company_id))
    # data = response.json()
    # return data
    return {'id' : 123, 'inn' : '2345566776', 'name' : 'ООО "УК Лучшая в городе"', 'adress' : 'Воронеж Победы 2', 'ogrn' : '4646464646', 'director:' : "Иванов Иван Иванович"}


def get_houses(users_id, company_id):
    # response = requests.get('https://reestrdoma.ru/api/houses?user_id={}&company_id={}'.format(users_id, company_id))
    # data = response.json()
    # return data
    return[
        {'id' : 123, 'adress' : 'Воронеж Победы 5'},
        {'id': 123, 'adress': 'Воронеж Победы 6'}
    ]


def get_house(user_id, company_id):
    # response = requests.get('https://reestrdoma.ru/api/house?user_id={}&company_id={}'.format(users_id, company_id))
    # data = response.json()
    # return data
    return {'id' : 123, 'adress' : 'Воронеж Победы 5'}
