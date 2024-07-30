import os 


def recon(ip):
    os.system(f"nmap -A -p- -Pn {ip} -v")
    os.system(f"dirb {ip}")


recon(input("Enter the ip: "))
