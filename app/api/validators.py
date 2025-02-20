from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charityproject import charity_project_crud
from app.crud.charityproject import charity_project_crud


async def check_project_same_name(name: str,
                                  session: AsyncSession):
    result = await charity_project_crud.get_by_name(name, session)
    if result:
        raise HTTPException(
            status_code=400,
            detail=f"Объекты с именем '{name}' уже существуют"
        )


async def check_project_new_full_amount(charity_project_id: int,
                                        new_full_amount: int,
                                        session: AsyncSession):
    charity_project = await charity_project_crud.get(
        charity_project_id,
        session
    )
    if new_full_amount and charity_project:
        if new_full_amount < charity_project.invested_amount:
            raise HTTPException(
                status_code=400,
                detail="Целевая сумма меньше набранной."
            )


async def check_project_delete_already_invested(charity_project_id: int,
                                                session: AsyncSession):
    charity_project = await charity_project_crud.get(
        charity_project_id,
        session
    )
    if charity_project:
        if charity_project.invested_amount > 0:
            raise HTTPException(
                status_code=400,
                detail="Нельзя удалять проекты с набранной суммой денег."
            )
