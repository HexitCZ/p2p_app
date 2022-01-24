import json
import platform

def get_path(file_name):
    if platform.system() == "Linux":
        return f'/home/{file_name}'
    elif platform.system() == "Windows":
        return f"{file_name}"

def write_config(i):
    with open(get_path("config.json"),'w') as f:
        json.dump(i, f)

def read_config(setting : str):
    data =""
    try:
        with open(get_path("config.json"), 'r') as f:
            data = dict(json.load(f))
        if len(setting) > 0:
            data = data[setting]
    except:
        pass
    return data

def change_config(setting : str, value):
    try:
        data = ""
        with open(get_path("config.json"), 'r') as f:
            data = dict(json.load(f))
        if len(setting) > 0:
            data[setting] = value
        write_config(data)
    except:
        pass

def clear_config():
    with open(get_path("config.json"), 'wb') as f:
        f.truncate()


def log(i):
    with open(get_path("log.txt"), 'a') as f:
        f.write(i+"\n")