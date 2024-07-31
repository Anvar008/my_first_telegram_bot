from aiogram import Bot, Dispatcher,  F, types, filters
import asyncio
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
import openai
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

bot = Bot(token="7286373007:AAG-qfWEBqFqp6bQrt-H6EExCLMfJ-7DgK0")
dp = Dispatcher(bot=bot)

openai.api_key = "sk-proj-97VH1ArqmfoD4Bn1dIwqT3BlbkFJjXsRLTJ8cROh8MfISWHr"
openai.Model.list()

korzina = []

keyboard1 = [
    [KeyboardButton(text="uz"), KeyboardButton(text="ru")],
]
main_button1 = ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)

keyboard2 = [
    [KeyboardButton(text="Raqam berish", request_contact=True)],
]
main_button2 = ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)

keyboard3 = [
    [KeyboardButton(text="Kurs"), KeyboardButton(text="Korzina"), KeyboardButton(text="Biz haqida")],
    [KeyboardButton(text="Yordam"), KeyboardButton(text="Til almashtirish")],
]
main_button3 = ReplyKeyboardMarkup(keyboard=keyboard3, resize_keyboard=True)

keyboard4 = [
    [KeyboardButton(text="Python"), KeyboardButton(text="JS"), KeyboardButton(text="SQL")],
    [KeyboardButton(text="Unity"), KeyboardButton(text="C++"), KeyboardButton(text="C#")],
    [KeyboardButton(text="Qaytish")],
]
main_button4 = ReplyKeyboardMarkup(keyboard=keyboard4, resize_keyboard=True)

keyboard5 = [
    [InlineKeyboardButton(text="Xa", callback_data="Xa")],
]
main_button5 = InlineKeyboardMarkup(inline_keyboard=keyboard5)

keyboard6 = [
    [InlineKeyboardButton(text="Video", callback_data="Video"), InlineKeyboardButton(text="Sayt", callback_data="Sayt")],
]
main_button6 = InlineKeyboardMarkup(inline_keyboard=keyboard6)


class Registration(StatesGroup):
    name = State()
    surname = State()
    phone_number = State()


@dp.message(filters.Command("start"))
async def start_bot(message: types.Message):
    await message.answer("Добро пожаловать")
    await message.answer("Выберите язык: ", reply_markup=main_button1)


@dp.message(F.text == "uz")
async def lang_uz(message: types.Message, state: FSMContext):
    await message.answer("Siz o'zbek tilini taladingiz\nRo'yxatdan o'ting: ")
    await state.set_state(Registration.name)
    await message.answer("Ismingizni yozing: ")


@dp.message(Registration.name)
async def name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.surname)
    await message.answer("Familiyezi kiriting: ")


@dp.message(Registration.surname)
async def surname(message: types.Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await state.set_state(Registration.phone_number)
    await message.answer("Raqamizi kiriting: ", reply_markup=main_button2)


@dp.message(Registration.phone_number)
async def phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    await message.answer("Siz ro'yxatdan o'tdingiz", reply_markup=main_button3)
    await state.clear()


@dp.message(F.text == "Kurs")
async def Kurs(message: types.Message):
    await message.answer("Mana bizi kurslarimiz: ", reply_markup=main_button4)


@dp.message(F.text == "Python")
async def python(message: types.Message):
    await message.answer("Python kursini korzinadan ochirib tashamoqchimisiz: ", reply_markup=main_button5)
    korzina.append("Python")


@dp.message(F.text == "JS")
async def python(message: types.Message):
    await message.answer("JavaScript kursini korzinadan ochirib tashamoqchimisiz: ", reply_markup=main_button5)
    korzina.append("JS")


@dp.message(F.text == "SQL")
async def python(message: types.Message):
    await message.answer("SQL kursini korzinadan ochirib tashamoqchimisiz: ", reply_markup=main_button5)
    korzina.append("SQL")


@dp.message(F.text == "Unity")
async def python(message: types.Message):
    await message.answer("Unity kursini korzinadan ochirib tashamoqchimisiz: ", reply_markup=main_button5)
    korzina.append("Unity")


@dp.message(F.text == "C++")
async def python(message: types.Message):
    await message.answer("C++ kursini korzinadan ochirib tashamoqchimisiz: ", reply_markup=main_button5)
    korzina.append("C++")


@dp.message(F.text == "C#")
async def python(message: types.Message):
    await message.answer("C# kursini korzinadan ochirib tashamoqchimisiz: ", reply_markup=main_button5)
    korzina.append("C#")


@dp.callback_query(F.data == "Xa")
async def Xa(call: types.CallbackQuery):
    await call.message.answer("Kursiz korzinadan ochirildi")
    korzina.pop()


@dp.message(F.text == "Qaytish")
async def qaytish(message: types.Message):
    await message.answer("Siz qaytingiz: ", reply_markup=main_button3)


@dp.message(F.text == "Korzina")
async def Korzina(message: types.Message):
    await message.answer(f"Mana sizi korzines: {korzina}")


@dp.message(F.text == "Biz haqida")
async def biz(message: types.Message):
    await message.answer(f"Yaratuvchi: Abdurashidov Anvarbek\nYoshi: 13", reply_markup=main_button6)


@dp.callback_query(F.data == "Video")
async def video(call: types.CallbackQuery):
    await call.message.answer_video(video="https://youtu.be/sGmNSsG-vrQ?si=fMo4xgbsYKYGu5L3")


@dp.callback_query(F.data == "Sayt")
async def sayt(call: types.CallbackQuery):
    await call.message.answer("https://marsit.uz/")


@dp.message(F.text == "Til almashtirish")
async def change_lang1(message: types.Message):
    await message.answer("Til almashtirin", reply_markup=main_button1)


@dp.message(F.text == "Yordam")
async def yordam(message: types.Message):
    responce = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=message.text,
        max_tokens=1000,
    )
    await message.reply(responce["choices"][0]["text"])


