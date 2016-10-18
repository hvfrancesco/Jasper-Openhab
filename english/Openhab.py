# -*- coding: utf-8-*-

# change 'user' and 'password' according to
# your Openhab settings, you may want to check
# the url and port of the Openhab server too

'''
This Jasper module connects to an Openhab server, using openhab
voice-control features in order to trigger openhab events by voice
commands.
In order for it to work you must have added a 'VoiceCommand' String item
to your Openhab configuration, and the corresponding rules to process the
VoiceCommand inputs.

Have a look at this wiki article for help and reference:
https://github.com/openhab/openhab/wiki/Controlling-openHAB-with-your-voice

When Jasper hears a keyword belonging to this module, it asks you what action you
want to perform, and you must answer with a phrase that triggers the action as set
in the openhab rules. Jasper simply passes the command to openhab via REST interface
and this gets processed by Openhab itself.
This way the voice control process is the same
using Jasper and Habdroid application for example.
'''

import re
import requests

INTENTS = ['command', 'please', 'control', 'home']
# Required by brain.py
WORDS = INTENTS

PRIORITY = 3

def handle(text, mic, profile):
	mic.say("What can I do for you " + profile['first_name'] + " ?")
	action = mic.activeListen()
	mic.say("I am doing " + str(action).lower())
	
	string = "http://localhost:8080/CMD?VoiceCommand=" + str(action).lower()
	r = requests.get(string, auth=('user', 'password')) 
	print r.status_code


def isValid(text):
	return bool(re.search(r'\bcommand|please|control|home\b', text, re.IGNORECASE))
