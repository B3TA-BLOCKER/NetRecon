from time import sleep
import os 
import subprocess
import platform


try:
    import distro
except ImportError:
    print("The 'distro' package is required for Linux distribution detection. Install it using 'pip install distro'")
    exit(1)

def install_nmap() -> bool:
    os_type = platform.system().lower()
    try:
        if os_type == 'linux' :
            distro = distro.name().lower()
            if 'ubuntu' in distro or 'debian' in distro :
                subprocess.run(['sudo', 'apt-get' , 'update'], check =True)
                subprocess.run(['sudo' , 'apt-get' , 'install' , '-y' , 'nmap'],check=True)
            elif 'fedora' in distro or 'centos' in distro or 'rhel' in distro:
                subprocess.run(['sudo', 'dnf', 'install' , '-y' , 'nmap'],check=True)
            else:
                print(f"Unsupported Linux Distribution : {distro}")
                return False
        elif os_type == 'darwin':  # macOS
            try:
                subprocess.run(['brew', '--version'], check=True)
                subprocess.run(['brew', 'install', 'nmap'], check=True)
            except subprocess.CalledProcessError:
                print("Homebrew is not installed. Please install Homebrew first.")
                return False
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
    # -A option enables "Aggressive Scan" mode. 
    # -p- option specifies that nmap should scan all 65,535 TCP ports (from 1 to 65535). 
    # -Pn option disables host discovery. {Nmap will assume that the host up}
    # -v option stands for verbose mode 


ip_address = input("Enter the ip: ")
result = subprocess.run(['nmap', '--version'])

try:
    if result.returncode == 0:
        recon(ip=ip_address)
    else:
        print("Nmap is not installed yet")
        sleep(1)
        print("Installing Nmap ", end='')
        for i in range(10):
            sleep(0.5)
            print(".",end='', flush=True)
        if install_nmap():
            recon(ip=ip_address)
except subprocess.CalledProcessError as e:
    print(f"An Error occured during Installation: {e}")
except OSError as e:
    print(f"An OS-related error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
