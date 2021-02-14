#import message_activity
#from message_activity import *
#from messages import show_messages
#from messages import sent_messages as sent
messages = ["Whats up?", "What are you up to?", "Wanna go out tonight?", "Good Night!"]

def show_messages(messages):
    for message in messages:
        print(message)

show_messages(messages)

new_messages = []
#message_activity.show_messages(messages)
#message_activity.sent_messages(messages, new_messages)
#sent(messages, new_messages)
def sent_messages(messages, new_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending message now: {current_message}")
        new_messages.append(current_message)

sent_messages(messages.copy(), new_messages)

for message in messages:
    print("Old Messages: ", message)

for message in messages:
    print("Sent Messages: ", message)