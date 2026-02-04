from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton

from filters.is_admin import IsAdmin
from keybaords.default.user import dynamic_reply_keyboard_builder

router = Router()


@router.message(F.text.in_(['🎓 Courses', '🎓 Курсы', '🎓 Kurslar']), IsAdmin())
async def admin_course_handler(message: types.Message, state: FSMContext, _, locale: str):
    keyboards = [
        {
            "uz": "Course1 uz",
            "ru": "Course1 ru",
            "en": "Course1 en",
        },
        {
            "uz": "Course2 uz",
            "ru": "Course2 ru",
            "en": "Course2 en",
        },
        {
            "uz": "Course3 uz",
            "ru": "Course3 ru",
            "en": "Course3 en",
        },
        {
            "uz": "Course4 uz",
            "ru": "Course4 ru",
            "en": "Course4 en",
        }
    ]

    text = _("All courses list")

    keyboard = KeyboardButton(text=_("Add new course"))
    reply_markup = await dynamic_reply_keyboard_builder(
        keyboards=keyboards, _=_, locale=locale,
        extra_keyboards=[keyboard]
    )
    await message.answer(text=text, reply_markup=reply_markup)
