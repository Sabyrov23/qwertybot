
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from decouple import config
import logging

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"HELLO {message.from_user.first_name}")

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "who is the creator of tik tok?"
    answers = [
        "Hyunjoo Shim",
        "Cho Jeong",
        "Lee Dong He",
        "Jihye Lee",
        "Znang Yiming",
        "Soon Hoe Kim",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="",
        open_period=25,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "who created atomic energy?"
    answers = [
        "Jhonson",
        "Chadwick",
        "David",
        "Kokeyn",
        "Gilbert",
        "Uilyam",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="",
        open_period=25,
        reply_markup=markup
    )

    async def mem(message: types.Message):
        photo = open("media/mem.jpg", 'rb')
        await bot.send_photo(message.chat.id, photo=photo)

    def register_handlers_client(dp: Dispatcher):
        dp.register_message_handler(start_handler, commands=['start', 'help'])
        dp.register_message_handler(quiz_1, commands=['quiz'])
        dp.register_message_handler(mem, commands=['mem'])