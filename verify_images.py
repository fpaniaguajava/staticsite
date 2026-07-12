import urllib.request
urls = [
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/NES-Console-Set.png/1280px-NES-Console-Set.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/SNES-Mod1-Console-Set.png/1280px-SNES-Mod1-Console-Set.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Nintendo_64_Console.jpg/1280px-Nintendo_64_Console.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/GameCube-Console-Set.png/1280px-GameCube-Console-Set.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Wii-Console.png/1280px-Wii-Console.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Wii_U_Console_and_Gamepad.png/1280px-Wii_U_Console_and_Gamepad.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Nintendo_Switch_logo.svg/1280px-Nintendo_Switch_logo.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Original_Xbox_console.jpg/1280px-Original_Xbox_console.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Xbox_360_consoles.png/1280px-Xbox_360_consoles.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Xbox_One_consoles_montage.png/1280px-Xbox_One_consoles_montage.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Xbox_Series_X_S_color.svg/1280px-Xbox_Series_X_S_color.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/PSX-Console-wController.jpg/1280px-PSX-Console-wController.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/PS2-Versions.png/1280px-PS2-Versions.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/PS3_consoles_montage.png/1280px-PS3_consoles_montage.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/PS4-Console-wDS4.jpg/1280px-PS4-Console-wDS4.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Black_and_white_Playstation_5_base_edition_with_controller.png/1280px-Black_and_white_Playstation_5_base_edition_with_controller.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Sega-Master-System-Set.png/1280px-Sega-Master-System-Set.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Sega-Mega-Drive-JP-Mk1-Console-Set.jpg/1280px-Sega-Mega-Drive-JP-Mk1-Console-Set.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Sega-CD-Model1-Set.jpg/1280px-Sega-CD-Model1-Set.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Sega-Saturn-Console-Set-Mk2.png/1280px-Sega-Saturn-Console-Set-Mk2.png',
]
for url in urls:
    req = urllib.request.Request(url, method='HEAD')
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f'{url} -> {resp.status} {resp.getheader("content-type")}')
    except Exception as e:
        print(f'{url} -> ERROR {e}')
