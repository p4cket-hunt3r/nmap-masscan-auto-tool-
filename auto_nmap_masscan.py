import subprocess
import os
import shutil
import platform
import sys

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
            print("[!] Please install Nmap manually from: https://nmap.org/download.html")
        else:
            print("[!] Unsupported OS for automatic Nmap installation.")
    except Exception as e:
        print(f"[-] Error installing Nmap: {e}")

def install_masscan():
    print("[+] Installing Masscan...")
    try:
        if "Android" in os.uname().release:
            print("[!] Masscan is not available in Termux pkg repositories. Skipping Masscan installation.")
        elif platform.system() == "Linux":
            subprocess.run(["sudo", "apt", "install", "masscan", "-y"], check=True)
        elif platform.system() == "Windows":
            print("[!] Please install Masscan manually from: https://github.com/robertdavidgraham/masscan")
        else:
            print("[!] Unsupported OS for automatic Masscan installation.")
    except Exception as e:
        print(f"[-] Error installing Masscan: {e}")

def nmap_scan(target_ip):
    print(f"\n[+] Running Nmap scan on {target_ip}...\n")
    try:
        result = subprocess.run(["nmap", "-sS", "-sV", "-T4", target_ip], capture_output=True, text=True, check=True)
        print("[+] Nmap Scan Result:\n")
        print(result.stdout)
    except Exception as e:
        print(f"[-] Error running Nmap: {e}")

def masscan_scan(target_ip):
    if "Android" in os.uname().release:
        print("[!] Skipping Masscan scan on Termux (Masscan not available).")
        return

    print(f"\n[+] Running Masscan scan on {target_ip}...\n")
    try:
        if platform.system() == "Linux":
            result = subprocess.run(["sudo", "masscan", target_ip, "-p1-65535", "--rate", "1000"], capture_output=True, text=True, check=True)
        elif platform.system() == "Windows":
            result = subprocess.run(["masscan", target_ip, "-p1-65535", "--rate", "1000"], capture_output=True, text=True, check=True)
        else:
            print("[!] Unsupported OS for running Masscan.")
            return

        print("[+] Masscan Scan Result:\n")
        print(result.stdout)
    except Exception as e:
        print(f"[-] Error running Masscan: {e}")

def main():
    print("=== Multi-Stage IP Scanner: Nmap → Masscan ===\n")

    # Check Nmap
    if not is_tool_installed("nmap"):
        install_nmap()
    else:
        print("[+] Nmap is already installed.")

    # Check Masscan
    if not is_tool_installed("masscan") and "Android" not in os.uname().release:
        install_masscan()
    elif "Android" in os.uname().release:
        print("[!] Skipping Masscan check on Termux (not available).")
    else:
        print("[+] Masscan is already installed.")

    target_ip = input("\n[?] Enter target IP address to scan: ").strip()

    if target_ip:
        nmap_scan(target_ip)
        masscan_scan(target_ip)
    else:
        print("[!] No IP entered. Exiting...")

if __name__ == "__main__":
    main()
