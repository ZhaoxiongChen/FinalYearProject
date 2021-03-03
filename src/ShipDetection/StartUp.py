import os
import time

date = time.strftime("%Y-%m-%d_", time.localtime())
command = "python Menu.py | tee -a " + date + "log.txt"

os.system(command)

# os.system("shutdown -s -t 120")
