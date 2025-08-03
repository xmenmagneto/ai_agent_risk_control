from pydantic import BaseModel

class BlacklistCheckInput(BaseModel):
    user_id: str

class UserProfileInput(BaseModel):
    user_id: str