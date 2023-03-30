import requests

class TestPaymentSalom():
    def test_payment_salom(self):
        url = 'https://api.mobi.dev.alif.cloud/api/mobi/v1/payment/pay'
        body = {
                "providerId": 988,
                "providerFields": [
                    {
                        "id": "account",
                        "val": "985 26 03 38"
                    }
                ],
                "destAccount": "985 26 03 38",
                "sourceAccount": "182249",
                "type": "payment",
                "currencyCode": "tjs",
                "sourceAccountType": "installments",
                "sourceAccountGate": "crm",
                "amount": 9,
                "condition": 8479,
                "orderId": "811f6c1a-4995-4cae-b2ac-cc9d3bc802ee"
            }

        headers = {
            "Authorization": "tjd0cb87575964bd00e2d26cbfd521c84e43fe216181965d48c9812f1ca23755fa",
            "AppVersion": "Android SDK:29(10),v.3.0.3.495",
            "DeviceID":"d994ff1e50fce44cdd4ff7b6eea70846"
                }
        response = requests.post(url=url, json=body, headers=headers)
        response_as_dict = response.json()
        assert response_as_dict['message'] == 'Сумма транзакции меньше лимита, введите сумму побольше', f"{response_as_dict}"