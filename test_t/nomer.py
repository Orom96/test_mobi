import requests

class TestSignin():
    def test_auth_signin(self):
        url = 'https://api.mobi.dev.alif.cloud/api/mobi/v1/t/+992985260338'
            body = {}
        headers = {
            "Authorization":"tj376836603e0f95ecfeb2e7b5ace3cabeca9c8b558a0e58c11b28147f91527b91",
            "AppVersion": "Android SDK:29(10),v.3.0.3.495",
            "Language": "ru",
            "Accept": "application/json",
            "DeviceID": "d994ff1e50fce44cdd4ff7b6eea70846"
        }
        response = requests.get(url=url, json=body, headers=headers)
        response_otvet = response.json()
        print(response_otvet)
        assert response_otvet['code'] == 200
        assert response_otvet ['payload'] == null