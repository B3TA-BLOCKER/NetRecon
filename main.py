import os 
import subprocess
import platform


def install_nmap() -> bool:
    os_type = platform.system().lower()
    try:
        if os_type == 'linux' :
            distro = platform.linux_distribution()[0].lower()
            if 'ubuntu' in distro or 'debian' in distro :
                subprocess.run(['sudo', 'apt-get' , 'update'], check =True)
                subprocess.run(['sudo' , 'apt-get' , 'install' , '-y' , 'nmap'],check=True)
            elif 'fedora' in distro or 'centos' in distro or 'rhel' in distro:
                subprocess.run(['sudo', 'dnf', 'install' , '-y' , 'nmap'],check=True)
            else:
                print(f"Unsupported Linux Distribution : {distro}")
                return False
        elif os_type == 'Darwin': # macOS
            subprocess.run(['brew' , 'install' , 'nmap'],check=True)
        elif os_type == 'windows':
            print("Please download and install nmap manually from https://nmap.org/download.html")
            return False
        else:
            print(f"Unsupported Linux Distribution : {distro}")
            return False
        print("nmap installation successful ")
        return True
    except subprocess.CalledProcessError as e:
        print(f"An Error occured during Installation: {e}")
        return False


def recon(ip)-> None:
    os.system(f"nmap -A -p- -Pn {ip} -v")


ip_address = input("Enter the ip: ")

result = subprocess.run(['nmap', '--version'])

if result.returncode == 0:
    recon(ip=ip_address)
else:
    if install_nmap():
        recon(ip=ip_address)
