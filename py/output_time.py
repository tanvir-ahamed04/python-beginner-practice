import datetime

current_time = datetime.datetime.now()
print("Current time:", current_time)
# 12 hours formet
print("Current time:", current_time.strftime("%I:%M:%S %p"))