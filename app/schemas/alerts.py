# app/schemas/alerts.py

from pydantic import BaseModel

class AlertBase(BaseModel):
    message: str
    user_id: int  # The user related to the alert

class AlertResponse(AlertBase):
    id: int

    class Config:
        from_attributes = True

class NotificationSchema(BaseModel):
    title: str
    message: str
    user_id: int  # The user related to the notification

    class Config:
        from_attributes = True
