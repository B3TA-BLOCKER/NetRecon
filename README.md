# netrecon

`netrecon` is a simple Python script designed for network reconnaissance. It utilizes `nmap` for network scanning and `dirb` for directory brute-forcing on a specified IP address.

## Features

- Scans all ports and performs service detection, OS detection, and more using `nmap`.
- Brute-forces directories on the target IP using `dirb`.

## Requirements

- Python 3.x
- `nmap`
- `dirb`

## Installation

1. Ensure that you have Python 3.x installed on your system.
2. Install `nmap` and `dirb` using your package manager.

For Debian-based distributions (Ubuntu, Kali, etc.):
```bash
sudo apt-get install nmap dirb
```

For Red Hat-based distributions (Fedora, CentOS, etc.):
```bash
sudo yum install nmap dirb
```

## Usage

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/netrecon.git
```

2. Navigate to the repository directory:
```bash
cd netrecon
```

3. Run the script:
```bash
python3 netrecon.py
```

4. Enter the IP address when prompted.

## Example

```bash
$ python3 netrecon.py
Enter the IP: 192.168.1.1
```

## Disclaimer

This script is intended for educational purposes only. Use it at your own risk and ensure that you have proper authorization before scanning any network or IP address.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Replace `YOUR_USERNAME` with your actual GitHub username in the `git clone` command.
