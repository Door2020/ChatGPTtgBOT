import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests

admin_id = #your id
telegram_token = "Telegram_token"
openai.api_key = "openai_token"

bot = Bot(telegram_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['info'])
async def help_command(message: types.Message):
    await message.reply('Сотрудничество - @Name')

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply('Список всех комманд:\n/start - начальная комманда \n'
'/img[текст] - генерация фото по описанию \n/help - список всех команд\n/info - сотрудничетво')

@dp.message_handler(commands=['start'])
async def greet_user(message: types.Message):
    await message.reply('''Привет✌️

ChatGPT - крупнейшая языковая модель, созданная OpenAI.
Она разработана для обработки естественного языка и может помочь вам во многих аспектах.
🔥В том числе и на русском языке🔥
Список всех комманд и тд - /help
👇Я постараюсь ответить на твои вопросы👇''')




@dp.message_handler(commands=['img'])
async def send_image(message: types.Message):
    if message.text == '/img':
        await message.answer('Бот не работает без аргументов😡')
    else:
        await message.answer('Dalle-e 2: Ожидайте, идет генерация⏳')
        response = openai.Image.create(
            prompt=message.text,
            n=1,
            size="1024x1024",
        )
        await message.answer_photo(response["data"][0]["url"])



@dp.message_handler()
async def send(message: types.Message):
    await message.answer('ChatGPT: Ожидайте, запрос принят⏳')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    await message.answer(response['choices'][0]['text'])





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

