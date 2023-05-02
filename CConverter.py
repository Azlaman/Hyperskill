# write your code here!
import requests
import json

i = 1
currency_code = input()
r = requests.get('http://www.floatrates.com/daily/' + str(currency_code) + '.json')
json_str = json.loads(r.content)
cache = {'eur': "0.91096840218234", 'usd': "1.0977329154385"}
while i <= len(json_str):
    i += 1
    currency_for_exchage = input()
    if currency_for_exchage == '' or currency_for_exchage is None:
        break
    count_for_exchege = int(input())
    print(f'Checking the cache...')
    matched = 0
    matched_rate = 0
    for currency in cache:
        if currency_for_exchage.lower() == currency:
            matched += 1
            matched_rate = cache[currency]
            break
    if matched == 1:
        print(f'Oh! It is in the cache!')
        result = round(count_for_exchege * float(matched_rate), 2)
        print(f'You received {result} {currency_for_exchage.upper()}')
        continue
    else:
        print(f'Sorry, but it is not in the cache!')
        for currency in json_str:
            if currency.lower() == currency_for_exchage.lower():
                for item in json_str[str(currency_for_exchage.lower())]:
                    if item == 'rate':
                        rate = json_str[str(currency_for_exchage.lower())]['rate']
                        cache[currency.lower()] = rate
                        result = round(count_for_exchege * rate, 2)
                        print(f'You received {result} {currency_for_exchage.upper()}')
                        break
            continue
