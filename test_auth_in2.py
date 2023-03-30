import requests

class TestAuthorization2():
    def test_auth_in(self):
        url = 'https://api.mobi.dev.alif.cloud/api/mobi/v1/auth/in'
        body = { "action": "auth",
                "phone": "+992985260338",
                "otp": "77777",
                "DeviceID": "d994ff1e50fce44cdd4ff7b6eea70846",}
        headers = {
            "request-Hash":"",
            "AppVersion": "Android SDK:29(10),v.3.0.3.495",
            "Language": "ru"
        }

        response = requests.post(url=url, json=body, headers=headers)
        response_as_dict = response.json()
        print(response_as_dict)
        assert response_as_dict['code'] == 200