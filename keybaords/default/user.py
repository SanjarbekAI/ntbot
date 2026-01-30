from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def share_contact(_):
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=_("☎️ Share phone number"), request_contact=True)
        ]], resize_keyboard=True
    )


async def share_location(_):
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=_("📍 Share my location"), request_location=True)
        ]], resize_keyboard=True
    )


async def user_main_menu(_):
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("🎓 Courses")),
                KeyboardButton(text=_("🎉 Events")),
            ],
            [
                KeyboardButton(text=_("☎️ Contacts")),
                KeyboardButton(text=_("⚙️ Settings")),
            ]
        ], resize_keyboard=True
    )
