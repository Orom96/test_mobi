import requests
class TestFavBalance():
        def test_fav_balance(self):

            url = 'https://api.mobi.dev.alif.cloud/api/mobi/v1/favorites/balance'
            body = {}
            headers = {
                "Authorization": "tj6545b72ca549ec3261d84730253ad240230ef2f22807f0aef04a7d5edec18aad",
                "DeviceID": "d994ff1e50fce44cdd4ff7b6eea70846",
                "AppVersion": "Android SDK:29(10),v.3.0.3.495"
                      }

            response = requests.get(url=url, json=body, headers=headers)
            response_as_dict = response.json()
            print(response_as_dict)
