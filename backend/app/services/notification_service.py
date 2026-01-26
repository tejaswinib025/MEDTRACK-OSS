from typing import List
from app.notifications.base import BaseNotificationProvider
from app.notifications.email_provider import EmailProvider
from app.notifications.sms_provider import SMSProvider

class NotificationService:
    def __init__(self):
        self.providers: List[BaseNotificationProvider] = [
            EmailProvider(),
            SMSProvider()
        ]

    async def send_reminder(self, user_email: str, medication_name: str):
        message = f"Reminder: It's time to take your {medication_name}."
        for provider in self.providers:
            await provider.send(user_email, message)

notification_service = NotificationService()
