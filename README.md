<div align="center"><strong>NetRecon</strong></div>

<div align="center">
    <strong>
        <p>
              NetRecon is a powerful network reconnaissance tool written in Python, designed to make network scanning and penetration testing easier. This script uses `nmap` to perform comprehensive network scans.
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
Enter the IP address: 192.168.1.1
Installing Nmap ......
nmap installation successful
Starting Nmap 7.80 ( https://nmap.org ) at 2024-07-30 12:00 UTC
Nmap scan report for 192.168.1.1
Host is up (0.00052s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
80/tcp open  http
```

## Author

- [Hassaan Ali Bukhari](https://github.com/B3TA-BLOCKER)
