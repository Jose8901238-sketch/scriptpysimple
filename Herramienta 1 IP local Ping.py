import os
import sys

while True:
    print("=== HOLA :) ===")
    print("1. Verificar si un servidor esta vivo")
    print("2. Ver mi ip local")
    print("3. Salir")

    opcion = input("Elige una opcion (1-3: ")
    if opcion == "1":
        print("\n[+] Has elegido la opcion 1: Verificar si el servidor esta vivo.")
        ip = input("Introduce la IP o dominio a verificar: ")
        resultado = os.system(f"ping -c 3 {ip}")
        if resultado != 0:
            print("\n[!] ALGO SALIO MAL. Razones posibles a continuacion:")
            print(" 1. El objetivo tiene un firewall que bloquea paquetes ICMP (Ping).")
            print(" 2. Escribiste mal la IP o el dominio no existe.")
            print(" 3. No tienes conexion a internet.")
    
    elif opcion == "2":
        print("\n[+] Has elegido la opcion 2: Ver IP local.")
        os.system("ip a")
    
    elif opcion == "3":
        print("\n[-] Saliendo del programa... ADIOS!!")
        sys.exit()
    
    else:
        print("\n[!] Opcion no valida. Por favor, elige 1, 2, 3.")