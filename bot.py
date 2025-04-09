
import requests
import time
import telegram

TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
API_URL = "https://diuwin.bet/api/some_endpoint"  # Replace with real endpoint

bot = telegram.Bot(token=TOKEN)

def fetch_data():
    try:
        response = requests.get(API_URL)
        return response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def make_prediction(data):
    # Dummy logic – replace with ML or rule-based logic
    return {
        "numbers": [3, 7],
        "colors": {"green": 50421, "red": 40322, "violet": 19320},
        "confidence": 89,
        "strategy": "Premium Analysis + Bet Distribution",
        "accuracy": "8/10",
    }

def send_prediction(prediction):
    message = f'''
Wingo Prediction
Time: {time.strftime('%H:%M:%S')}
Period: Live

Confidence: {prediction['confidence']}%
Numbers: {prediction['numbers'][0]} या {prediction['numbers'][1]}
Color Prediction:
- Green: ₹{prediction['colors']['green']}
- Red: ₹{prediction['colors']['red']}
- Violet: ₹{prediction['colors']['violet']}

Strategy: {prediction['strategy']}
Last 10 Accuracy: {prediction['accuracy']}

Alert: Jaldi karo! Bet Window चालू है!
'''
    bot.send_message(chat_id=CHAT_ID, text=message)

def main_loop():
    while True:
        data = fetch_data()
        if data:
            prediction = make_prediction(data)
            send_prediction(prediction)
        time.sleep(60)

if __name__ == "__main__":
    main_loop()
