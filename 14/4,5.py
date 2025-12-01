import os
import re

os.chdir(os.path.dirname(__file__))

def _load_email():
    with open('email.txt', encoding='utf-8') as f:
        return f.read()

def email_sender():
    text = _load_email()
    m = re.search(r'From:.*?<(.+?)>', text)
    return m.group(1)

def email_recipient():
    text = _load_email()
    m = re.search(r'To:.*?<(.+?)>', text)
    return m.group(1)

def email_subject():
    text = _load_email()
    m = re.search(r'^Subject: (.+)$', text, re.MULTILINE)
    return m.group(1)

def email_body():
    text = _load_email()
    m = re.search(r'\n\n(.*)', text, re.DOTALL)
    return m.group(1)

print(email_sender())
print(email_recipient())
print(email_subject())
print(email_body())