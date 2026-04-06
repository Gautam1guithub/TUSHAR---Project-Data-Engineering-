import requests
response = requests.get('https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_2023_10.zip')

print(response)