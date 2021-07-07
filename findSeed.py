import os
import sys
import requests
import json
from datetime import datetime
from multiprocessing import Process
import subprocess
import signal
import json
import socket

old_getaddrinfo = socket.getaddrinfo


def new_getaddrinfo(args, *kwargs):
    resps = old_getaddrinfo(args, *kwargs)
    return [resp for resp in resps if resp[0] == socket.AF_INET]


socket.getaddrinfo = new_getaddrinfo


def display_seed(verif_data, seed):
    if os.path.exists("token.txt"):
        if not os.path.exists("past-tokens"):
            os.mkdir("past-tokens")
        datestr = datetime.now().strftime("%Y%m%d%H%M%S%f")
        os.rename("token.txt", f"past-tokens/token-{datestr}.txt")
    with open(f"token.txt", 'w') as tokenFile:
        tokenFile.write("Seed: " + seed + "\n")
        tokenFile.write("Token: " + json.dumps(verif_data) + "\n")
    print(seed)


def run_seed(filter):
    seed = ""
    while seed == "":
        resp = requests.get(f"http://fsg.gel.webfactional.com?filter={filter}")
        res_json = resp.json()
        sseed = res_json.get("struct")
        sclass = res_json.get("class")
        randbiome = res_json.get("randbiome")
        pref = res_json.get("pref")  # village and/or shipwreck preference
        cmd = f'./bh {sseed} {sclass} {randbiome} {pref}'
        seed = os.popen(cmd).read().strip()
    display_seed(res_json, seed)


def start_run():
    with open('settings.json') as filter_json:
        read_json = json.load(filter_json)
        filter = read_json["filter"]
        num_processes = read_json["thread_count"]
    processes = []
    for i in range(num_processes):
        processes.append(Process(target=run_seed, args=(filter,)))
        processes[-1].start()
    i = 0
    while True:
        for j in range(len(processes)):
            if not processes[j].is_alive():
                for k in range(len(processes)):
                    processes[k].kill()
                    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
                    out, err = p.communicate()
                    for line in out.splitlines():
                        if b'bh' in line:
                            pid = int(line.split(None, 1)[0])
                            os.kill(pid, signal.SIGTERM)
                return
        i = (i + 1) % num_processes


if __name__ == '__main__':
    start_run()
