import json
credentials = {}
credentials['CONSUMER_KEY'] = "jphOTAxUYfYe0xmFrWDEkCCc0"
credentials['CONSUMER_SECRET'] = "btyEWIIqSVCR8uFDzoPdm7F9yNXuSaJkx2wSEnhhxyovgRK7cH"
credentials['ACCESS_TOKEN'] = "813194346216484865-n1ZRaYXVngZ5Z86RB4q2qUUlK2WjJKy"
credentials['ACCESS_SECRET'] = "72QIwsKzTXuT8C2WrTMogfEfdlvYgYc3Dbr0Mm4npCcAm"

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)
