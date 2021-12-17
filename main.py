import discord

global client


def error(text, e=""):
    print("[ERROR]\t" + text + "\nError text: " + str(e) + "\n[Enter to finish]")
    input()
    exit(1)


def info(text):
    print("[INFO]\t" + text)


try:
    config_file = open("settings.env", "r")
    config = eval(config_file.read())
    info("Server starting with settings: " + str(config))
except BaseException as e:
    error("Can not open or read and parse settings file", e)

try:
    client = discord.Client()

    from commands import main

    main(client, config)

    client.run(config["token"])
    info("Bot server finished")
except BaseException as e:
    error("Can not initialize bot", e)

error("programm finished")
