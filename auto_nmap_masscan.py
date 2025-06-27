import subprocess
import os
import shutil
import platform

def is_tool_installed(tool):
    return shutil.which(tool) is not None

def install_nmap():
    print("[+] Installing Nmap...")
    try:
        if "Android" in os.uname().release:
            subprocess.run(["pkg", "install", "nmap", "-y"], check=True)
        elif platform.system() == "Linux":
            subprocess.run(["sudo", "apt", "install", "nmap", "-y"], check=True)
        elif platform.system() == "Windows":
            print("[!] Please install Nmap manually from https://nmap.org/download.html")
        else:
            print("[!] Unsupported OS for automatic Nmap installation.")
    except Exception as e:
        print(f"[-] Error installing Nmap: {e}")


def install_masscan():
    print("[+] Installing Masscan...")
    try:
        if "Android" in os.uname().release:
            subprocess.run(["pkg", "install", "masscan", "-y"], check=True)
        elif platform.system() == "Linux":
            subprocess.run(["sudo", "apt", "install", "masscan", "-y"], check=True)
        elif platform.system() == "Windows":
            print("[!] Please install Masscan manually from https://github.com/robertdavidgraham/masscan")
        else:
            print("[!] Unsupported OS for automatic Masscan installation.")
    except Exception as e:
        print(f"[-] Error installing Masscan: {e}")
        def nmap_scan(target_ip):
    print(f"[+] Running Nmap scan on {target_ip}...")
    try:
        subprocess.run(["nmap", "-sS", "-sV", "-T4", target_ip])
    except Exception as e:
        print(f"[-] Error running Nmap: {e}")

def masscan_scan(target_ip):
    print(f"[+] Running Masscan scan on {target_ip}...")
    try:
        subprocess.run(["sudo", "masscan", target_ip, "-p1-65535", "--rate", "1000"])
    except Exception as e:
        print(f"[-] Error running Masscan: {e}")

def main():
    print("=== Multi-Stage IP Scanner: Nmap → Masscan ===\n")

    # Tool Check: Nmap
    if not is_tool_installed("nmap"):
        install_nmap()
    else:
        print("[+] Nmap is already installed.")

    # Tool Check: Masscan
    if not is_tool_installed("masscan"):
        install_masscan()
    else:
        print("[+] Masscan is already installed.")

    # Now ask for IP
    target_ip = input("\nEnter target IP to scan: ")

    # Run Scans
    nmap_scan(target_ip)
    masscan_scan(target_ip)

    print("\n[+] Scanning complete!")

if __name__ == "__main__":
    main()
