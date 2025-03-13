
from app.infrastructure import settings
from app.infrastructure.delivery_strategies.mail_delivery_strategy import MailDeliveryStrategy
from app.infrastructure.delivery_strategies.slack_delivery_strategy import SlackDeliveryStrategy


def build_delivery_strategies():
   return {'Pricing' : MailDeliveryStrategy(settings.mail_delivery_settings()),
           'Sales' : SlackDeliveryStrategy(settings.slack_delivery_settings())}