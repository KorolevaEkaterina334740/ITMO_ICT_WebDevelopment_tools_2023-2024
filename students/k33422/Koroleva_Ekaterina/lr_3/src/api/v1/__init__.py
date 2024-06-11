from fastapi import APIRouter

from .auth import auth_router
from .celery_tasks import celery_tasks_router
from .trips import trips_router
from .users import users_router

router = APIRouter(prefix='/v1')

router.include_router(auth_router)
router.include_router(users_router)
router.include_router(trips_router)
router.include_router(celery_tasks_router)
