import requests

URL = "https://app.goflightlabs.com/flights?access_key=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiOGM4NTgwODA5ZmM5OTdlMzkwM2FmOGEwZGY0NzE2YzA3ODZiMTIwZWNkMmVhY2I3MTQ5MjJmODlmMGUxNGM2YzEwYTc0MjcwY2VmNWJlYjciLCJpYXQiOjE2NjA0MTgwMzcsIm5iZiI6MTY2MDQxODAzNywiZXhwIjoxNjkxOTU0MDM3LCJzdWIiOiIxMDU4NCIsInNjb3BlcyI6W119.TBhBPA7pPv40HuiX54qke9lk0ntyiJtSiyXm7PzpZImc4Z_EVDduxtUBdvusOjZWb-FDL2jxERCxRGqHpHyW6g"



r = requests.get(url=URL+"&flight_iata=DL1350")
data = r.json()
print(data)
