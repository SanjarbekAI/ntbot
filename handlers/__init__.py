from aiogram import Router

from . import admin_courses
from . import start


def include_routers():
    main_router = Router()
    main_router.include_router(start.router)
    main_router.include_router(admin_courses.router)

    return main_router
