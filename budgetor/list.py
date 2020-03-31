#!/usr/bin/python3
from datetime import datetime
import json

""" This program will allow me to set tasks
    and record moments and acheivements

    GOAL: turn into a small app in flutter
    create a temp file for the json

"""


class event():
    def __init__(self, name="", sumofev="", timeofev="", typofev="", complete=""):
        self.id = 0
        self.types = ""
        self.nameOfEvent = ""
        self.create_at = datetime.now()
        self.create_at = self.create_at.strftime("%d/%m/%Y %H:%M:%S")
        self.summaryEvent = ""  # input("What is the summary of this event?")
        self.timeOfEvent = ""  # input("What was the time of the event")
        self.completed = ""

    def __str__(self):
        s = self
        i = s.id
        t = s.types
        noe = s.nameOfEvent
        ca = s.create_at
        se = s.summaryEvent
        toe = s.timeOfEvent
        c = s.completed
        str = '[{}] ({})-|{}|+|{}|=|{}|'.format(noe, t, toe, se, c)


def Types():
    types = ["task", "completed_tasks", "achievements", "general"]

    run = False
    while (run is False):
        t = input("Input type of Journal or T to see type!\n- ")
        if t == 'T':
            print("Types are", end=" ")
            for i in types:
                print("{}".format(i), end=", ")
            print(".")

        elif t in types:
            return t


def Create():
    types = Types()
    name = input("Input name of {}: ".format(types))
    toe = input("Enter Date in (dd-mm-yyyy) format: ")
    summary = input("Write a summery for event: ")
    # complete - soon boolen
    completed = input("Completed (y or n): ")
    new_event = event(name, summary, toe, types, completed)
    print(new_event)


def View():
    pass


def Journal():
    play = True
    while (play):

        # input for option
        choice = input("c = create a tasks or events | v to view events or tasks | q to quit:\n- ")

        # similar to an array of structs
        switcher = {
            'c': Create,
            'v': View
        }

        if choice == 'q':
            play = False
            print("good bye lone ranger...")
        elif choice in switcher:
            switcher[choice]()
        else:
            print("You can't pick that buddy :|")
            continue


Journal()
