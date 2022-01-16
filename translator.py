#### Import libraries ####
import speech_recognition as sr
from gtts import gTTS
import playsound
import translators as ts
import os 


#### Text to Speech / Speech to Text ####

## Convert english speech into text
def mily_listen_en():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        
        r.adjust_for_ambient_noise(source, duration=0.2)

        audio = r.listen(source)

        text = r.recognize_google(audio, language = 'en')

    text = text.lower()

    return text

## Convert spanish speech into text
def mily_listen_es():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        
        r.adjust_for_ambient_noise(source, duration=0.2)

        audio = r.listen(source)

        text = r.recognize_google(audio, language='es-PE')

    text = text.lower()

    return text  

## Convert english text to speech
def mily_talk_en(text):

    # create audio file
    file_name = 'audio_data.mp3'
    # transform file to speech
    tts = gTTS(text = text, lang = 'en')
    # save file
    tts.save(file_name)

    # play file
    playsound.playsound(file_name)

    #remove audio file
    os.remove(file_name)


## Convert spanish text to speech
def mily_talk_es(text):

    # create audio file
    file_name = 'audio_data.mp3'
    # transform file to speech
    tts = gTTS(text = text, lang = 'es')
    # save file
    tts.save(file_name)

    # play file
    playsound.playsound(file_name)

    #remove audio file
    os.remove(file_name)


#### Translation functions ####
## Spanish to English
def translator_es_en(text):

    mily_talk_en(ts.google(text, from_language='es', to_language='en'))

## English to Spanish
def translator_en_es(text):

    mily_talk_es(ts.google(text, from_language='en', to_language='es'))

# Reply function
def mily_reply(text):

    if 'translate' in text:

        while True:

            mily_talk_en('I will choose the right translator for you. Please tell me the source language and target language')
            source_target_lang = mily_listen_en()
            print(source_target_lang)

            if 'english to spanish' in source_target_lang:
                mily_talk_en('Got it, you need to translate from English to Spanish. Please tell me what do you need to translate')
                while True:
                    text_to_translate = mily_listen_en()
                    print(text_to_translate)

                    if text_to_translate != 'switch translator':
                        translator_en_es(text_to_translate)
                    else:
                        break

            elif 'spanish to english' in source_target_lang:
                mily_talk_es('Ok, Necesitas traducir de espanol a ingles. Dime que necesitas traducir')
                while True:
                    text_to_translate = mily_listen_es()
                    print(text_to_translate)

                    if text_to_translate != 'cambia traductor':
                        translator_es_en(text_to_translate)
                    else:
                        break

            elif 'turn off translator':
                mily_talk_en('It was a pleasure to translate for you. Have a nice day')
                break

            else:
                mily_talk_en('Sorry, I did not get what you said')

        else:
            mily_talk_en('Sorry, I cannot support that')


# Code run
def mily_run():
    mily_talk_en('Hi, I am Milagros. What is your name?')
    listen_name = mily_listen_en()
    mily_talk_en('Hi' + listen_name + ', how can I help you?')

    listen_assistant = mily_listen_en()
    print(listen_assistant)

    mily_reply(listen_assistant)

mily_run()



# Test & Prep

#i = mily_talk_es('Hola, tia Mily, anticuchos?')

#print(i)

#x = ts.google('How are you?', from_language='auto', to_language='es')
#print(x)