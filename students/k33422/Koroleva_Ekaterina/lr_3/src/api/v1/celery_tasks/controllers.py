from typing import Annotated

from fastapi import (APIRouter, Body, Depends, Path)

from celery_worker.app import parse as celery_parse
from .schemes import (TaskRequest, TaskResponse)

router = APIRouter(prefix='/celery', tags=['Celery'])


@router.post('/parse', response_model=Annotated[TaskResponse, Depends()])
async def parse(url: Annotated[TaskRequest, Body()]):
    task = celery_parse.delay(url.url)
    return TaskResponse(id=task.id, status='PENDING')


@router.get('/check/{pk}', response_model=Annotated[TaskResponse, Depends()])
async def check(pk: Annotated[str, Path()]):
    task = celery_parse.AsyncResult(pk)
    return TaskResponse(id=task.id, status=task.status)


@router.get('/result/{pk}')
async def result(pk: Annotated[str, Path()]):
    task = celery_parse.AsyncResult(pk)

    return {'data': task.result}
