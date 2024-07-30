<div align="center">
  
  # NetRecon
  
</div>

<div align="center">
    <strong>
        <p>
            NetRecon is a Python-based network reconnaissance tool that is designed to make network scanning and penetration testing easier. This script uses `nmap` to perform comprehensive network scans.
        </p>
    </strong>
</div>

<br>

## Features

- Detects and installs `nmap` if not already installed.
- Performs aggressive scans on all 65,535 TCP ports.
- Compatible with multiple operating systems: Linux, macOS, and Windows.

## Installation

Before running the script, ensure you have Python installed on your system. The script will handle the installation of `nmap` for Linux distributions and macOS. Windows users need to install `nmap` manually.

For Linux distributions, the script uses the `distro` package to detect the Linux version. Install it using:

```bash
pip install distro
```

## Usage

Clone the repository and run the script:

```bash
git clone https://github.com/B3TA-BLOCKER/NetRecon.git
cd NetRecon
python3 main.py
```

The script will prompt you to enter an IP address for scanning:

```plaintext
Enter the IP address: <your-ip-address>
```

## Example

Here is an example of how the script works:

```plaintext
Enter the ip: 10.1.170.65
Nmap version 7.94SVN ( https://nmap.org )
Platform: x86_64-pc-linux-gnu
Compiled with: liblua-5.4.6 openssl-3.2.2 libssh2-1.11.0 libz-1.3.1 libpcre2-10.42 libpcap-1.10.4 nmap-libdnet-1.12 ipv6
Compiled without:
Available nsock engines: epoll poll select
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-30 19:00 PKT
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 19:00
Completed NSE at 19:00, 0.00s elapsed
Initiating NSE at 19:00
Completed NSE at 19:00, 0.00s elapsed
Initiating NSE at 19:00
Completed NSE at 19:00, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 19:00
Completed Parallel DNS resolution of 1 host. at 19:00, 0.04s elapsed
Initiating SYN Stealth Scan at 19:00
Scanning 10.1.170.65 [65535 ports]
Completed SYN Stealth Scan at 19:00, 1.33s elapsed (65535 total ports)
Initiating Service scan at 19:00
Initiating OS detection (try #1) against 10.1.170.65
Retrying OS detection (try #2) against 10.1.170.65
NSE: Script scanning 10.1.170.65.
Initiating NSE at 19:00
Completed NSE at 19:00, 0.03s elapsed
Initiating NSE at 19:00
Completed NSE at 19:00, 0.01s elapsed
Initiating NSE at 19:00
Completed NSE at 19:00, 0.01s elapsed
Nmap scan report for 10.1.170.65
Host is up (0.00010s latency).
All 65535 scanned ports on 10.1.170.65 are in ignored states.
Not shown: 65535 closed tcp ports (reset)
Too many fingerprints match this host to give specific OS details
Network Distance: 0 hops

NSE: Script Post-scanning.
Initiating NSE at 19:00
Completed NSE at 19:00, 0.02s elapsed
Initiating NSE at 19:00
Completed NSE at 19:00, 0.00s elapsed
Initiating NSE at 19:00
Completed NSE at 19:00, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 3.65 seconds
           Raw packets sent: 65547 (2.885MB) | Rcvd: 131092 (5.508MB)

```

## Author

- [Hassaan Ali Bukhari](https://github.com/B3TA-BLOCKER)
