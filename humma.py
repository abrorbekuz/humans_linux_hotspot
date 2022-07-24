from os import system


choice = input('Akasi bugun humansdamizmi ? [y/n] ')

if choice.lower() == "y":
    system("sudo sysctl -w net.ipv4.ip_default_ttl=65")
else: system("sudo sysctl -w net.ipv4.ip_default_ttl=64")

