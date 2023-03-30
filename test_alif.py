import requests

class TestAlif():
    def test_alif(self):
        url = 'https://api.mobi.dev.alif.cloud/api/mobi/v1/cashback/top'
        body = {}
        headers = {
            "Authorization": "tj4c9c7ef23a1779f1799386ad340776312c8ec0797b4c266e61ead4879eef1eab",
            "DeviceID": "d994ff1e50fce44cdd4ff7b6eea70846",
            "AppVersion": "Android SDK:29(10),v.3.0.3.495"
        }

        response = requests.post(url=url, json=body, headers=headers)
        response_as_dict = response.json()

        # with open("log.log", 'w') as f:
        #     f.write(
        #         f"'header': {headers} \n"
        #         f"'url': {url} \n"
        #         f"'body': {body}\n"
        #         f"'response': {response_as_dict}"
        #     )
        assert response_as_dict['code'] == 200, f"Unexpected code. Expected 200. Actually = {response_as_dict['code']}"
         assert response_as_dict['payload'][0]['mainCategoryOrder'] == 1