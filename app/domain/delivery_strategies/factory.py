from app.domain.delivery_strategies.mail_delivery_strategy import MailDeliveryStrategy
from app.domain.delivery_strategies.slack_delivery_strategy import SlackDeliveryStrategy
from app.infrastructure import settings


def build_delivery_strategies():
   return {'Pricing' : MailDeliveryStrategy(settings.mail_delivery_settings()),
           'Sales' : SlackDeliveryStrategy(settings.slack_delivery_settings())}