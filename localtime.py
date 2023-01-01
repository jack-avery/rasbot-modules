from src.commands import BaseModule

import time


class Module(BaseModule):
    helpmsg = "Show the streamers' local time. Usage: time"

    def main(self, message):
        return time.asctime()
