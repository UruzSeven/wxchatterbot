#!/usr/bin/env python
# coding: utf-8

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import hug


wxchatterbot = ChatBot("wxchatterbot")
wxchatterbot.set_trainer(ChatterBotCorpusTrainer)
wxchatterbot.train("chatterbot.corpus.english")


@hug.get()
def get_response(user_input):
    response = wxchatterbot.get_response(user_input).text
    return {"response":response}