import telebot
import json
import requests

bot = telebot.TeleBot("telegram_bot_token")

api_key = 'api_key'
url = 'http://localhost:7070/api/v1/workspace/firstworkspace/chat'
headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}

def send_request(message):

    payload = {
            "message": f"{message}",
            "mode": "chat",
            "sessionId": "identifier-to-partition-chats-by-external-id",
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Request failed with status code " + str(response.status_code)}

@bot.message_handler()
def start(message):
    if message.text == "Hello" and message.from_user.id == 'This should have been my account id :)' :
        mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>, my creator'
        bot.send_message(message.chat.id,mess,parse_mode='html')
    elif message.text == "Hello":
        mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>, someone I dont know'
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == "I want a million":
        t = 0
        bot.send_message(message.chat.id, 'Breaking into the bank', parse_mode='html')
        for a in range(10):
            t += 10
            bot.send_message(message.chat.id, str(t) + '%', parse_mode='html')
    elif message.text == "Wether":
        question = bot.send_message(message.chat.id, 'All right, enter the city', parse_mode='html')
        bot.register_next_step_handler(question,wether)
    else:
        response = send_request(message.text)
        print(response)
        bot_response = response.get("textResponse")
        bot.send_message(message.chat.id, bot_response, parse_mode='html')

def wether(message):
    city = message.text
    try:
        weather_data = requests.get(url=f'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=eng&appid=79d1ca96933b0328e1c7e3e7a26cb347').json()
        temperature = round(weather_data['main']['temp'])
        description = weather_data['weather'][0]['description']
        bot.send_message(message.chat.id, 'Right now, the temperature in the city = '+ str(temperature) + '°C', parse_mode='html')
        bot.send_message(message.chat.id, 'Right now in the city ' + description, parse_mode='html')
    except:
        bot.send_message(message.chat.id, 'You have entered the wrong city or the server is not responding', parse_mode='html')

bot.polling(none_stop=True)
