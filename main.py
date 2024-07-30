import os 
import subprocess
import platform


result = subprocess.run(['nmap', '--version'])

def install_nmap():
    os_type = platform.system()
    try:
        if os_type == 'Linux' :
            distro = platform.linux_distribution()[0].lower()
            if 'ubuntu' in distro or 'debian' in distro :
                subprocess.run(['sudo', 'apt-get' , 'update'], check =True)
                subprocess.run(['sudo' , 'apt-get' , 'install' , '-y' , 'nmap'],check=True)
            elif 'fedora' in distro or 'centos' in distro or 'rhel' in distro:
                subprocess.run(['sudo', 'dnf', 'install' , '-y' , 'nmap'],check=True)


def recon(ip):
    os.system(f"nmap -A -p- -Pn {ip} -v")
    os.system(f"dirb {ip}")


if result.returncode == 0: 
    recon(input("Enter the ip: "))
else:
    install_nmap()

