#sentiment analysis
from textblob import TextBlob
positive = 0
negative = 0
neutral = 0
#store messages 
history = []

name = input("What's your name?").strip()
print(f"\n Hi {name}! Type something and I'll tell you the sentiment")
print("\n commands:summary,history,reset,exit\n")

while True:
    message = input(f"\n {name}:").strip()
    if not message:
        print("Please write something")
        continue
    if message.lower() == "exit":
        print(f"Goodbye {name}!")
        break
    elif message.lower() == "summary":
        print("\n summary report:")
        print(f"positive:{positive}")
        print(f"negative:{negative}")
        print(f"neutral:{neutral}")
    elif message.lower() == "history":
        if history:
            print("\n history details:")
            for i, msg in enumerate(history,start=1):
                print(f"{i}. {msg}")
        else:
            print("no messages yet")
    elif message.lower() == "reset":
        positive = negative = neutral = 0
        history.clear()
        print("data resestted")
    else:
        blob = TextBlob(message)
        score = blob.sentiment.polarity
        history.append(message)
        if score > 0.25:
            print("that sounds positive")
            positive += 1
        elif score <-0.25:
            print("that sounds negative")
            negative += 1
        else:
            print("that feels neutral")
            neutral += 1 