import pandas as pd
import http.client
import json


def curlFunc(body):
    conn = http.client.HTTPSConnection("ghtk-payment.ghtk.vn")
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJFUzI1NiIsImtpZCI6IjAxRk0zWllBQUpBQ0JCRE5YREE5VzlLVk5XXzE2MzY1MTY3MDIiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJld2FsbGV0IGdodGstcGF5bWVudCIsImV4cCI6MTY1Mjg1NzkzNywianRpIjoiMDFHMzhEUkdZRjVCMjBQVjc1N0RKTVNWQkEiLCJpYXQiOjE2NTI3NzE1MzcsImlzcyI6Imh0dHBzOi8vYXV0aC5naWFvaGFuZ3RpZXRraWVtLnZuIiwic3ViIjoiMDFGTTNaWUFBSkFDQkJETlhEQTlXOUtWTlciLCJzY3AiOlsiZXdhbGxldDpmdW5kLXRyYW5zZmVyLmRpcmVjdCIsImV3YWxsZXQ6ZnVuZC10cmFuc2Zlci5iYXRjaCIsImV3YWxsZXQ6ZnVuZC10cmFuc2Zlci5kaXJlY3Quc2hvcCIsImdodGstcGF5bWVudDpvcmRlci1yZWFkIiwiZ2h0ay1wYXltZW50Om9yZGVyLXdyaXRlIiwiZ2h0ay1wYXltZW50OnRyYW5zYWN0aW9uLWxvZy13cml0ZSIsImV3YWxsZXQ6dHJhbnNhY3Rpb24ucmVhZCIsImV3YWxsZXQ6YWNjb3VudC5pbnF1aXJ5IiwiZXdhbGxldDpnaHRrLXBheW1lbnQuc2NoZWR1bGUuc2hvcCIsImdodGstcGF5bWVudDpjb2Qtb3JkZXItcmVhZCIsImdodGstcGF5bWVudDpjb2Qtb3JkZXItd3JpdGUiLCJnaHRrLXBheW1lbnQ6c2hvcC13cml0ZSJdLCJjbGllbnRfaWQiOiIwMUZNM1pZQUFKQUNCQkROWERBOVc5S1ZOVyIsInR5cGUiOiJkaXJlY3QifQ.uDtC5IhCofJXRN3gbcjPjpNTBraLeCP40np0p3pT146YXbikb3A2Vlm3lsvkjs5KV5cXEElF1zN75_b4mBtpxw',
        'Content-Type': 'application/json',
        'Cookie': 'JSESSIONID=44AB9DA60C62A808CE0B081A7B5A7330; JSESSIONID=71AB702229BDAC2095B888E8054921B5; JSESSIONID=55DA1647E73CF86B66585A0EFA9DA4B8; JSESSIONID=201D428A6F07E5BFC3EEE03C35ECE0E9; JSESSIONID=CEB316196C0A623333780E554F7B2CCD'
    }

    payload = json.dumps(body)
    conn.request("POST", "/api/v1/wallet/transaction", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


if __name__ == '__main__':
    # df = pd.read_csv('../files/Bank_payment_schedule.csv')
    df = pd.read_csv('../files/sample.csv')
    df.head()
    # curlFunc(df['body'])
