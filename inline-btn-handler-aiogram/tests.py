import asyncio
import unittest
from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.filters import CallbackQueryFilter
from inline_btn_handler_aiogram import add_inline_button_handler

class MockMessage:
    def __init__(self):
        self.text = ""
    async def edit_text(self, text):
        self.text = text

class MockCallbackQuery:
    def __init__(self):
        self.data = "test_data"
        self.message = MockMessage()
        self.answered = False
    async def answer(self):
        self.answered = True

class InlineBtnHandlerAiogramTest(unittest.TestCase):
    def test_add_inline_button_handler(self):
        router = Router()
        add_inline_button_handler(router, "test_data", "Клик!")
        # Проверяем, что обработчик добавлен (1 шт.)
        self.assertEqual(len(router.callback_query_handlers), 1)
        # Проверяем работу обработчика
        cb_query = MockCallbackQuery()
        handler = router.callback_query_handlers[0].callback
        asyncio.run(handler(cb_query))
        self.assertTrue(cb_query.answered)
        self.assertEqual(cb_query.message.text, "Клик!")

if __name__ == "__main__":
    unittest.main()
