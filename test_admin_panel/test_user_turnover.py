import requests
import pytest
# тестирование скачивания оборота пользователя
class TestPaymentMethod():
    def test_user_turnover(self):
        url = 'https://reportmobi.alif.tj/api/reports/v1/user/turnover'
        body = {"dateFrom": "20.02.2023",
                "dateTo": "25.02.2023",
                "limit": 0,
                "offset": 0,
                "phone": "",
                "type": 0,
                "userID": 0}
        headers = {
            "Authorization": "eae97a5611222954e3b3bef8dce20d0a205bb0e476191813642837fb34b20142",
            "language": "ru"
            # "DeviceID": "d994ff1e50fce44cdd4ff7b6eea70846",
            # "AppVersion": "Android SDK:29(10),v.3.0.3.495"
        }

        response = requests.post(url=url, json=body, headers=headers)
        response_as_dict = response.json()
        print(response_as_dict)
        assert response_as_dict['code'] == 200, f"Unexpected code. Expected 200. Actually = {response_as_dict['code']}"
        # assert response_as_dict['payload'] == [{'userID': type(int), 'balanceOnStart': type(int), 'balanceOnEnd': type(int), 'income': type(int),
        #                                         'expense': type(int), 'phone': type(str), 'fullName': type(str), 'identification': type(str),
        #                                         'status': type(str)}]
        #  # assert isinstance(response_as_dict['payload'][0]['userID'], int)