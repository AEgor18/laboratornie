import requests


city = input('Введите название города: ')
x = '0e3e7db659a35f7ef331243fd896b5b7'
z = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={x}')
y = z.json()

temp = y['main']['temp']
temp_min = y['main']['temp_min']
temp_max = y['main']['temp_max']
feels_like = y['main']['feels_like']
description = y['weather'][0]['description']
humidity = y['main']['humidity']
wind = y['wind']['speed']
pressure = y['main']['pressure']

print('Ваш город:', city)
print('Температура:', temp, 'градусов')
print('Максимальная температура:',temp_max, 'градусов')
print('Минимальная температура:',temp_min, 'градусов')
print('Температура ощущается как:', feels_like, 'градусов')
print('Облачность:', description)
print('Влажность:', humidity, '%')
print('Скорость ветра:', wind, 'м/с')
print('Давление:', pressure, 'паскалей')