# Landbot Backend Challenge

## Description

The product department wants a system to be notified when a customer requests assistance from a bot. The bot will make an http call (like a webhook) with the following information:

- Topic: a string with values can be sales or pricing
- Description: a string with a description of the problem that needs assistance from.

You need to expose an API endpoint that will receive this call and depending on the selected topic will forward it to a different channel:

``` 
Topic    | Channel   
----------------------
Sales    | Slack
Pricing  | Email
```

## Notes:
- Slack and Email are suggestions. Select one channel that you like the most, the other can be a mock.
- There may be more topics and channels in the future.

## The solution should:
- Be written in your favorite language and with the tools with which you feel comfortable.
- Be coded as you do daily (libraries, style, testing...).
- Be easy to grow with new functionality.
- Be a dockerized app.


## Howto

# Running
There's a Makefile to do common tasks

Start project
```bash
make up
```
It starts a fastapi server at  http://0.0.0.0:8000

Also there's a `make up-d` to start docker compose at background

Stop the project
```bash
make down
```

There's a shell quick access executing 
```
make shell
```

Run tests with 
```
make tests
```

Manual tests:
```bash
curl --request POST \
  --url http://localhost:8000/request_assistance \
  --header 'Content-Type: application/json ' \
  --data '{"topic": "Pricing", "description": "hola"}'
```

Settings are stored at  `config/config.ini`
```
[MAIL]
host = mailpit
port = 1025
user = your-email@example.com
password = your-password

[SLACK]
api_token = 12341234123

[PRICING]
mailto = pricing@landbot.io
mail_from = assistance@lanbot.io
subject = assisntace request

[SALES]
slack_channel = pricing-assistance
```

Environment values are allowed for service client configurations. If are not present, then use the config one:
```python
def mail_settings():
    smtp_server = os.getenv("MAIL_HOST") or config["MAIL"]["host"]
    smtp_port = os.getenv("MAIL_PORT") or config["MAIL"]["port"]
    username = os.getenv("MAIL_USER") or config["MAIL"]["user"]
    password = os.getenv("MAIL_PASSWORD") or config["MAIL"]["password"]

    return MailSettings(smtp_server=smtp_server, smtp_port=int(smtp_port), username=username, password=password)

def slack_settings():
    api_token = os.getenv("SLACK_API_TOKEN") or config["SLACK"]["api_token"]
    return SlackSettings(token=api_token)
```

### Mailpit
I use mailpit for e2e testing and ensure that the mails are sent 
Mailpit website is exposed at http://localhost:8025

### Release

A release docker image can be build using. It will use the git short commit to label the image version
```
make release
```