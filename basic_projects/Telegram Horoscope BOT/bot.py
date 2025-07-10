# Import necessary modules
import os
from dotenv import load_dotenv  # Used to load environment variables from a .env file
load_dotenv()

import telebot  # Telegram Bot API wrapper
from telebot import types  # For creating custom keyboard layouts
from utils import get_daily_horoscope  # A custom function to get horoscope data

# Get the bot token from environment variables
BOT_TOKEN = os.environ.get('BOT_TOKEN')
if not BOT_TOKEN:
    print("ERROR: BOT_TOKEN is not set.")
    exit(1)

# Initialize the Telegram bot
bot = telebot.TeleBot(BOT_TOKEN)

# 🟢 Handle the /start and /hello commands
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello, how are you doing?")

# 🪐 Handle the /horoscope command - ask user to select their zodiac sign
@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    # Create a keyboard layout for zodiac signs
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)
    
    # List of all 12 zodiac signs
    signs = ["Aries", "Taurus", "Gemini", "Cancer",
             "Leo", "Virgo", "Libra", "Scorpio",
             "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    
    # Add buttons for each zodiac sign
    markup.add(*(types.KeyboardButton(s) for s in signs))

    # Send message with custom keyboard
    bot.send_message(message.chat.id, "Select your zodiac sign:", reply_markup=markup)

    # After sign selection, move to the next step: day selection
    bot.register_next_step_handler(message, day_handler)

# 📅 Ask the user to select the day after they chose a zodiac sign
def day_handler(message):
    sign = message.text.capitalize()  # Get the selected sign, ensure it has a capital first letter
    
    # Create keyboard for day options
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    options = ["TODAY", "TOMORROW", "YESTERDAY", "YYYY‑MM‑DD"]  # Last option allows custom date
    markup.add(*(types.KeyboardButton(opt) for opt in options))

    # Send message to select day and move to fetch horoscope
    msg = bot.send_message(message.chat.id, f"You chose *{sign}*. Now pick a day:", 
                           parse_mode="Markdown", reply_markup=markup)
    bot.register_next_step_handler(msg, fetch_horoscope, sign)  # Pass `sign` to next handler

# 🔮 Fetch and display horoscope
def fetch_horoscope(message, sign):
    day = message.text  # Get the selected day (e.g., TODAY, TOMORROW, or a specific date)
    
    try:
        # Call utility function to get horoscope data
        horoscope = get_daily_horoscope(sign, day)
        data = horoscope["data"]

        # Format and send the horoscope message
        text = f"*Here’s your horoscope:*\n{data['horoscope_data']}\n" \
               f"_Sign: {sign}_  |  _Day: {data['date']}_"
        
        bot.send_message(message.chat.id, text, parse_mode="Markdown",
                         reply_markup=types.ReplyKeyboardRemove())  # Remove custom keyboard
    except Exception as e:
        # Log the error to the console
        print("Error:", e)

        # Inform the user something went wrong
        bot.send_message(message.chat.id,
                         "Sorry, couldn’t fetch horoscope. Try again?", 
                         reply_markup=types.ReplyKeyboardRemove())

# 🗣️ Echo fallback for any unrecognized messages
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# 🔁 Keep bot running indefinitely
bot.infinity_polling()
