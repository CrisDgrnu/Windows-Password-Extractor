import subprocess

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "Perfil de todos los usuarios" in line]

for wifi in wifis:
    results = subprocess.check_output(['netsh','wlan','show','profile',wifi,'key=clear']).decode('Windows-1252').split('\n')
    result = [line.split(':')[1][1:-1] for line in results if "Contenido de la clave" in line] 
    try:
        print(f'name:{wifi},Password:{results[0]}')
    except IndexError:
        print(f'name:{wifi},Password: Cannot be readed!')

print(wifis)