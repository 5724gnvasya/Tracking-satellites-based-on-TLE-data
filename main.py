import threading
import time
from func import fetch_tle_data, initialize_csv, add_id, remove_id, assign_colours, make_other

event = threading.Event()

def stop():
    event.set()
    thread.join()

def endless_loop():
    while True:
        event.wait()  # Ждем события
        if event.is_set():
            break
        # Выполняйте код, который должен повторяться бесконечно
        fetch_tle_data()
        make_other()
        time.sleep(30)


# fetch_tle_data()
#initialize_csv()
#add_id(0)
#remove_id(0)
#assign_colours()
#make_other()

thread = threading.Thread(target=endless_loop)
thread.start()

time.sleep(20)
stop()

