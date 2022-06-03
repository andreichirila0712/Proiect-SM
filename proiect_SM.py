import serial.tools.list_ports
import numpy as np

cod_scanat = np.empty(8, int)
matrice_coduri = np.array([[0, 0, 0, 1, 1, 1, 0, 1],
                           [0, 1, 0, 1, 1, 0, 1, 1],
                           [0, 1, 0, 1, 1, 1, 0, 1],
                           [0, 1, 1, 0, 1, 1, 0, 1],
                           [1, 0, 0, 1, 1, 1, 0, 1],
                           [1, 0, 1, 0, 1, 1, 0, 1],
                           [1, 0, 1, 1, 1, 0, 0, 1],
                           [1, 1, 0, 1, 1, 1, 0, 1]])

n = 0  # de cate ori s-a trecut prin senzor
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("select Port: COM")

for x in range(0, len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

while n < 8:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        cod_scanat[n] = packet.decode('utf')
        n = n + 1
        print(packet.decode('utf').rstrip('\n'))


if (np.array_equal(matrice_coduri[0], cod_scanat) or np.array_equal(matrice_coduri[1], cod_scanat)
        or np.array_equal(matrice_coduri[2], cod_scanat) or np.array_equal(matrice_coduri[4], cod_scanat)
        or np.array_equal(matrice_coduri[5], cod_scanat) or np.array_equal(matrice_coduri[6], cod_scanat)
        or np.array_equal(matrice_coduri[7], cod_scanat)):
    serialInst.write('1'.encode())
else:
    serialInst.write('0'.encode())

print(cod_scanat)