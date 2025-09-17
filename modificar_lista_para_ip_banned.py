def modificar_m3u(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    nuevo_link = "https://raw.githubusercontent.com/TarunG78/livetv/refs/heads/main/1000088748.m3u8"
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            if line.startswith('#EXTINF'):
                f.write(line)  # Escribir la línea de información del canal
            elif line.strip() and not line.startswith('#'):
                f.write(nuevo_link + '\n')  # Reemplazar el enlace por el nuevo

# Utiliza el script
modificar_m3u('lista.m3u', 'lista_modificada.m3u')