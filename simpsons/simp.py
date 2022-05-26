#!/usr/bin/env python3

#define the lists
challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

# define the trialpull function
def challengepull ():
    eyes1=challenge[2][1]
    goggles1=challenge[2][0]
    noth1=challenge[3]
    print("My " + eyes1 + "! The " + goggles1 + " do " + noth1 + "!")

def trialpull():
    eyes2=trial[2]["goggles"]
    goggles2=trial[2]["eyes"]
    noth2=trial[3]
    print("My " + eyes2 + "! The " + goggles2 + " do " + noth2 + "!")

def nightmarepull():
    a=nightmare[0]["user"]["name"]["first"]
    b=nightmare[0]["kumquat"]
    c=nightmare[0]["d"]
    print(f"My {a}! The {b} do {c}!")

challengepull()
trialpull()
nightmarepull()
