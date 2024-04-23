# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import requests

def say_hello():
    resp = requests.get("https://httpbin.org/get")
    if resp.status_code == 200:
        print("i am here")
        return "hi"
    else:
        print("i am here")
        return "something went wrong"


if __name__ == "__main__":
    say_hello()
