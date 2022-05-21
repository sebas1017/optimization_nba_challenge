from pydantic import BaseModel
from typing import List
class UserRequestModel(BaseModel):
    height_target: int