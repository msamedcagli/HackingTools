import subprocess
import optparse

# Argument parser
parse_object = optparse.OptionParser()
parse_object.add_option("-i", "--interface", dest="interface", help="Interface to change")
parse_object.add_option("-m", "--mac", dest="mac_address", help="New MAC address")

(user_inputs, arguments) = parse_object.parse_args()

# Input validation
if not user_inputs.interface:
    print("[-] Please specify an interface. Use --help for more info.")
    exit()
if not user_inputs.mac_address:
    print("[-] Please specify a MAC address. Use --help for more info.")
    exit()

user_interface = user_inputs.interface
user_mac_address = user_inputs.mac_address

print("[+] Changing MAC address of {} to {}".format(user_interface, user_mac_address))

try:
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])
    print("[+] MAC address was successfully changed.")
except subprocess.CalledProcessError:
    print("[-] Failed to change MAC address. Are you running as root?")
