# from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
import requests
import datetime

def login():
    url = "https://new.albato.ru/api/user/auth/"
    payload = {"language": "ru", "login": "komiltuev@icloud.com", "password": "Zaqwsx123."}
    response = requests.post(url=url, json=payload)
    print("________________", response.text)
    return response.text

class HistoryView(viewsets.ViewSet):
    def list(self, request):
        login2 = login()
        if login2 == "OK":
            api = requests.get(f"https://new.albato.ru/api/bundle/history?bundleId=262890&dateFrom=2022-01-01&dateTo={datetime.date.today}0&expand=triggerActionData%2CtriggerDataAsObject")
            return Response(api)
        return Response(login2)
