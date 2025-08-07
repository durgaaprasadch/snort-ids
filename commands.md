| Mode                    | Command                                                              |
| ----------------------- | -------------------------------------------------------------------- |
| IDS (alert/log/pass)    | `sudo snort -A console -q -c /etc/snort/snort.conf -i ens33`          |
| IPS (drop/reject/sdrop) | `sudo snort -Q --daq nfq -c /etc/snort/snort.conf --daq-var queue=0` |


| Action         | Command                                                |
| -------------- | ------------------------------------------------------ |
| alert `/admin` | `curl http://192.168.0.0/admin`                         |
| log telnet     | `telnet 192.168.0.0 23`                                 |
| drop SSH       | `ssh 192.168.0.0`                                       |
| reject ping    | `ping 192.168.0.0`                                      |
| pass test      | `curl http://192.168.0.0/admin` from IP `192.168.1.1` |
| sdrop RDP      | `nc 192.168.0.0 3389`                                   |
