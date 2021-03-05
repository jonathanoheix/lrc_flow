import re
from threading import Timer


def parse_lrc_file(path: str):
    lrc_file = open(path, 'r')
    lines = lrc_file.readlines()

    line_delays = []
    line_contents = []
    timers = []

    for line in lines:
        delay_str = re.search(r'(?<=\[).*?(?=])', line).group()
        delay_float = int(delay_str.split(':')[0])*60 + float(delay_str.split(':')[1])

        line_delays.append(delay_float)

        contents = re.search(r'(?<=]).*', line).group()
        line_contents.append(contents)

        timers.append(Timer(delay_float, print, contents))

    for t in timers:
        t.start()


if __name__ == "__main__":
    parse_lrc_file('../data/test1.lrc')
