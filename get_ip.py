# encoding=utf-8
import re
import linecache


def fileParse():
    """
    FOR FILE CONTENT LIKE THIS:
    
    counterstrike1-prestg | CHANGED | rc=0 >>
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
           valid_lft forever preferred_lft forever
    2: ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        link/ether 52:54:00:f2:2f:80 brd ff:ff:ff:ff:ff:ff
        inet 11.231.21.11/23 brd 10.235.3.255 scope global ens3
           valid_lft forever preferred_lft forever
        inet6 fe80::5054:ff:fef2:2f80/64 scope link
           valid_lft forever preferred_lft forever
    counterstrike2-prestg | CHANGED | rc=0 >>
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
           valid_lft forever preferred_lft forever
    2: ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        link/ether 52:54:00:b1:1e:1e brd ff:ff:ff:ff:ff:ff
        inet 11.232.41.33/24 brd 10.235.4.255 scope global ens3
           valid_lft forever preferred_lft forever
        inet6 fe80::5054:ff:feb1:1e1e/64 scope link
           valid_lft forever preferred_lft forever
    """

    fp = open('./ips.txt', 'r')

    number = []
    lineNumber = 1

    for index, eachLine in enumerate(fp):
        m = re.search('CHANGED', eachLine)
        if m is not None:
            number.append(lineNumber)
        lineNumber = lineNumber + 1
    number.append(index+1)
    size = int(len(number))

    line_cache = linecache.getlines('./ips.txt')

    for i in range(0, size-1):
        start = number[i]
        end = number[i + 1]
        segment = line_cache[start-1:end - 1]

        print(segment[0].split("|")[0])
        for line in segment:
            result2 = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',line)
            for item in result2:
                if not item == [] and item != '127.0.0.1' and '255' not in item:
                    nic_name = line.split(" ")[-1].replace("\n", "")
                    print(nic_name + ": " + item)
        print("==========")


if __name__ == '__main__':

    fileParse()
