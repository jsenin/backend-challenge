from app.domain.delivery_strategies.mail_delivery_strategy import MailDeliveryStrategy
from app.domain.delivery_strategies.slack_delivery_strategy import SlackDeliveryStrategy


def build_delivery_strategies():
   return {'Pricing' : MailDeliveryStrategy(), 'Sales' : SlackDeliveryStrategy()}