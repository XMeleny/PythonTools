import os


def get_pid_list(process_name):
    cmd = "ps aux"
    process_list = os.popen(cmd).readlines()
    pid_list = []
    for process in process_list:
        if "python" not in process.lower() and process_name in process.lower():
            print(process)
            pid_list.append(process.split()[1])
    print("pid_list = {}".format(pid_list))
    return pid_list


def kill_all_pid(pid_list):
    if len(pid_list) <= 0:
        print("pid list is empty")
        return
    command = "kill -9 " + " ".join(pid_list)
    print("command = {}".format(command))

    result = os.popen(command).readlines()
    print("result = {}".format(result))


if __name__ == '__main__':
    kill_all_pid(get_pid_list("gradle"))
