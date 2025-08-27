# [py-async-inline-btn-handler]
from aiogram import Router, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import CallbackQueryFilter

def add_inline_button_handler(router: Router, callback_data: str, response_text: str) -> None:
    """
    Регистрирует асинхронный обработчик нажатия inline-кнопки по callback_data в aiogram 3.x.

    :param router: Router aiogram, куда добавляется обработчик.
    :param callback_data: Значение callback_data, на которое реагируем.
    :param response_text: Ответ, который отправится пользователю.
    """
    @router.callback_query(F.data == callback_data)
    async def inline_btn_callback(query: CallbackQuery):
        await query.answer()
        await query.message.edit_text(response_text)
