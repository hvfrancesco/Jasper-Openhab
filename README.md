This is an home automation simple Jasper module that connects to an Openhab server and passes voice commands to trigger OpenHab events.
It is provided for Italian (the one I use on my own house= and for English, and being very simple can be customized for any language.

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
