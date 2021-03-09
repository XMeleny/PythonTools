import subprocess


def sh(command, print_msg=True):
    """用于实时输出控制台信息"""
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines = []
    for line in iter(p.stdout.readline, b''):
        line = line.rstrip().decode('utf8')
        if print_msg:
            print(">>>", line)
        lines.append(line)
    return lines


if __name__ == '__main__':
    cmd = "python xxx.py --arg-name value"
    sh(cmd)
