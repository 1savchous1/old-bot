#                               ПЕРВАЯ ВЕРСИЯ БОТА С БИБЛИОТЕКОЙ TELEBOT!!!!!!!!! ЕСТЬ ОШИБОЧКИ!!!


from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

#                                Функция обработки команды /выбрать

async def choose(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Книги", callback_data='books')],
        [InlineKeyboardButton("Кино", callback_data='movies')],
        [InlineKeyboardButton("Магазин", callback_data='shop')],
        [InlineKeyboardButton("Подписки", callback_data='subscriptions')],
        [InlineKeyboardButton("Список команд", callback_data='commands')],
        [InlineKeyboardButton("Поддержка", callback_data='support')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Пожалуйста, выберите один из вариантов:', reply_markup=reply_markup)

#                                 Функция обработки команды /test

async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Команда /test работает!')

#                                 Основная функция для запуска бота

async def main() -> None:
    application = ApplicationBuilder().token("токен!!!").build()

    #                             Регистрация команд
    application.add_handler(CommandHandler("выбрать", choose))
    application.add_handler(CommandHandler("test", test_command))  # Добавлена тестовая команда

    await application.run_polling()

if __name__ == '__main__':
    import asyncio