import discord
import os
import consts
import os.path
import sys

from consts import allowed_functions, help_list

servdir_files = {"config.json": "{'prefix': '/'}"}


def error(text, e=""):
    print("[ERROR]\t" + str(text) + "\nError text: " + str(e) + "\n[Enter to finish]")
    input()
    exit(1)


def info(text):
    print("[INFO]\t" + str(text))


global client


def main(client, config):
    @client.event
    async def on_ready():
        info('Server success started, we have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if str(message.guild.id) not in os.listdir(path="./servers"):
            os.mkdir("./servers/" + str(message.guild.id))
        servdir = "./servers/" + str(message.guild.id)
        for i in servdir_files:
            if not os.path.exists(servdir + "/" + i):
                f = open(servdir + "/" + i, "w")
                f.write(servdir_files[i])
                f.close()
        servconfig = eval(open(servdir + "/config.json", "r").read())

        if message.author == client.user:
            return

        if message.content.lower().startswith('hello, bot'):
            await message.channel.send('Hello, build 1.0.0')

        if message.content.lower().startswith(servconfig['prefix'] + 'version'):
            f = open("requirements.txt", "r")

            embed = discord.Embed(
                title='Версия бота и библиотек',
                description="Сборка бота: ```\n" + consts.VERSION +
                            "\n```\n\nВерсии библиsотек: ```\n" + f.read() + "\n```",
                colour=discord.Colour.from_rgb(config['embed_color'][0], config['embed_color'][1],
                                               config['embed_color'][2])
            )
            await message.channel.send(embed=embed)

        if message.content.lower().startswith(servconfig['prefix'] + 'info'):
            embed = discord.Embed(
                title='Технические свойства сообщения',
                description="Автор: **" + str(message.author.name) + "#" + str(
                    message.author.discriminator) + "**\nКанал: **" + str(message.channel) + '**\nID канала: **' + str(
                    message.channel.id) + "**\nСервер: **" + str(message.guild) + "**\nСервер ID: **" + str(
                    message.guild.id) + "**",
                colour=discord.Colour.from_rgb(config['embed_color'][0], config['embed_color'][1],
                                               config['embed_color'][2])
            )
            await message.channel.send(embed=embed)

        if message.content.lower().startswith(servconfig['prefix'] + 'help'):
            try:
                temp = "\n"
                for j in help_list:
                    temp += "**"
                    temp += j
                    temp += "**\n"
                    temp += help_list[j]["short"]
                    temp += "```\n"
                    for i in help_list[j]["examples"]:
                        temp += servconfig['prefix']
                        temp += i
                        temp += "\n"
                    temp += "```\n"
                embed = discord.Embed(
                    title='Помощь',
                    description=temp,
                    colour=discord.Colour.from_rgb(config['embed_color'][0], config['embed_color'][1],
                                                   config['embed_color'][2])
                )
                await message.channel.send(embed=embed)
            except BaseException as e:
                embed = discord.Embed(
                    title='Помощь',
                    description="Ошибка: " + str(e),
                    colour=discord.Colour.from_rgb(config['error_color'][0], config['error_color'][1],
                                                   config['error_color'][2])
                )
                await message.channel.send(embed=embed)

        if message.content.lower().startswith(servconfig['prefix'] + 'setprefix'):
            servconfig['prefix'] = message.content.split()[1][0]
            f = open(servdir + "/config.json", "w")
            f.write(str(servconfig))
            f.close()
            embed = discord.Embed(
                title='Смена префикса',
                description="Отлично!\nНовый префикс для этого сервера установлен в '**" + message.content.split()[1][
                    0] + "**'",
                colour=discord.Colour.from_rgb(config['embed_color'][0], config['embed_color'][1],
                                               config['embed_color'][2])
            )
            await message.channel.send(embed=embed)

        if message.content.lower().startswith(servconfig['prefix'] + 'calc'):
            comand = message.content[6:]

            if comand.find("__") != -1:
                if (str(message.author.name) + "#" + str(message.author.discriminator)) in config["admin_list"]:
                    try:
                        embed = discord.Embed(
                            title='Вычисление',
                            description="Результат выражения ```python\n" + comand + "``` равняется **" + str(
                                eval(comand)) + "**",
                            colour=discord.Colour.from_rgb(config['embed_color'][0], config['embed_color'][1],
                                                           config['embed_color'][2])
                        )
                        await message.channel.send(embed=embed)
                    except BaseException as e:
                        embed = discord.Embed(
                            title='Вычисление',
                            description="При вычислении вашего выражения ```python\n" + comand + "``` произошла "
                                                                                                 "ошибка **" + str(
                                e) + "**",
                            colour=discord.Colour.from_rgb(config['error_color'][0], config['error_color'][1],
                                                           config['error_color'][2])
                        )
                        await message.channel.send(embed=embed)
                else:
                    embed = discord.Embed(
                        title='Вычисление',
                        description="Ошибка!\nВаше выражение оказалось не безопасным, поэтому мы не смогли его "
                                    "интерпретировать",
                        colour=discord.Colour.from_rgb(config['error_color'][0], config['error_color'][1],
                                                       config['error_color'][2])
                    )
                    await message.channel.send(embed=embed)
            else:
                if (str(message.author.name) + "#" + str(message.author.discriminator)) in config["admin_list"]:
                    try:
                        embed = discord.Embed(
                            title='Вычисление',
                            description="Результат выражения ```python\n" + comand + "``` равняется **" + str(
                                eval(comand)) + "**",
                            colour=discord.Colour.from_rgb(config['embed_color'][0], config['embed_color'][1],
                                                           config['embed_color'][2])
                        )
                        await message.channel.send(embed=embed)
                    except BaseException as e:
                        embed = discord.Embed(
                            title='Вычисление',
                            description="При вычислении вашего выражения ```python\n" + comand + "``` произошла "
                                                                                                 "ошибка **" + str(
                                e) + "**",
                            colour=discord.Colour.from_rgb(config['error_color'][0], config['error_color'][1],
                                                           config['error_color'][2])
                        )
                        await message.channel.send(embed=embed)
                else:
                    if comand.find("**") != -1:
                        embed = discord.Embed(
                            title='Вычисление',
                            description="Использование оператора ```**``` отключено, используйте ```pow()```",
                            colour=discord.Colour.from_rgb(config['error_color'][0], config['error_color'][1],
                                                           config['error_color'][2])
                        )
                        await message.channel.send(embed=embed)
                    if comand.find("for") != -1 or comand.find("while") != -1:
                        embed = discord.Embed(
                            title='Вычисление',
                            description="Использование оператора ```\nfor\nwhile``` отключено используйте range()",
                            colour=discord.Colour.from_rgb(config['error_color'][0], config['error_color'][1],
                                                           config['error_color'][2])
                        )
                        await message.channel.send(embed=embed)
                    try:
                        embed = discord.Embed(
                            title='Вычисление',
                            description="Результат выражения ```python\n" + comand + "``` равняется **" + str(
                                eval(comand, {'__builtins__': allowed_functions})) + "**",
                            colour=discord.Colour.from_rgb(config['embed_color'][0], config['embed_color'][1],
                                                           config['embed_color'][2])
                        )
                        await message.channel.send(embed=embed)
                    except BaseException as e:
                        embed = discord.Embed(
                            title='Вычисление',
                            description="При вычислении вашего выражения ```python\n" + comand + "``` произошла "
                                                                                                 "ошибка **" + str(
                                e) + "**",
                            colour=discord.Colour.from_rgb(config['error_color'][0], config['error_color'][1],
                                                           config['error_color'][2])
                        )
                        await message.channel.send(embed=embed)

        if message.content.lower().startswith(servconfig['prefix'] + 'exec'):
            command = message.content[6:]
            if (str(message.author.name) + "#" + str(message.author.discriminator)) in config["admin_list"]:
                try:
                    sys.stdout = open("tmp.log", "w")
                    exec(command)
                    sys.stdout.close()

                    f = open("tmp.log", "r")
                    tmp = f.read()
                    f.close()

                    embed = discord.Embed(
                        title='Исполнение',
                        description="Ваш код: ```python\n#code:\n\n" + command + "``` Успешно завершен!\nВывод "
                                                                                 "stdout: ```#stdout:\n\n" + tmp +
                                    "```",
                        colour=discord.Colour.from_rgb(config['embed_color'][0], config['embed_color'][1],
                                                       config['embed_color'][2])
                    )
                    await message.channel.send(embed=embed)
                except BaseException as e:
                    embed = discord.Embed(
                        title='Исполнение',
                        description="Ваш код: ```python\n#code:\n\n" + command + "``` Не удалось выполнить из-за не "
                                                                                 "обработанной ошибки ```\n#stderr:\n\n"
                                    + str(e) + "```",
                        colour=discord.Colour.from_rgb(config['error_color'][0], config['error_color'][1],
                                                       config['error_color'][2])
                    )
                    await message.channel.send(embed=embed)

        if message.content.lower().startswith(servconfig['prefix'] + 'file'):
            command = message.content[6:]
            if (str(message.author.name) + "#" + str(message.author.discriminator)) in config["admin_list"]:
                try:
                    await message.channel.send(file=discord.File(command))
                except BaseException as e:
                    embed = discord.Embed(
                        title='Выгрузка файлов',
                        description="Не удалось выполнить из-за не "
                                    "обработанной ошибки "
                                    + str(e),
                        colour=discord.Colour.from_rgb(config['error_color'][0], config['error_color'][1],
                                                       config['error_color'][2])
                    )
                    await message.channel.send(embed=embed)

        if message.content.lower().startswith(servconfig['prefix'] + 'clear'):
            command = message.content[7:]
            if (str(message.author.name) + "#" + str(message.author.discriminator)) in config["admin_list"]:
                try:
                    Schannel = message.channel
                    async for i in Schannel.history(limit=int(command)):
                        await i.delete()
                    # deleted = await client.purge_from(message.channel, limit=10, check=True)

                    embed = discord.Embed(
                        title='Удаление',
                        description="Успешно удалено " + str(command) + " сообщений",
                        colour=discord.Colour.from_rgb(config['embed_color'][0], config['embed_color'][1],
                                                       config['embed_color'][2])
                    )
                    await message.channel.send(embed=embed)
                except BaseException as e:
                    embed = discord.Embed(
                        title='Удаление',
                        description="При удалении сообщений произошла ошибка " + str(e),
                        colour=discord.Colour.from_rgb(config['embed_color'][0], config['embed_color'][1],
                                                       config['embed_color'][2])
                    )
                    await message.channel.send(embed=embed)

        if message.content.lower().startswith(servconfig['prefix'] + 'status'):
            command = message.content[8:]
            Ctype = message.content.split()[1]
            try:
                if (str(message.author.name) + "#" + str(message.author.discriminator)) in config["admin_list"]:
                    if Ctype == "play":
                        await client.change_presence(status=discord.Status.online,
                                                     activity=discord.Game(command[len(Ctype) + 1:]))
                        message.delete()
                    elif Ctype == "stream":
                        await client.change_presence(
                            status=discord.Status.online,
                            activity=discord.Streaming(name=command[len(Ctype) + 1:],
                                                       url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                                                       ))
                        message.delete()
                    elif Ctype == "comp":
                        await client.change_presence(status=discord.Status.online,
                                                     activity=discord.Activity(name=command[len(Ctype) + 1:],
                                                                               type=discord.ActivityType.competing))
                        message.delete()
                    elif Ctype == "listen":
                        await client.change_presence(status=discord.Status.online,
                                                     activity=discord.Activity(name=command[len(Ctype) + 1:],
                                                                               type=discord.ActivityType.listening))
                        message.delete()
                    elif Ctype == "watch":
                        await client.change_presence(status=discord.Status.online,
                                                     activity=discord.Activity(name=command[len(Ctype) + 1:],
                                                                               type=discord.ActivityType.watching))
                        message.delete()
                    elif Ctype == "off":
                        await client.change_presence(status=discord.Status.invisible, activity=None)
                        message.delete()
                    else:
                        embed = discord.Embed(
                            title='Изменение статуса',
                            description="Не верный тип статуса. Используйте доступные в настоящее время: \n```\n"
                                        "play  -  играет в *user data*\n" +
                                        "stream  -  стримит *user data*\n" +
                                        "comp  -  соревнуется в *user data*\n" +
                                        "listen  -  слушает *user data*\n" +
                                        "watch  -  смотрит *user data*\n" +
                                        "off  -  *no status*\n" +
                                        "\n```",
                            colour=discord.Colour.from_rgb(config['error_color'][0], config['error_color'][1],
                                                           config['error_color'][2])
                        )
                        await message.channel.send(embed=embed)
            except BaseException as e:
                embed = discord.Embed(
                    title='Изменение статуса',
                    description="Ошибка: " + str(e),
                    colour=discord.Colour.from_rgb(config['error_color'][0], config['error_color'][1],
                                                   config['error_color'][2])
                )
                await message.channel.send(embed=embed)


"""@client.command() async def stream(ctx, *, status): await client.change_presence(status = discord.Status.online, 
activity = discord.Streaming(name = f'{status}', url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', platform = 
'Google')) """
