# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import network, senko, machine

OTA = senko.Senko(
  user="Psylenceo", # Required
  repo="ESP32_uPy_testbed", # Required
  branch="master", # Optional: Defaults to "master"
  working_dir="app", # Optional: Defaults to "app"
  files = ["main.py"]
)

updater = network.WLAN(network.STA_IF)
updater.active(True)
updater.connect(<insert network name>, <insert network password>)
while not updater.isconnected():
            pass
    
print()
print('network config:')
print("interface's IP/netmask/gw/DNS addresses")
print(updater.ifconfig())

print()
print("Using Senko to check for firmware updates")

print()
if OTA.fetch():
    print("A newer version is available!")
    print()
    if OTA.update():
        print("Updated to the latest version! Rebooting...")
        machine.reset()
else:
    print("Up to date!")