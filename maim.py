import json, pyaudio
from multiprocessing.connection import answer_challenge
from vosk import Model, KaldiRecognizer
import sys
import webbrowser
import random
import datetime
import os
import speech_recognition as sr
import wikipedia
import pyscreenshot
import  pytesseract
from PIL import Image
import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox
import ctypes
import re
import os
import datetime
import pyglet
from time import sleep

def lll():
   print('привет я камилла голосовой помошник\nменя создавал камиль ему 15 лет\nя создавалась обсалютно без вдожений\nесли вы хотите мемя поддержать вот мой крипто кошелек\n0x18c232a8b0f160d89e22f3afd2dc38c83553f43f')
#ответы на не сложные диологи,в exe

ur2 = 'https://www.youtube.com/'
url = 'https://www.youtube.com/'
url3 = 'https://www.google.com/search?q=курс+'
url4 = 'https://www.google.com/search?q=как+сделать'
url41 = 'https://www.google.com/search?q=расскажи+о'
music = pyglet.resource.media('music.mp3')
time_now = datetime.datetime.now()
now = datetime.datetime.now()
anekdot = ["чем негр похож на вилосепед оба не могут работать без цепи", 
"Здравствуйте, нужен проверенный электрик, можете кого-нибудь посоветовать? Конечно могу! Любой живой электрик автоматически считается проверенным.", 
"Что должна была сделать настоящая, уважающая себя женщина 14 февраля? Правильно, выводы.", 
"Фрезеровщик Фёдор знал, что семь это счастливое число, но семь пальцев на руках не вселяли в него оптимизма.", 
"Халяльных ресторанов мало, а халявных нет вообще...", 
"У Буратино была кожаная куртка, из бересты",
"Погружаться в полную анархию и дикий хаос нужно под чьим-нибудь чутким руководством."]
chetati= ["Люди-идиоты плюс алкоголь — вот вам рецепт любой потасовки",
"Тем, кого вдохновляют мои герои, не помешало бы лишний раз подумать","Женщины у вас потрясающие! Безусловно. В России встречаются просто убойные красотки",
"Люди, считающие, что деньги способны сделать все, сами способны все сделать за деньги",
"Я полагаю, что европейцы опасны и волосаты",
"Превосходство — это когда есть на что насрать, и есть чем",
"Есть такая штука как «Двигаться дальше». Попробуйте, поможет",]
kak_dela = ["хорошо у вас?","превасходно","супер","отлично","все хорошо вот жду вашей команды",]
chto_delaech = ["ничего жду вашей команды","жду вашей команды","ничего особенного просто анализирую ваши последние запросы","ничего особенного","да так жду вашей команды",]
privet = ["салют","алоха","салам","приветик","hi","привет","алоха","бонжур","добрый вечер ну или если можно так сказать","здарова","че как","ку","привки","саламчик попалпмчик","и вам не тухнкть"]
model = Model ('vosk-model-small-ru-0.4')
rec = KaldiRecognizer (model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input= True, frames_per_buffer=8000)
stream.start_stream()
wikipedia.set_lang("ru")

def ddd():
    if text == "что здесь написанно":
       image = pyscreenshot.grab()
       image.save('sss.png')
       img = Image.open('sss.png')
       pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Камильчик\Documents\ntcthfrn\tesseract.exe'
       texty = pytesseract.image_to_string(img)
       print(texty)
def command():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Говорите")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
	try: 
		zadanie = r.recognize_google(audio, language="ru-RU").lower()
		print("Вы сказали: " + zadanie)
	except sr.UnknownValueError:
		print("Я вас не поняла")
		zadanie = command()
	return zadanie


def my_fun():
    if text == 'камилла открыткрой ' :
            webbrowser.open(url)
    if text == 'камилла расскажи анекдот':
        random_index = random.randint(0, len(anekdot) - 1)
        print(anekdot[random_index])
    if text == 'камилла расскажи цитату':
        random_index = random.randint(0, len(chetati) - 1)
        print(chetati[random_index])
    if text == 'привет':
        random_index = random.randint(0, len(privet) - 1)
        print(privet[random_index])
    if text == 'как дела':
        random_index = random.randint(0, len(kak_dela) - 1)
        print(kak_dela[random_index])
    if text == 'что делаешь':
        random_index = random.randint(0, len(chto_delaech ) - 1)
        print(chto_delaech [random_index])
    if text == 'расскажи о себе':
        lll()
    if text == 'у меня тоже':
        print("отлично")


def ggg():
    url1 = 'https://music.yandex.ru/search?text='
    
    if text == 'камилла давай послушаем':
        print('что')
        webbrowser.open(url1 + command())
    if text.count("что такое") > 0:
            result = wikipedia.summary(text.replace("что такое", ""))
            print(result)
    if text.count("кто такие") > 0:
            result = wikipedia.summary(text.replace("что такое", ""))
            print(result)
    if text.count("расскажи о") > 0:
            webbrowser.open(url41 + command())
    if text == 'как сделать':
         print('что же')
         webbrowser.open(url4 + command())
    if text == 'камилла включи ютуб':
        print('хорошо')
        webbrowser.open(ur2)
    if text == 'камилла курс валют':
        print('какой валюты')
        webbrowser.open(url3 + command())
    if text == 'камилла заметки':
         pass
    if text == 'редактор кода':
        print('действуй')
        from wert import rgb
        rgb()
    if text == 'будильник':
         from rer import idfs
         idfs()


def listen():
  while True:
   data = stream.read(4000, exception_on_overflow= False)
   if (rec.AcceptWaveform(data)) and (len(data) > 0 ):
    answer = json.loads(rec.Result())
    if answer ['text']:
        yield answer['text']
        my_fun()
        ggg()
        ddd()
for text in listen():
         print(text)