import nltk
import random
import time
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Emotion-based responses
responses = {
    "sad": [
        "I'm really sorry you're feeling like this. You're not alone 🤗.",
        "It's okay to feel sad sometimes. I'm here for you 💙.",
        "Sending you virtual hugs. You matter 💛."
    ],
    "anxious": [
        "Take a deep breath 🧘. Let's go step by step — you got this!",
        "Anxiety can be tough, but you're stronger than you feel 💪.",
        "You're doing your best, and that’s enough 🌈."
    ],
    "happy": [
        "Yay! What made you feel happy today? 🌟",
        "That's great to hear! Keep smiling 😄.",
        "I love that energy! Spread the joy 🎉."
    ],
    "birthday": [
        "🎉 That’s wonderful! Wishing you a very Happy Birthday in advance! 🎂",
        "Hope your birthday is full of joy and cake! 🎈"
    ],
    "default": [
        "Hmm, I'm listening... want to tell me more?",
        "I'm here for you. Can you describe how you're feeling in another way?",
        "Let’s talk it through. How’s your day going so far?"
    ]
}

# Self-care tips
tips = [
    "🌞 Take a walk in the sun today!",
    "📖 Read something you enjoy.",
    "🎧 Listen to calming music.",
    "💧 Don’t forget to drink water!",
    "📝 Try journaling your thoughts!"
]

# Emotion detection logic
def detect_emotion(user_input):
    user_input = user_input.lower()
    words = user_input.split()
    lemmas = [lemmatizer.lemmatize(word) for word in words]

    if any(word in lemmas for word in ["sad", "depressed", "unhappy"]):
        return "sad"
    elif any(word in lemmas for word in ["anxious", "nervous", "worried", "stressed"]):
        return "anxious"
    elif any(word in lemmas for word in ["happy", "joyful", "excited", "glad"]):
        return "happy"
    elif "birthday" in lemmas:
        return "birthday"
    else:
        return "default"

# Bot typing effect
def bot_reply(text):
    print("🤖 Mental Health Bot is typing...", end="\r")
    time.sleep(1.2)
    print("🧠 Mental Health Bot:", text)

# Start chatbot
print("🧠 Mental Health Bot: Hey there! I'm here for you 💬")
print("🧠 How are you feeling today? 😊 (e.g., happy, sad, anxious, tired)")
print("🧠 Just type how you feel and I’ll respond. Type 'exit' to leave anytime.")

counter = 0

while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        bot_reply("Take care of yourself. You're doing great! 💙")
        break
    emotion = detect_emotion(msg)
    bot_reply(random.choice(responses[emotion]))
    counter += 1

    # Show self-care tip every 2 chats
    if counter % 2 == 0:
        bot_reply("🧘 Self-care tip: " + random.choice(tips))

