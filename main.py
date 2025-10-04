# main.py
# ...
# Авторское право (c) 2024 Кучеренко В.А. (AlterVall). Все права защищены.
# Использование регулируется файлом LICENSE в корне проекта.

import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load environment variables
load_dotenv()

# Get the bot token from environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Import calculator functions
from utils.electric_calculator import calculate_electricity_consumption, calculate_cost

# Define a command handler function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your Electric Bot. Use /calculate to calculate electricity consumption.')

# Define a command handler for calculating electricity
async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Example calculation (in a real bot, this would be more complex)
    device_power_watts = 100  # Example device power in watts
    hours_used = 5            # Example usage time in hours
    cost_per_kwh = 0.15       # Example cost per kWh in currency units
    
    consumption = calculate_electricity_consumption(device_power_watts, hours_used)
    total_cost = calculate_cost(consumption, cost_per_kwh)
    
    response = f"Device power: {device_power_watts} W\nUsage time: {hours_used} h\nCost per kWh: {cost_per_kwh}\n\n"
    response += f"Electricity consumption: {consumption:.2f} kWh\nTotal cost: {total_cost:.2f} currency units"
    
    await update.message.reply_text(response)

def main():
    # Create the Application and pass it your bot's token
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("calculate", calculate))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == '__main__':
    main()
