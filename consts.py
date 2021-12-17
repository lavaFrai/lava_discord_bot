import math
from MathFunctions import *

VERSION = "1.1.0"
allowed_functions = {
    "range": rangeTmp,
    "list": list,
    "set": set,
    "str": str,
    "int": int,
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "asin": lambda x: math.degrees(math.asin(x)),
    "acos": lambda x: math.degrees(math.acos(x)),
    "atan": lambda x: math.degrees(math.atan(x)),
    "hypotenuse": math.hypot,
    "pow": powTmp,
    "pi": math.pi,
    "e": math.e,
    "deg": math.degrees,
    "rad": math.radians,
    "abs": abs,
    "fact": factTmp,
    "sum": sumTmp,
    "log": math.log,
    "sqrt": math.sqrt,
    "gamma": math.gamma
}

help_list = {
    "version": {
        "short": "текущая версия бота и используемых им библиотек",
        "examples": [
            "version"
        ],
        "details": None
    },
    "info": {
        "short": "предоставляет техническую информацию о сообщении, канале, сервере (может быть полезно при отладке)",
        "examples": [
            "info"
        ],
        "details": None
    },
    "setprefix": {
        "short": "меняет используемый на вашем сервере префикс (доступно только админам)",
        "examples": [
            "setprefix !"
        ],
        "details": None
    },
    "calc": {
        "short": "вычисляет математическое выражение, може использовать функции (подробнее о функциях - *help math*)",
        "examples": [
            "calc 2+2*2"
        ],
        "details": None
    },
    "exec": {
        "short": "итерпретирует код на сервере с помощью python3 и возвращает стандартный поток ввода-вывода ("
                 "доступно только администраторам)",
        "examples": [
            "exec print(\"Hello, World!\")"
        ],
        "details": None
    },
    "file": {
        "short": "выгружает файл с сервера (доступно только администраторам)",
        "examples": [
            "file cat.png"
        ],
        "details": None
    },
    "clear": {
        "short": "удаляет сообщения из текущего канала (доступно только администраторам)",
        "examples": [
            "clear 25"
        ],
        "details": None
    },
    "status": {
        "short": "устанавливает боту новый статус (доступно только администраторам)",
        "examples": [
            "status listen любимую песню",
            "status play GTA5"
        ],
        "details": None
    }
}
