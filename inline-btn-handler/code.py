# [py-inline-btn-handler]
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler

def add_inline_button_handler(app, callback_data: str, response_text: str) -> None:
    """
    Adds a handler for inline button callbacks.

    :param app: The Application instance from python-telegram-bot.
    :param callback_data: The callback_data string to listen for.
    :param response_text: The text to send when the button is pressed.
    """
    def button_callback(update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query.answer()
        query.edit_message_text(text=response_text)

    app.add_handler(CallbackQueryHandler(button_callback, pattern=f"^{callback_data}$"))
