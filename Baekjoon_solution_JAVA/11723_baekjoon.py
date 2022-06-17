import sys


def add(x):
    if x not in s:
        s.append(x)


def remove(x):
    if x in s:
        s.remove(x)


def check(x):
    if x in s:
        print(1)
    else:
        print(0)


def toggle(x):
    if x in s:
        s.remove(x)
    else:
        s.append(x)


def all():
    s = []
    for i in range(1, 21):
        s.append(i)


def empty():
    s = []


cnt = int(sys.stdin.readline())
s = []



for i in range(cnt):
    commands = list(sys.stdin.readline().split())
    #print(type(command[1]))
    name = commands[0]
    try:
        num = int(commands[1])
    except:
        continue

    if name == "add":
        add(num)
    elif name == "remove":
        remove(num)
    elif name == "check":
        check(num)
    elif name == "toggle":
        toggle(num)
    elif name == "all":
        all()
    else:
        empty()
