import os
# Очиска экрана
def clear_screen():
    # Для Windows
    if os.name == 'nt':
        os.system('cls')
    # Для Linux и macOS
    else:
        os.system('clear')
