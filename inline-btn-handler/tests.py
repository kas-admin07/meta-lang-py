import unittest
from telegram import Update, CallbackQuery, Message, Chat, User
from telegram.ext import CallbackContext, Application, CallbackQueryHandler
from inline_btn_handler import add_inline_button_handler

class MockApp:
    def __init__(self):
        self.handlers = []
    def add_handler(self, handler):
        self.handlers.append(handler)

class InlineBtnHandlerTest(unittest.TestCase):
    def test_add_inline_button_handler(self):
        app = MockApp()
        add_inline_button_handler(app, "test_data", "Clicked!")
        self.assertEqual(len(app.handlers), 1)
        self.assertIsInstance(app.handlers[0], CallbackQueryHandler)

if __name__ == "__main__":
    unittest.main()
