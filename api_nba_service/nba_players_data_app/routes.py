import sys

from pip import main
from fastapi import APIRouter, Response
from .constants import final_response_error_parameters
from .schemas import UserRequestModel

sys.path.append('..')
from functions.functions_app import main_calculus



router = APIRouter(
    prefix='/api/v1',
    tags=["nba players"]
)


@router.post("/find_heights_nba")
async def all_properties(user:UserRequestModel,response:Response):
    if user.height_target <= 0:
        response_final = final_response_error_parameters
    else:
        response_final = main_calculus(user.height_target)
        
    return {"results":response_final}