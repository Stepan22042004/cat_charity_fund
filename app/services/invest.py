
from datetime import datetime
from fastapi import Depends

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session

from app.models import Donation, CharityProject


async def invest_new_donation(
        donation: Donation,
        session: AsyncSession = Depends(get_async_session)
):

    projects = await session.execute(
        select(CharityProject).order_by(CharityProject.create_date).where(
            CharityProject.fully_invested == 0
        )
    )
    charity_projects = projects.scalars().all()
    now = datetime.now()
    for project in charity_projects:
        available_investment = project.full_amount - project.invested_amount
        investment = min(
            available_investment,
            donation.full_amount - donation.invested_amount
        )
        project.invested_amount += investment
        if project.invested_amount == project.full_amount:
            project.fully_invested = True
            project.close_date = now
        donation.invested_amount += investment
        print(project.invested_amount, 'ok')
        if donation.invested_amount >= donation.full_amount:
            donation.fully_invested = True
            donation.close_date = now
            break

    await session.commit()
    await session.refresh(donation)


async def invest_to_new_project(
        project: CharityProject,
        session: AsyncSession = Depends(get_async_session)
):
    donations = await session.execute(
        select(Donation).order_by(Donation.create_date).where(
            Donation.fully_invested == 0
        )
    )
    donations = donations.scalars().all()
    now = datetime.now()
    for donation in donations:
        available_investment = project.full_amount - project.invested_amount
        investment = min(
            available_investment,
            donation.full_amount - donation.invested_amount
        )
        project.invested_amount += investment
        donation.invested_amount += investment

        if donation.invested_amount >= donation.full_amount:
            donation.fully_invested = True
            donation.close_date = now
        if project.invested_amount == project.full_amount:
            project.fully_invested = True
            project.close_date = now
            break
    await session.commit()
    await session.refresh(project)