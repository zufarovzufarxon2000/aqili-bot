import asyncio
from os import getenv
from  dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from buttons import menu
load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(F"Assalomu alaykum!{message.from_user.full_name}\n Aqlli yordamchingiz sizning xizmatingizga  tayyor? 😊",reply_markup=menu)

@dp.callback_query()
async  def ans(callback: CallbackQuery):
    if callback.data=="diyfuz1":
        await  callback.answer()
        await callback.message.answer("Bugun sening kayfiyating shunchalik zo‘rki, hatto kofe ham seni taqlid qilolmaydi! ☕⚡")

    elif callback.data=="diyfuz2":
        await  callback.answer()
        await callback.message.answer( "Kayfiyating o‘rtacha? Hechqisi yo‘q, hatto kompyuter ham “loading”da! 💻😅")

    elif callback.data=="diyfuz3":
        await  callback.answer()
        await callback.message.answer( "Kayfiyating past? Hechqisi yo‘q, har bir “Monday” ham oxirida “Friday”ga aylanadi! 🗓️😄")


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)



# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    print("Bot ishladi✅")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

