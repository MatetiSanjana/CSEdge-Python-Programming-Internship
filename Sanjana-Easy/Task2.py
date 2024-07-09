import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')
#creating questions and answers 
s=[
 [
    r"Hello|Hi|Hey",
    ["Hello,How are you?"]
 ],
 [
    r"I'm fine",
    ["Glad to hear that,how can i help you?"]
 ],
 [
    r"What is your name?",
    ["well they haven't kept me a name but they call me as a chatbot ,if you wish u can give me a name"]
 ],
 [
    r"Actually I'm feeling a bit lonely|sad|angry|irritated today",
    ["sorry to hear about that.I'm here for you! Would you like to share about what's on your mind?"]
 ],
 [
    r"Yeah well that was a big problem, i can't get rid off it",
    ["I'm really sorry to hear about that you are going through a tough time.It's okay to feel overwhelmed by problems sometimes but dont worry that you are not at all alone!"]
 ],
 [
    r"Can you try to say something lie a joke or entertain me?",
    ["Sure,I can definitely change your mood!So,how about this:Why maths book look sad?Because it had any problems!I hope that this brought a little smile to your face!"]
 ],
 [
    r"Thanks a lot for helping me",
    ["You're Welcome!I'm always here for you at anytime,if you need a chat or joke or anything,feel free to ask me"]
 ],
 [
    r"Exit",
    ["It was my pleasure to help you.Please,come again!"]
 ]
]
#default message for starting chat
print("Please,write anything to start the chat")
#create a chat instance
chatbot=Chat(s)
#start conversation
chatbot.converse()