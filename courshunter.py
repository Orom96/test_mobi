# import requests
# # payload = {"content":"12345"}
# # response = requests.get("https://alif.shop", params=payload)
# # print(response.json)
# headers = {"some_headers":"12345"}
# response = requests.get("https://alif.shop", headers = headers)
# print(response.text)
# print((response.))

class TestExample:
    def test(self):
        a = 5
        b = 6
        expected_Sum = 11
        assert a + b == expected_Sum, f"сумма a+b не равна {expected_Sum}"

    def test_2(self):
        a = 5
        b = 15
        expected_Sum = 14
        assert a + b == expected_Sum, f"сумма a+b не равна {expected_Sum}"
        
    def test_hello(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = "vitalii"
        data = {"name":name}
        response = request.get(url, params=data)
        assert response.status_code == 200, "Wrong response code"
        response_dict = response.json()
        assert "answer" in response_dict, "There is no field 'answer'"
        expected_resposne_text = f"{name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_resposne_text, "Actual text is the response  is not correct"
