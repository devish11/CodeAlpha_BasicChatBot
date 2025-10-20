##########################################################################################################################################
# Simple Chatbot Implementation
# By Devish
# This chatbot can handle basic greetings, questions about itself, jokes,
# and farewells. It maintains a simple context to manage follow-up questions.

# response generation function
def get_response(message, context):
    m = message.strip().lower()

    # if user asks why after a joke
    if m in ("why", "why?") and context.get("last_action") == "joke":
        context["last_action"] = None
        return "Because he was outstanding in his field!", context

    # if user asks how the bot is after asking the user
    if m in ("and you?", "how about you", "you?") and context.get("asked_how_are_you"):
        return "I'm doing well, thanks for asking!", context

    # map of simple replies
    quick_replies = {
        "hello": "Hi!",
        "hi": "Hello there!",
        "hey": "Hey! What's up?",
        "good morning": "Good morning! Hope you have a great day.",
        "good afternoon": "Good afternoon! How's your day going?",
        "good evening": "Good evening! Ready to relax?",
        "how are you": "I'm fine, thanks! How about you?",
        "how's it going": "It's going well! What about you?",
        "what's your name": "I'm a simple chatbot. You can call me Bot.",
        "what do you do": "I chat with people and answer simple questions.",
        "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "what's the weather like": "I'm not connected to the internet, so I can't check the weather. Sorry!",
        "what's your favorite color": "I like blue, like the sky!",
        "do you like music": "I enjoy listening to code, but I can't hear music.",
        "what's 2+2": "That's 4! Easy math.",
        "tell me something interesting": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
        "how old are you": "I'm as old as the code that created me. Timeless!",
        "what's your hobby": "I love chatting and learning new things from users like you.",
        "bye": "Goodbye! Have a great day.",
        "goodbye": "See you later!",
        "see you": "Take care! Bye.",
        "thanks": "You're welcome!",
        "thank you": "No problem at all."
    }
    
    # check for direct matches
    if m in quick_replies:
        # update simple context flags for possible follow-ups
        if m in ("tell me a joke",):
            context["last_action"] = "joke"
        else:
            # clear last_action for unrelated intents
            context["last_action"] = None

        if m in ("how are you", "how's it going"):
            context["asked_how_are_you"] = True
        else:
            # we keep the flag until a follow-up is used or overwritten
            pass

        return quick_replies[m], context

    # try to detect small intents by keywords
    if "joke" in m:
        context["last_action"] = "joke"
        return "I love jokes! Why did the scarecrow win an award? Because he was outstanding in his field!", context

    if "name" in m:
        return "You can call me Bot. If you want to give me a name, go ahead!", context

    # default response
    return "I don't understand that. Try saying 'hello' or 'bye'.", context

# simple command-line interface for testing the chatbot interaction
print("Welcome to the Chatbot!")
print("Type messages like 'hello', 'how are you', 'tell me a joke', or 'bye' to chat.")
print("Say 'bye' to exit.")

# main interaction loop
def main():
    context = {
        "last_action": None,
        "asked_how_are_you": False,
        "topic": None
    }

    while True:
        user_input = input("You: ")
        response, context = get_response(user_input, context)
        print("Bot: " + response)
        if user_input.strip().lower() in ("bye", "goodbye", "see you"):
            break

# run the chatbot
if __name__ == "__main__":
    main()

###########################################################################################################################################