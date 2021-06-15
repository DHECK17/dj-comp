"""
Includes a lot of useful constants that are used in the bot.
"""

from os import environ as env

from datetime import datetime as dt
from dataclasses import dataclass

from discord import Colour


BASE_URL = env['BASE_URL'] if 'BASE_URL' in env else "https://judge0-ce.p.rapidapi.com"
IDE_LINK = "https://hpwebide.42web.io/"

AUTH_HEADER = env['AUTH_HEADER'] if 'AUTH_HEADER' in env else 'X-RapidAPI-Key'
AUTH_KEY = env['AUTH_KEY'] if 'AUTH_KEY' in env else 'a5ec239b6dmsh981b1fd6fbc602ap199c49jsnd2575d8baead'

PREFIX = ";"

# output embed limits
NEWLINES_LIMIT = 10 
CHARACTERS_LIMIT = 300

# time used for calculating uptime
START_TIME = dt.utcnow()

# some information for the Judge0 support server
JUDGE0_GUILD = 620615182116323328
JUDGE0_JOIN_CHANNEL = 623949481167290410
JUDGE0_TEAM = [365859941292048384, 512551605321596928]
JUDGE0_ICON = "https://i.imgur.com/Nab2jCa.png"


LANGUAGES = {
   "array": {
    45: {
        'command': 'assembly',
        'version': 'Assembly (NASM 2.14.02)',
        'icon': 'https://i.imgur.com/ObWopeS.png',
        
        },
    46: {
        'command': 'bash',
        'aliases': ['sh'],
        'version': 'Bash (4.4)',
        'icon': 'https://i.imgur.com/6BQ4g4J.png',
        
        },
    50: {
        'command': 'c',
        'version': 'C (GCC 9.2.0)',
        'icon': 'https://i.imgur.com/Aoo95wm.png',
        
        },
    54: {
        'command': 'cpp',
        'version': 'C++ (GCC 9.2.0)',
        'aliases': ['c++'],
        'icon': 'https://i.imgur.com/CJYqkG5.png',
       
        },
    51: {
        'command': 'csharp',
        'version': 'C# (Mono 6.6.0.161)',
        'aliases': ['c#'],
        'icon': 'https://i.imgur.com/M1AQVY2.png',
        
        },
    55: {
        'command': 'lisp',
        'version': 'Common Lisp (SBCL 2.0.0)',
        'icon': 'https://i.imgur.com/ms9qW6e.png',
       
        },
    56: {
        'command': 'd',
        'version': 'D (DMD 2.089.1)',
        'icon': 'https://i.imgur.com/uoeBAsf.png',
       
        },
    57: {
        'command': 'elixir',
        'version': 'Elixir (1.9.4)',
        'icon': 'https://i.imgur.com/0tigIIL.png',
        
        },
    58: {
        'command': 'erlang',
        'version': 'Erlang (OTP 22.2)',
        'icon': 'https://i.imgur.com/5dVX2NF.png',
        
        },
    60: {
        'command': 'go',
        'version': 'Go (1.13.5)',
        'aliases': ['golang'],
        'icon': 'https://i.imgur.com/a3yrHtU.png',
       
        },
    61: {
        'command': 'haskell',
        'version': 'Haskell (GHC 8.8.1)',
        'icon': 'https://i.imgur.com/NpyZ3z7.png',
       
        },
    62: {
        'command': 'java',
        'version': 'Java (OpenJDK 13.0.1)',
        'icon': 'https://i.imgur.com/5OwBztX.png',
        
        },
    63: {
        'command': 'javascript',
        'aliases': ['js'],
        'version': 'JavaScript (Node.js 12.14.0)',
        'icon': 'https://i.imgur.com/YOsQqBF.png',
       
        },
    64: {
        'command': 'lua',
        'version': 'Lua (5.3.5)',
        'icon': 'https://i.imgur.com/WVKZnEo.png',
        
        },
    65: {
        'command': 'ocaml',
        'version': 'OCaml (4.09.0)',
        'icon': 'https://i.imgur.com/pKLADe6.png',
       
        },
    66: {
        'command': 'octave',
        'version': 'Octave (5.1.0)',
        'icon': 'https://i.imgur.com/dPwBc2g.png',
        
        },
    67: {
        'command': 'pascal',
        'version': 'Pascal (FPC 3.0.4)',
        'icon': 'https://i.imgur.com/KjSF3JE.png',
        
        },
    68: {
        'command': 'php',
        'version': 'PHP (7.4.1)',
        'icon': 'https://i.imgur.com/cnnYSIE.png',
        
        },
    69: {
        'command': 'prolog',
        'version': 'Prolog (GNU Prolog 1.4.5)',
        'icon': 'https://i.imgur.com/yQAknfK.png',
        
        },
    71: {
        'command': 'python',
        'version': 'Python (3.8.1)',
        'aliases': ['py'],
        'icon': 'https://i.imgur.com/N4RyEvG.png',
       
        },
    72: {
        'command': 'ruby',
        'version': 'Ruby (2.7.0)',
        'icon': 'https://i.imgur.com/u9xb12N.png',
        
        },
    73: {
        'command': 'rust',
        'version': 'Rust (1.40.0)',
        'icon': 'https://i.imgur.com/l1TnRxU.png',
        
        },
    74: {
        'command': 'typescript',
        'aliases': ['ts'],
        'version': 'TypeScript (3.7.4)',
        'icon': 'https://i.imgur.com/IBjXVQv.png',
        
        }
   },
   #TODO make this dictionary based on "array"
    "ids": {
        'assembly': 45, 'bash': 46, 'sh': 46,
        'c': 50, 'cpp': 54, 'c++': 54, 'csharp': 51,
        'c#': 51, 'lisp': 55, 'd': 56, 'elixir': 57,
        'erlang': 58, 'go': 60, 'golang': 60,
        'haskell': 61, 'java': 62, 'javascript': 63,
        'js': 63, 'lua': 64, 'ocaml': 65, 'octave': 66,
        'pascal': 67, 'php': 68, 'prolog': 69, 'python': 71,
        'py': 71, 'ruby': 72, 'rust': 73,
        'typescript': 74, 'ts': 74
        }
}


@dataclass
class Emoji:
    """
    Represents storage for custom and external emojis.
    """
    class Workers:
        """
        Represents emojis for workers health check.
        (command in bot.cogs.information)
        """
        total= "\U0001F1FD"
        available = "\U0001F1FD"
        idle = "\U0001F1FD"
        working = "\U0001F1FD"
        paused = "\U0001F1FD"
        failed = "\U0001F1FD"

    class Execution:
        loading = "\U0001F1FD"
        error = "\U0001F1FD"
        successful = "\U0001F1FD"
        offline = "\U0001F1FD"
        idle = "\U0001F1FD"

@dataclass
class Color:
    difficulties = [
5025872, 9225035, 13491257, 16772154, 16761352, 16750593, 16668450, 16073527
]
