import can
import datetime
bus = can.interface.Bus("can0", bustype = "socketcan")

a_listener = can.BufferedReader()
notifier = can.Notifier(bus, [a_listener])

counter = 0
counter_files = 0
filename = str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')).replace(" ", "-")[:19]


signals = []
while True:
    export_name = filename + "_" + str(counter_files) + ".log"
    m = a_listener.get_message(0.5)
    counter+=1
    signals.append(str(m) + "\n")

    if(counter ==5000):
        with open(export_name, "w") as f:
            f.writelines(signals)
        signals = []
        counter = 0
        counter_files+=1


        #@reboot cd /home/pi/py_aut/listenery && /usr/bin/python3.5 logfiles_listener.py
