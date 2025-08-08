import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
import keyboars as kb


load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

dp = Dispatcher()




# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.reply(f"Assalawma aleykum! Botimizg'a xosh kelipsiz! {message.from_user.first_name}",reply_markup= kb.keyboard_single_row )

@dp.message(F.text=="Profile")
async def profile_handler(message:Message):
    user_id=message.from_user.id
    full_name="Sarsenbaeva Gulmira"
    caption=f"Bottin iyesi: {full_name}, Telegram  ID: {user_id}"
    # await message.answer(f'Username: {message.from_user.username}')
    # await message.answer(f"Chat ID: {message.chat.id}")
    await message.answer_photo('AgACAgIAAxkBAAODaJI9Tw2TbSC9wHDxUfrxb3SV4XwAArL3MRtgl5BIcOMJM3CkB4ABAAMCAAN5AAM2BA', caption)
    
    photo_file_id="AgACAgIAAxkBAAODaJI9Tw2TbSC9wHDxUfrxb3SV4XwAArL3MRtgl5BIcOMJM3CkB4ABAAMCAAN5AAM2BAZZ"
    
    
    await message.answer_photo(photo=photo_file_id,caption="Gulmira"
    )



@dp.message(F.text=="help")
async def help_information(message: Message):
      await message.answer(f"{message.from_user.username} Mag'an sorawlarin'iz bolsa @gulmirabaltabaevna  akkina xabar qaldirsaniz boladi")

@dp.message(F.text == "test") # if text == test
async def magicfilter(message: Message):
      await message.answer(f'Username: {message.from_user.username}')
      await message.answer(f"Chat ID: {message.chat.id}")
      await message.answer_photo('AgACAgIAAxkBAAODaJI9Tw2TbSC9wHDxUfrxb3SV4XwAArL3MRtgl5BIcOMJM3CkB4ABAAMCAAN5AAM2BA')

@dp.message(F.photo)
async def photo_handler(soobsheine: Message):
      await soobsheine.reply(f'id = {soobsheine.photo[-1].file_id} - size = {soobsheine.photo[-1].file_size} uniqid = {soobsheine.photo[-1].file_unique_id}')
      await soobsheine.reply(f'id = {soobsheine.photo[0].file_id} - size = {soobsheine.photo[0].file_size} uniqid = {soobsheine.photo[0].file_unique_id}')



@dp.message()
async def echo_words(message:Message)->None:
    words=message.text.split()
    for word in words:
        await message.answer(word)
        await asyncio.sleep(0.5)




@dp.message(F.photo)
async def hello(soobsheine: Message):
      await soobsheine.reply(f'id = {soobsheine.photo[-1].file_id} - size = {soobsheine.photo[-1].file_size} uniqid = {soobsheine.photo[-1].file_unique_id}')
      await soobsheine.reply(f'id = {soobsheine.photo[0].file_id} - size = {soobsheine.photo[0].file_size} uniqid = {soobsheine.photo[0].file_unique_id}')


# Run the bot
@dp.message()
async def echo_words(message:Message)->None:
    words=message.text.split()
    for word in words:
        await message.answer(word)
        await asyncio.sleep(0.5)



    
    

    
async def main():
    bot=Bot(token=TOKEN)
    await dp.start_polling(bot)






if __name__ == "__main__":
    asyncio.run(main())
          