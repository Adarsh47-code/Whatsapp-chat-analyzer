# open the exported chat with friend 
with open("Put your own file here", "r", encoding="utf-8") as c:
    chat_data = c.readlines()


messages = []
for line in chat_data:
    if " - " in line: #whatsapp format check
        parts = line.split("-", 1)
        timestamp = parts[0]
        if ":" in parts[1]:
            sender, message = parts[1].split(":", 1)  
            messages.append((timestamp, sender, message))

from collections import Counter
senders = [msg[1] for msg in messages]
count = Counter(senders)
for sender, count in count.items():
    print(f"{sender}: {count} messages")


words = []
for timestamp, sender, message in messages:
    for word in message.split():
        words.append(word)

word_count = Counter(words)
print("Top 10 words:")
for word, count in word_count.most_common(10):
    print(f"{word} {count}")

#To check peak hours chat:
hours = [msg[0].split(",")[1].split(":")[0].strip() for msg in messages]
hourly_count = Counter(hours)

print("Peak Chatting Hours: ")
for hour, count in sorted(hourly_count.items()):
    print(f"{hour}:00 hrs -> {count} messages")
 