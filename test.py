import subprocess


s = subprocess.run(["ssh", "pi@192.168.16.44", "journalctl", "-f"])
s.stdout.decode()
#stdount = s.communicate()
#print(stdount)