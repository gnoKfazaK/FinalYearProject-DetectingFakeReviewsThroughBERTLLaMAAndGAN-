from telegram import Update
from telegram.ext import *
import telepot
from telepot.loop import MessageLoop
from BERT import BERTClassifier, BERTClass
import time
import torch

NEED_TO_TYPE_COMMAND_EVERYTIME = False
API_TOKEN = 'IWONTELAKMYAPITOKENTHISTIME!'
model_path = '../best_model.pt'

def classifier(text):
    isBot, score = BERTClassifier(model, text)
    result = f"Bot Comment ({score * 100})" if isBot else f"Genuine Comment ({(1 - score) * 100})"
    print(result)
    return result

def generator(text):
    return "Not finish"

def loadBERTmodel():
    model = BERTClass()
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model.load_state_dict(torch.load(model_path, map_location=device)['state_dict'])
    print("BERT model loaded sucessfully")
    return model

# Message handler to process text input
def handle_text(msg):
    chat_id = msg['chat']['id']  # Get the chat ID from the message
    command = msg['text']  # Get the text of the message

    print('Received:', command)  # Print the received command

    if command == '/classi':
        bot.sendMessage(chat_id, "You have selected classification. Please enter text for classification:")
        # Store state if needed (optional)
        user_states[chat_id] = 'waiting_for_classification_input'
        
    elif command == '/gen':
        bot.sendMessage(chat_id, "You have selected generation. Please enter text for generation:")
        # Store state if needed (optional)
        user_states[chat_id] = 'waiting_for_generation_input'
        
    elif chat_id in user_states:
        if user_states[chat_id] == 'waiting_for_classification_input':
            result = classifier(command)  # Process the input for classification
            bot.sendMessage(chat_id, result)
            if NEED_TO_TYPE_COMMAND_EVERYTIME:
                del user_states[chat_id]  # Clear state after processing
            
        elif user_states[chat_id] == 'waiting_for_generation_input':
            result = generator(command)  # Process the input for generation
            bot.sendMessage(chat_id, result)
            if NEED_TO_TYPE_COMMAND_EVERYTIME:
                del user_states[chat_id]  # Clear state after processing
            
    else:
        bot.sendMessage(chat_id, "Unknown command. Please use /classi or /gen.")

if __name__ == '__main__':
    user_states = {}
    bot = telepot.Bot(API_TOKEN)
    print("Bot starting")
    model = loadBERTmodel()
    MessageLoop(bot, handle_text).run_as_thread()
    print('Listening...')

    while True:
        time.sleep(10)

    



