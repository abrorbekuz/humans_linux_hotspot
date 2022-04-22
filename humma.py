from os import system


choice = input('Akasi bugun humansdamizmi ? [y/n] ')

if choice.lower() == "y":
    system("./h_activate.sh")
else: system("./h_deactivate.sh")

