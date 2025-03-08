
import telegram
import asyncio
from barber.settings import TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID


async def send_telegram_message(token, chat_id, message, parse_mode="Markdown"):
    try:
        bot = telegram.Bot(token=token)
        await bot.send_message(chat_id=chat_id, text=message, parse_mode=parse_mode)
    except Exception as e:
        raise

# Тестируем отправку прямо тут
if __name__ == "__main__":
    message = "Тестовое сообщение"
    asyncio.run(send_telegram_message(TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID, message))