#! /usr/bin/env python3

from colorama import init, Fore, Back, Style
init(autoreset=True)
messages = [
         'blah blah blah',
          (Fore.LIGHTYELLOW_EX + Style.BRIGHT
               + Back.MAGENTA + 'Alert!!!'),
           ( Fore.RED + 'blah blah blah' )
           ]
for m in messages:
     print(m)
