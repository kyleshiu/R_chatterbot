from chatterbot import ChatBot
chatterbot = ChatBot("DinDin")
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.comparisons import levenshtein_distance
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import tempfile
import time
import os

#******************************************* chatbot設定 ******************************************#

chatterbot = ChatBot(
    'DinDin',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=
        [{
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_most_frequent_response"
            # 'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            # 'threshold': 0.65,
            # 'default_response': 'I am sorry, but I do not understand.'
        }],
    input_adapter='chatterbot.input.VariableInputTypeAdapter',
    output_adapter="chatterbot.output.OutputAdapter",
    output_format="text",
    # response_selection_method='get_most_frequent_response',
    # filters=['chatterbot.filters.RepetitiveResponseFilter'],
    # preprocessors=['chatterbot.preprocessors.clean_whitespace','chatterbot.preprocessors.unescape_html'],
    database='chatterbot-database')

print('Speak something to begin...')

#********************************************* training ******************************************#

chatterbot.set_trainer(ChatterBotCorpusTrainer)
chatterbot.train("chatterbot.corpus.chinesezh_tw")
chatterbot.trainer.export_for_training('./my_export.json')

chatterbot.set_trainer(ListTrainer)

#*********************************************** 語音 *********************************************#

# def Speech(input):
#     with tempfile.NamedTemporaryFile(delete=True) as fp:
#         tts = gTTS(text=input, lang='zh-tw', slow= False)
#         tts.save('{}.mp3'.format(fp.name))
#         playsound('{}.mp3'.format(fp.name))

# def Recognizer():
#     print('Please Speak')
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         voice = r.listen(source)
#         userSpeech = r.recognize_google(voice)
#         print(userSpeech)
#         return userSpeech

#*********************************************** 顯示 *********************************************#

while True:
    try:
        #request=Recognizer()
        request= input('you:')
        # print('You:',request)
        bot_input = chatterbot.get_response(request)
        if (bot_input == '好, 馬上幫你查一下,以下是 (可樂) 的地點'):
            print('可樂Func')
        else:
            print('DinDin:', bot_input)
        # Speech(bot_input)
        # print('DinDin:', bot_input)
              
    except:
        print('請換個方式讓我理解')
