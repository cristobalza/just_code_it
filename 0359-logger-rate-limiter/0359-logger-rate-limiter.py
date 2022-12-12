class Logger:

    def __init__(self):
        self.msg2time = collections.defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msg2time:
            self.msg2time[message] = timestamp
            return True
        if timestamp - self.msg2time[message] >= 10:
            self.msg2time[message] = timestamp
            return True
        else:
            return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)