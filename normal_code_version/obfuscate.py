import requests
import re
import json
import sys

from parse import shit


def obuscate(filename, power=50, times=1):
    link = "https://pyob.oxyry.com/obfuscate"

    with open(filename, "r") as f:
        data = "def hvjhzdhfklhakhhgfxhhcuyi9832():\n" + "\n".join(
            ["    " + i for i in f.readlines()]
        )

    payload = {
        "append_source": False,
        "remove_docstrings": False,
        "rename_nondefault_parameters": True,
        "rename_default_parameters": True,
        "preserve": "",
        "source": data,
    }

    result = "\n".join(
        [
            i[4:]
            for i in (
                json.loads(requests.post(link, json=payload).content)["dest"].split(
                    "\n"
                )[1:]
            )
        ]
    )

    with open(filename, "w") as f:
        f.write(re.sub(r"\#line:\d+", "", result))

    for _ in range(times):
        shit(filename, power)


args = sys.argv

if len(args) not in (2, 3, 4):
    raise ValueError("Wrong number of arguments, please provide filename")

if len(args) == 2:
    obuscate(args[1])
elif len(args) == 3:
    obuscate(args[1], int(args[2]))
elif len(args) == 4:
    obuscate(args[1], int(args[2]), int(args[3]))
