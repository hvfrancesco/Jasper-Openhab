# -*- coding: utf-8-*-

# cambiare 'utente' e 'password' secondo il proprio settaggio di Openhab

import re
import requests

INTENTS = ['per favore', 'comando', 'please', 'control', 'prego']
# Required by brain.py
WORDS = INTENTS

PRIORITY = 3

def handle(text, mic, profile):
	mic.say("Cosa posso fare per lei " + profile['first_name'] + " ?")
	comando = mic.activeListen()
	mic.say("eseguo " + str(comando).lower())
	
	string = "http://localhost:8080/CMD?VoiceCommand=" + str(comando).lower()
	r = requests.get(string, auth=('utente', 'password')) 
	print r.status_code


def isValid(text):
	return bool(re.search(r'\bper favore|comando|please|control|prego\b', text, re.IGNORECASE))
