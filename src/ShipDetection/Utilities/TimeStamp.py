import time


class TimeStamp:

    def __init__(self):
        self.t0 = 0.0
        self.t0_formatted = ""
        self.t1 = 0.0
        self.t1_formatted = ""

    def start(self):
        self.t0 = time.process_time()
        self.t0_formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("Started at: " + self.t0_formatted + ".")

    def stop(self):
        self.t1 = time.process_time()
        self.t1_formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("Finished at: " + self.t1_formatted + ".")

    def summary(self):
        print("Summary")
        print("Operation started at: " + self.t0_formatted + ".")
        print("Operation finished at: " + self.t1_formatted + ".")
        print("Operation costs " + str(self.t1 - self.t0) + " seconds.")
