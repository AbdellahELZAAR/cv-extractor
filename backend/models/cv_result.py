from pydantic import BaseModel
from typing import Optional

class CVResult(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    degree: Optional[str]
