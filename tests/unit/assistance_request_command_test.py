from unittest.mock import Mock

from app.assistanace_request_command import AssistanceRequestCommand
from app.main import MailDeliveryStrategy, AssistanceRequestCommandHandler, \
     SlackDeliveryStrategy


def test_request_assistance_to_pricing_sends_and_email():
    mock_mail_strategy = Mock(spec=MailDeliveryStrategy)
    mock_slack_strategy = Mock(spec=SlackDeliveryStrategy)
    assistance_request = AssistanceRequestCommandHandler({'Pricing' : mock_mail_strategy, 'Sales' : mock_slack_strategy})

    assistance_request.handle(AssistanceRequestCommand(topic="Pricing", description="Need assistance"))

    mock_mail_strategy.send.assert_called_once_with(message="Need assistance")

def test_request_assistance_to_sales_sends_a_message_to_slack():
    mock_mail_strategy = Mock(spec=MailDeliveryStrategy)
    mock_slack_strategy = Mock(spec=SlackDeliveryStrategy)
    assistance_request = AssistanceRequestCommandHandler({'Pricing' : mock_mail_strategy, 'Sales' : mock_slack_strategy})

    assistance_request.handle(AssistanceRequestCommand(topic="Sales", description="Need assistance"))

    mock_slack_strategy.send.assert_called_once_with(message="Need assistance")
