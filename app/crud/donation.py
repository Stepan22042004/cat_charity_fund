from app.models.donation import Donation
from app.crud.base import CRUDBase


donation_crud = CRUDBase(Donation)
