import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from credits import bot_token, bot_token_omauga
from aiogram.utils.keyboard import ReplyKeyboardBuilder

logging.basicConfig(level=logging.INFO)
bot = Bot(token = bot_token_omauga)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Игры", callback_data = "play"),
            types.KeyboardButton(text="Приложения по монтажу", callback_data = "programs"),
            types.KeyboardButton(text="СТОП, ты мне надоел", callback_data="exit"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Тыкните на кнопку"
    )
    await message.answer("Привет, в этом боту вы сможеете скачать платные программы - БЕСПЛАТНО.", reply_markup=keyboard)


@dp.message(F.text.lower() == "игры")
async def play_lower(message: types.Message):
    kb1=[
        [
            types.KeyboardButton(text="Hitman", callback_data="hitman"),
            types.KeyboardButton(text="CupHead", callback_data="cuphead"),
            types.KeyboardButton(text="FNAF", callback_data="cuphead"),
            types.KeyboardButton(text="Rust", callback_data="rust"),
            types.KeyboardButton(text="Вернуться в главное меню", callback_data="leaf"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb1,
        resize_keyboard=True,
        input_field_placeholder="Тыкните на кнопку"
    )
    await message.answer("Выбери игру которую хочешь скачать",
                         reply_markup=keyboard)




@dp.message(F.text.lower() == "приложения по монтажу")
async def programs_for_m(message: types.Message):
    kb2=[
        [
            types.KeyboardButton(text="Adoby Photoshop", callback_data="adobyp"),
            types.KeyboardButton(text="Author Efects", callback_data="adobya"),
            types.KeyboardButton(text="Вернуться в главное меню", callback_data="leaf"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb2,
        resize_keyboard=True,
        input_field_placeholder="Тыкните на кнопку"
    )
    await message.answer("Выбери Программу которую хочшеь скачать",
                         reply_markup=keyboard)



@dp.message(F.text.lower() == "hitman")
async def programs_for_m(message: types.Message):
    kb3 = [
        [
            types.KeyboardButton(text="Hitman: Absolution", callback_data="hitman1"),
            types.KeyboardButton(text="Hitman 2", callback_data="hitman2"),
            types.KeyboardButton(text="Hitman 3", callback_data="hitman3"),
            types.KeyboardButton(text="Вернуться в главное меню", callback_data="leaf"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb3,
        resize_keyboard=True,
        input_field_placeholder="Выбери что тебя интересует"
    )
    await message.answer("Выбери чатсь которую хочешь скачать",
                         reply_markup=keyboard)

@dp.message(F.text.lower() == "fnaf")
async def programs_for_m(message: types.Message):
    kb4 = [
        [
            types.KeyboardButton(text="Five Nights at Freddy's", callback_data="fnaf1"),
            types.KeyboardButton(text="Five Nights At Freddy's 2", callback_data="fnaf2"),
            types.KeyboardButton(text="Five Nights At Freddy's 4", callback_data="fnaf4"),
            types.KeyboardButton(text="Five Nights at Freddy's Security Breach", callback_data="fnafsq"),
            types.KeyboardButton(text="Вернуться в главное меню", callback_data="leaf"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb4,
        resize_keyboard=True,
        input_field_placeholder="Выбери что тебя интересует"
    )
    await message.answer("Выбери чатсь которую хочешь скачать",
                         reply_markup=keyboard)


@dp.message(F.text.lower() == "five nights at freddy's")
async def fnaf_1(message: types.Message):
    await message.answer("Лови ссылку: https://itorrents-igruha.org/6371-five-nights-at-freddys.html ")

@dp.message(F.text.lower() == "five nights at freddy's 2")
async def fnaf_2(message: types.Message):
    await message.answer("Лови ссылку: https://itorrents-igruha.org/430-5-nochey-s-freddi-2.html ")

@dp.message(F.text.lower() == "five nights at freddy's 4")
async def fnaf_4(message: types.Message):
    await message.answer("Лови ссылку: https://itorrents-igruha.org/429-five-nights-at-freddys-4.html ")

@dp.message(F.text.lower() == "five nights at freddy's security breach")
async def fnaf_sq(message: types.Message):
    await message.answer("Лови ссылку: https://itorrents-igruha.org/6449-five-nights-at-freddys-security-breach.html ")



@dp.message(F.text.lower() == "hitman: absolution")
async def play_h_1(message: types.Message):
    await message.answer("Лови ссылку: https://itorrents-igruha.org/571-05-hitman-absolution-besplatno-1.html ")

@dp.message(F.text.lower() == "hitman 2")
async def play_h_2(message: types.Message):
    await message.answer("Лови ссылку: https://itorrents-igruha.org/3003-04-hitman-2-besplatno-pc-1.html ")

@dp.message(F.text.lower() == "hitman 3")
async def play_h_1(message: types.Message):
    await message.answer("Лови ссылку: https://itorrents-igruha.org/5325-hitman-3.html ")

@dp.message(F.text.lower() == "cuphead")
async def play_cup_head(message: types.Message):
    await message.answer("Лови ссылку: https://itorrents-igruha.org/547-01-cuphead-rus.html")


@dp.message(F.text.lower() == "adoby photoshop")
async def programs_adobby(message: types.Message):
    await message.answer("Лови ссылку: https://rsload.net/soft/big-programm/14213-adobe-photoshop.html")

@dp.message(F.text.lower() == "author efects")
async def programs_au(message: types.Message):
    await message.answer("Лови ссылку: https://diakov.net/15282-adobe-after-effects-2023-v230.html")

@dp.message(F.text.lower() == "rust")
async def play_rust(message: types.Message):
    await message.answer("Лови ссылку: https://itorrents-igruha.org/519-rust.html")


@dp.message(F.text.lower() == "вернуться в главное меню")
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Игры", callback_data = "play"),
            types.KeyboardButton(text="Приложения по монтажу", callback_data = "programs")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Тыкните на кнопку"
    )
    await message.answer("Выбери интересующий тебя пункт", reply_markup=keyboard)

@dp.message(F.text.lower() == "стоп, ты мне надоел")
async def cmd_start(message: types.Message):
    await message.answer("Пока, если буду нужен пиши снова /start")
async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())