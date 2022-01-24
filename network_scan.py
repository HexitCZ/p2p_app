import subprocess
import threading
import re
import socket
import time
import file_manager as fm
import platform

max_thread_count = 800

__ping_count = 0

address = "000.000"

clients = []



def ping(third_clm : int,fourth_clm : int):
    global __ping_count
    global address
    global clients

    full_address = f"{address}{third_clm}.{fourth_clm}"
    __ping_count += 1

    try:
        print(full_address, threading.activeCount())
        if platform.system() == "Linux":
            output = subprocess.run(['ping', '-c', '1', full_address],capture_output=True, timeout=0.8, encoding="utf-8")
        elif platform.system() == "Windows":
            output = subprocess.run(['ping', '-n', '1', full_address],capture_output=True, timeout=0.8, encoding="utf-8")
        if re.search(r'unreachable', str(output)) is not None:
            __ping_count -= 1
            return
        clients.append(full_address)
        __ping_count -= 1
        return
    except subprocess.CalledProcessError:
        __ping_count -= 1
        return
    except subprocess.TimeoutExpired:
        __ping_count -= 1
        return


def scan_net(from_third : int, to_third : int, from_fourth : int, to_fourth : int):
    global clients
    global address
    global __ping_count
    address = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.", fm.read_config("ip")).group()

    for j in range(from_third, to_third+1):
        for i in range(from_fourth, to_fourth+1):
            if threading.activeCount() >= max_thread_count:
                time.sleep(0.6)
            t = threading.Thread(target=ping, args=(j, i,), daemon=True)
            t.start()
        # time.sleep(0.8)
    while (__ping_count > 0):
        # print(__ping_count)
        pass
    return clients


# print(scan_net(80,89,1,255))

