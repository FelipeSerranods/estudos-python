'''
Exercício - 21
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''
import time
from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
time.sleep(5)