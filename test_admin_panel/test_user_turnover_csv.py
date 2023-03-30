import requests
# тестирование скачивания оборота пользователя
class TestPaymentMethod():
    def test_user_turnover(self):
        url = 'https://reportmobi.alif.tj/api/reports/v1/user/turnover/csv'
        body = {"dateFrom": "20.02.2023",
                "dateTo": "25.02.2023",
                "limit": 0,
                "offset": 0,
                "phone": "+992555555651",
                "type": 0,
                "userID": 0}
        headers = {
            "Authorization": "0b1157e57cb0002978a3fd4a0ea0e24bee413c3e109e45f7f2b2f47260bf38e2",
            "language": "ru"
            # "DeviceID": "d994ff1e50fce44cdd4ff7b6eea70846",
            # "AppVersion": "Android SDK:29(10),v.3.0.3.495"
        }

        response = requests.post(url=url, json=body, headers=headers)
        response_as_dict = response.json()
        print(response_as_dict)
         assert response_as_dict['code'] == 200, f"Unexpected code. Expected 200. Actually = {response_as_dict['code']}"