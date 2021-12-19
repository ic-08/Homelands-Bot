# Indent level of 1 says the day of the week # 
#805 schedule
dict805 = {
    "1": {
        "1": "Math",
        "2": "Math",
        "3": "Arts",
        "4": "Phys Ed.",
        "5": "Français",
        "6": "Science",
        "7": "Geography/Language Arts",
        "8": "Geography/Language Arts"},
    "2": {
        "1": "Math",
        "2": "Math",
        "3": "Français",
        "4": "Science",
        "5": "Language Arts",
        "6": "Music",
        "7": "Geography",
        "8": "Art"},
    "3": {
        "1": "Math",
        "2": "Math",
        "3": "Français",
        "4": "DPA",
        "5": "Language Arts",
        "6": "Music",
        "7": "STEAM",
        "8": "Geography/Language Arts"},
    "4": {
        "1": "Math",
        "2": "Math",
        "3": "Français",
        "4": "Health",
        "5": "Language Arts",
        "6": "Core/Science",
        "7": "Core/Science",
        "8": "Phys Ed."},
    "5": {
        "1": "Math",
        "2": "Math",
        "3": "Français",
        "4": "DPA",
        "5": "Language Arts",
        "6": "Core/Geography",
        "7": "Core/Geography",
        "8": "STEAM"}}

#705 schedule
dict705 = {
    "1": {
        "1": "Core",
        "2": "Core",
        "3": "Core",
        "4": "French",
        "5": "Core",
        "6": "Core",
        "7": "Core",
        "8": "Phys Ed"},
    "2": {
        "1": "Core",
        "2": "STEAM",
        "3": "Core",
        "4": "Core",
        "5": "Core",
        "6": "French",
        "7": "Core",
        "8": "Core"},
    "3": {
        "1": "Core",
        "2": "Core",
        "3": "STEAM",
        "4": "French",
        "5": "Core",
        "6": "Core",
        "7": "Core",
        "8": "Core"},
    "4": {
        "1": "Core",
        "2": "Phys Ed",
        "3": "Core",
        "4": "Music",
        "5": "Core",
        "6": "Core",
        "7": "Core",
        "8": "French"},
    "5": {
        "1": "Core",
        "2": "Core",
        "3": "French",
        "4": "Core",
        "5": "Core",
        "6": "Core",
        "7": "Music",
        "8": "Core"}}

#605 schedule
dict605 = {
    "1": {
        "1": "Core",
        "2": "Core",
        "3": "Core",
        "4": "French",
        "5": "Core",
        "6": "Music",
        "7": "Core",
        "8": "Core"},
    "2": {
        "1": "Core",
        "2": "Phys Ed",
        "3": "Core",
        "4": "Health/Art",
        "5": "Core",
        "6": "Core",
        "7": "French",
        "8": "Core"},
    "3": {
        "1": "Core",
        "2": "Core",
        "3": "Health/Art",
        "4": "Core",
        "5": "Core",
        "6": "Core",
        "7": "Music",
        "8": "French"},
    "4": {
        "1": "Core",
        "2": "Core",
        "3": "STEAM",
        "4": "Core",
        "5": "Core",
        "6": "Health/Art",
        "7": "French",
        "8": "Core"},
    "5": {
        "1": "Core",
        "2": "STEAM",
        "3": "Core",
        "4": "French",
        "5": "Core",
        "6": "Core",
        "7": "Core",
        "8": "Phys Ed"}}


def sub(day,cls):
    txt = ""
    if cls == '705':
        cls = dict705
    elif cls == '605':
        cls = dict705
    else:
        cls = dict805
    for x in range(1,9):
        txt += f"Period {x} : {cls[str(day)][str(x)]} \n"
    return txt



