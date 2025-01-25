import unittest
from support_bot import SupportBot

class TestSupportBot(unittest.TestCase):
    def setUp(self):
        self.bot = SupportBot()

    def test_exit_commands(self):
        self.assertTrue(self.bot.make_exit("bye"))
        self.assertTrue(self.bot.make_exit("quit"))
        self.assertFalse(self.bot.make_exit("hello"))

    def test_match_reply(self):
        reply = "I need help with my product"
        response = self.bot.match_reply(reply)
        self.assertIn(response, self.bot.ask_about_product())

if __name__ == "__main__":
    unittest.main()
