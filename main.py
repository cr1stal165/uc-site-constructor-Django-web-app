class Main:

    @staticmethod
    def get_company(users_id, company_id):
        # response = requests.get('https://reestrdoma.ru/api/company?user_id={}&company_id={}'.format(users_id, company_id))
        # data = response.json()
        # return data
        return {'id' : 123, 'inn' : '2345566776', 'name' : 'ООО "УК Лучшая в городе"', 'adress' : 'Воронеж Победы 2', 'ogrn' : '4646464646', 'director:' : "Иванов Иван Иванович"}

    @staticmethod
    def get_houses(users_id, company_id):
        # response = requests.get('https://reestrdoma.ru/api/houses?user_id={}&company_id={}'.format(users_id, company_id))
        # data = response.json()
        # return data
        return[
            {'id' : 123, 'adress' : 'Воронеж Победы 5'},
            {'id': 123, 'adress': 'Воронеж Победы 6'}
        ]

    @staticmethod
    def get_house(user_id, company_id):
        # response = requests.get('https://reestrdoma.ru/api/house?user_id={}&company_id={}'.format(users_id, company_id))
        # data = response.json()
        # return data
        return {'id' : 123, 'adress' : 'Воронеж Победы 5'}

    @staticmethod
    def get_news(user_id, company_id):
        # response = requests.get('https://reestrdoma.ru/api/house?user_id={}&company_id={}'.format(users_id, company_id))
        # data = response.json()
        # return data
        return [{'id': 123, 'data': '10.10.2020', 'title': 'ЗАГОЛОВОК', 'text': 'dtimhdtophdhht'},
                {'id': 125, 'data': '10.10.2022', 'title': 'ЗАГОЛОВОК1', 'text': 'jflylpjlyjth'},
                {'id': 126, 'data': '10.10.2024', 'title': 'ЗАГОЛОВОК2', 'text': 'd4h67vm34v'}
                ]