keyboard22 = [
    [KeyboardButton(text="Дать номер", request_contact=True)],
]
main_button22 = ReplyKeyboardMarkup(keyboard=keyboard22, resize_keyboard=True)

keyboard33 = [
    [KeyboardButton(text="Курсы"), KeyboardButton(text="Корзина"), KeyboardButton(text="О нас")],
    [KeyboardButton(text="Помощь"), KeyboardButton(text="Сменить язык")],
]
main_button33 = ReplyKeyboardMarkup(keyboard=keyboard33, resize_keyboard=True)

keyboard44 = [
    [KeyboardButton(text="python"), KeyboardButton(text="js"), KeyboardButton(text="sql")],
    [KeyboardButton(text="unity"), KeyboardButton(text="c++"), KeyboardButton(text="c#")],
    [KeyboardButton(text="Вернутся")],
]
main_button44 = ReplyKeyboardMarkup(keyboard=keyboard44, resize_keyboard=True)

keyboard55 = [
    [InlineKeyboardButton(text="Да", callback_data="да")],
]
main_button55 = InlineKeyboardMarkup(inline_keyboard=keyboard55)

keyboard66 = [
    [InlineKeyboardButton(text="Видео", callback_data="Видео"), InlineKeyboardButton(text="Сайт", callback_data="Сайт")]
]


class Registration1(StatesGroup):
    name1 = State()
    surname1 = State()
    phone_number1 = State()


@dp.message(F.text == "ru")
async def lang_ru(message: types.Message, state: FSMContext):
    await message.answer("Вы выбрали русский язык\nПройдите регистрацию: ")
    await state.set_state(Registration1.name1)
    await message.answer("Введите свое имя: ")


@dp.message(Registration1.name1)
async def name1(message: types.Message, state: FSMContext):
    await state.update_data(name1=message.text)
    await state.set_state(Registration1.surname1)
    await message.answer("Введите свою фамилию: ")


@dp.message(Registration1.surname1)
async def surname1(message: types.Message, state: FSMContext):
    await state.update_data(surname1=message.text)
    await state.set_state(Registration1.phone_number1)
    await message.answer("Введите свой номер: ", reply_markup=main_button22)


@dp.message(Registration1.phone_number1)
async def phone_number1(message: types.Message, state: FSMContext):
    await state.update_data(phone_number1=message.contact.phone_number)
    await message.answer("Вы прошли регистрацию", reply_markup=main_button33)
    await state.clear()


@dp.message(F.text == "Курсы")
async def Kurs1(message: types.Message):
    await message.answer("вот наши курсы: ", reply_markup=main_button44)


@dp.message(F.text == "python")
async def python1(message: types.Message):
    await message.answer("Хотите удалить python из корзины: ", reply_markup=main_button55)


@dp.message(F.text == "js")
async def python(message: types.Message):
    await message.answer("Хотите начать изучать js: ", reply_markup=main_button55)


@dp.message(F.text == "sql")
async def python(message: types.Message):
    await message.answer("Хотите начать изучать sql: ", reply_markup=main_button55)


@dp.message(F.text == "unity")
async def python(message: types.Message):
    await message.answer("Хотите начать изучать unity: ", reply_markup=main_button55)


@dp.message(F.text == "c++")
async def python(message: types.Message):
    await message.answer("Хотите начать изучать c++: ", reply_markup=main_button55)


@dp.message(F.text == "c#")
async def python(message: types.Message):
    await message.answer("Хотите начать изучать c#: ", reply_markup=main_button55)


@dp.callback_query(F.data == "да")
async def Xa1(call: types.CallbackQuery):
    await call.message.answer("Курс удален из корзины")
    korzina.pop()


@dp.message(F.text == "Вернутся")
async def qaytish1(message: types.Message):
    await message.answer("Вы вернулись: ", reply_markup=main_button33)


@dp.message(F.text == "Корзина")
async def Korzina1(message: types.Message):
    await message.answer(f"Вот ваша корзина: {korzina}")


@dp.message(F.text == "О нас")
async def biz1(message: types.Message):
    await message.answer("Создатель: Абдурашидов Анварбек\nВозраст: 13")


@dp.callback_query(F.data == "Видео")
async def video(call: types.CallbackQuery):
    await call.message.answer_video(video="https://youtu.be/sGmNSsG-vrQ?si=fMo4xgbsYKYGu5L3")


@dp.callback_query(F.data == "Сайт")
async def sayt(call: types.CallbackQuery):
    await call.message.answer("https://marsit.uz/")


@dp.message(F.text == "Сменить язык")
async def change_lang2(message: types.Message):
    await message.answer("Сменить язык: ", reply_markup=main_button1)


@dp.message(lambda message: message.text == "Yordam")
async def yordam(message: types.Message):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=message.text,
        max_tokens=1000,
    )
    await message.reply(response.choices[0].text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
