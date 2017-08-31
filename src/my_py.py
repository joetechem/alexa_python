"""
Simple Python template file allowing users to define intent resposnes (convention is lowercase
intent name from your intentsSchema and Utterances) as a function; leaving all the lambda skill
service details to the alexa_py.py file.

Intents implemented here for example:
  About
  Contact
  Upcoming

Intents supported by default (but to be filled in with your info):
  Open 
  AMAZON.HelpIntent
  AMAZON.CancelIntent or AMAZON.StopIntent


"""

import logging

# --------------- Your functions to implement your intents ------------------

def about():
    return "<speak>Welcome to Virginia Save Our Streams. A program of the Izaak Walton League of America. Virginia Save Our Streams monitors water quality of Virginia's streams and educates the public about the importance of clean water.</speak>"

def contact():
    return "<speak>The best way to reach us is at info at V. A. S. O. S. dot org.</speak>"

def upcoming():
    return "<speak>Check us out at a stream near you. We will be in the water collecting data!</speak>"


# --------------- Primary/Required functions (update as needed) ------------------

def launch():
    """ Called when the user launches the skill without specifying what they want
    """

    return "<speak>Welcome to the 411 for Virginia Save Our Streams. This skill provides information about V. A. S. O S., a program of the Isaak Walton League of America.</speak>"


def help():
    """ Called when the user asks for help
    """

    return "<speak>This skill provides some basic information about V. A. S. O. S. You can ask for our location, contact info, and upcoming events.</speak>"


def end():

    return "<speak.Thank you for asking about our organzization. Have a nice day! </speak>"

