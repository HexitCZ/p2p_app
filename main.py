import socket
import threading
import network_scan as ns
import re
import file_manager as fm
import time


listen_ip = fm.read_config("ip")
listen_port = fm.read_config("port")

listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listen_sock.settimeout(3)
send_sock.settimeout(3)

dictionary = fm.read_config("word-dict")
err_messages = {"nolocal" : "prdel",
                "noremote" : "That word cannot be translated remotely.",
                "noany" : "That word cannot be translated in any way.",
                "noconfig" : "Config file is missing. Run build_conf.py"}

peer_list = []

def update_peer_list():
    global peer_list
    global send_sock
    ranges = [int(item) for item in str(fm.read_config("subnet-range")).split('-')]
    ips = ns.scan_net(ranges[0], ranges[1], ranges[2], ranges[3])
    ips.remove(listen_ip)
    ips.sort()

    for p in ips:
        try:
            send_sock.close()
            send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            send_sock.settimeout(1)
            send_sock.connect((p,listen_port))
            peer_list.append(p)
        except TypeError:
            if peer_list.count(p) > 0:
                peer_list.remove(p)
                peer_list.sort()
            continue
        except ConnectionRefusedError:
            continue
        except OSError:
            return
    #print(peer_list)

def answer(word : str = "", success : bool = False, err_msg : str = ""):
    if success:
        return f'TRANSLATESUC"{word}"'
    else:
        return f'TRANSLATEERR"{err_msg}"'

def local_translate(word):
    try:
        return answer(word=dictionary[word],success=True)
    except:
        return answer(success=False, err_msg=err_messages["nolocal"])


def remote_translate(word):
    global peer_list
    global send_sock
    update_peer_list()
    for p in peer_list:

        try:
            send_sock.close()
            send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            send_sock.connect((p,listen_port))
            send_sock.send(f'TRANSLATELOC"{word}"'.encode('utf-8'))
            output = send_sock.recv(128).decode('utf-8')
            if re.match('TRANSLATESUC',output) is not None:
                return answer(word=output[13:-1],success=True)
            else:
                continue
        except socket.timeout:
            continue
        except OSError:
            continue
    return answer(success=False,err_msg=err_messages["noremote"])


def any_translate(word):
    lt = local_translate(word)
    if not re.match('TRANSLATEERR',lt):
        return lt
    else:
        rt = remote_translate(word)
        if not re.match('TRANSLATEERR',rt):
            return rt
    return answer(success=False, err_msg=err_messages["noany"])


commands = \
     {
     "TRANSLATELOC" : local_translate,
     "TRANSLATEREM" : remote_translate,
     "TRANSLATEANY" : any_translate,
     }


def check_command(command : str):
    try:
        return commands[command]
    except:
        return None


def listen_remote(bind_ip : str, bind_port : int):
    global listen_sock
    try:
        listen_sock.bind((bind_ip, bind_port))
    except TypeError:
        fm.log(answer(success=False, err_msg=err_messages["noconfig"]))
    listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_sock.listen()
    while True:
        try:
            client, info = listen_sock.accept()
            cmd = client.recv(128).decode('utf-8')
            fm.log(cmd)
            if re.match("TRANSLATE", cmd):
                output = check_command(cmd[:12])(cmd[13:-1])
                client.send(output.encode('utf-8'))
                fm.log(output)
        except :
            continue


def main():
    listener = threading.Thread(target=listen_remote, args=(listen_ip,listen_port,))
    listener.start()
    #region DEBUG-ONLY
    #THIS PIECE OF CODE IS FOR DEBUGGING ONLY
    #while True:
    #    cmd = input("cmd:")
    #    fm.log(cmd)
   #     out = check_command(cmd[:12])(cmd[13:-1])
   #     print(out)
    #    fm.log(out)

    #endregion
if __name__ == '__main__':
    main()


