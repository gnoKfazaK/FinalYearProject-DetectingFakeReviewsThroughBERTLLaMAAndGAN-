from flask import Flask, request, jsonify
from BERT import BERTClassifier, BERTClass
import torch

model_path = '../best_model.pt'

app = Flask(__name__)

def classifier(text):
    isBot, score = BERTClassifier(model, text)
    result = f"Bot Comment ({score * 100})" if isBot else f"Genuine Comment ({(1 - score) * 100})"
    print(result)
    return result

def loadBERTmodel():
    model = BERTClass()
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model.load_state_dict(torch.load(model_path, map_location=device)['state_dict'])
    print("BERT model loaded sucessfully")
    return model

@app.route('/classifier/<comment>', methods = ['GET', 'POST'])
def classification(comment):

    print('input:' + comment)
    reply = classifier(comment)
    print('output:' + reply)
    return reply

if __name__ == '__main__':
    print("Bot starting")
    model = loadBERTmodel()
    app.run(debug = True, host = "127.0.0.1", port = '5000')