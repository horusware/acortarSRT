def acortar_tiempo(tiempo, segundos_a_acortar):
    partes = tiempo.split(':')
    horas = int(partes[0])
    minutos = int(partes[1])
    segundos_con_coma = partes[2].replace(',', '.')
    segundos = float(segundos_con_coma)
    
    total_segundos = horas * 3600 + minutos * 60 + segundos
    total_segundos -= segundos_a_acortar
    
    if total_segundos < 0:
        total_segundos = 0
    
    horas_nuevas = int(total_segundos // 3600)
    minutos_nuevos = int((total_segundos % 3600) // 60)
    segundos_nuevos = total_segundos % 60
    
    return '{:02d}:{:02d}:{:06.3f}'.format(horas_nuevas, minutos_nuevos, segundos_nuevos).replace('.', ',')


def acortar_archivo_srt(archivo, segundos_a_acortar):
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    for i in range(len(lineas)):
        if ' --> ' in lineas[i]:
            inicio, fin = lineas[i].strip().split(' --> ')
            inicio_nuevo = acortar_tiempo(inicio, segundos_a_acortar)
            fin_nuevo = acortar_tiempo(fin, segundos_a_acortar)
            lineas[i] = f"{inicio_nuevo} --> {fin_nuevo}\n"

    with open(archivo, 'w') as f:
        f.writelines(lineas)


if __name__ == "__main__":
    archivo_srt = input("Introduce el nombre del archivo SRT: ")
    segundos_a_acortar = float(input("Introduce el número de segundos a acortar: "))

    acortar_archivo_srt(archivo_srt, segundos_a_acortar)
    print("¡El archivo ha sido modificado exitosamente!")
