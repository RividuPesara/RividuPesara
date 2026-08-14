#!/usr/bin/env python3

ART = """\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣤⣤⡀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⢰⣿⢋⠈⣿⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠙⠛⠀⣿⡄⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠛⠃⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢾⣿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠟⢿⣿⡿⢿⣿⣿⣿⣿⣿⡟⠛⠛⠛⠛⢻⣿⠉⢹⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠈⠟⣡⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠸⠏⣠⣾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣤⣴⣾⣿⣿⣿⣿⣶⣶⣿⣿⣿⣶⣤⣤⣤⣾⣿⣿⣿⣿⣿⣇⣀⣀⣀⣀⣀⣀⠀
⠀⠀⠀⠀⠸⠟⠛⠛⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠁⠀⠀⠀⠀⠁⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⡶⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠓⠲⠶⠶⠶⠤⣤⣀⠀
⠀⠀⠀⠀⠀⠛⠋⠉⠁⠀⠀⣠⣼⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣯⣄⣀⠀⠀⠀⠀⠀⠀⠈⠁
⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠛⠉⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠉⠀⠀⠀⠉⠙⠳⠶⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

CHAR_W   = 9.59
GUTTER   = 15
BRAILLE_W= 11.0
ART_X    = 15
LINE_H   = 20
ART_Y0   = 30
PANEL_W  = 54
ART_COLS = max(len(l) for l in ART.split('\n'))
ART_ROWS = len(ART.split('\n'))
PANEL_X  = int(ART_X + ART_COLS * BRAILLE_W + GUTTER)
WIDTH    = int(PANEL_X + PANEL_W * CHAR_W + 15)
HEIGHT   = ART_Y0 + ART_ROWS * LINE_H

PALETTES = {
    'dark_mode.svg': {
        'bg': '#282a36', 'fg': '#f8f8f2', 'key': '#ffb86c', 'value': '#8be9fd',
        'add': '#50fa7b', 'del': '#ff5555', 'cc': '#6272a4', 'art': '#bd93f9',
    },
    'light_mode.svg': {
        'bg': '#f5f5f0', 'fg': '#1f1f1f', 'key': '#a34d14', 'value': '#036a96',
        'add': '#14710a', 'del': '#cb3a2a', 'cc': '#a5a5b5', 'art': '#644ac9',
    },
}

def dots(n):
    return ' ' + '.' * max(0, n - 2) + ' ' if n > 2 else {0: '', 1: ' ', 2: '. '}[max(0, n)]


def kv(key, value, vid=None):
    keys = key.split('.')
    klen = sum(len(k) for k in keys) + (len(keys) - 1)
    pad = PANEL_W - 2 - klen - 1 - len(value)
    kmarkup = '.'.join(f'<tspan class="key">{k}</tspan>' for k in keys)
    d = dots(pad)
    if vid:
        return (f'<tspan class="cc">. </tspan>{kmarkup}:'
                f'<tspan class="cc" id="{vid}_dots">{d}</tspan>'
                f'<tspan class="value" id="{vid}">{value}</tspan>')
    return (f'<tspan class="cc">. </tspan>{kmarkup}:'
            f'<tspan class="cc">{d}</tspan><tspan class="value">{value}</tspan>')


def rule(label):
    text = f'- {label} ' if label else ''
    return f'<tspan class="hdr">{text}</tspan>' + '—' * max(0, PANEL_W - len(text) - 3) + '-—-'


def title(name):
    return f'<tspan class="key">{name}</tspan>' + ' ' + '—' * max(0, PANEL_W - len(name) - 4) + '-—-'


BLANK = '<tspan class="cc">. </tspan>'

PANEL = [
    title('rividu@pesara'),
    kv('OS', 'Windows, Linux'),
    kv('Languages', 'Python, Rust, TypeScript, Dart, Ruby'),
    kv('Databases.SQL', 'PostgreSQL, MySQL, SQLite'),
    kv('Databases.NoSQL', 'MongoDB, Firebase'),
    kv('Focus', 'AI/ML, Web, Mobile'),
    BLANK,
    kv('Hobbies.Media', 'Anime, Manga, Manhwa, Light Novels'),
    kv('Hobbies.Gaming', 'Video Games, Board Games'),
    kv('Hobbies.Other', 'Gym, DIY Cards'),
    kv('Hobbies.Code', 'Exploring Open Source'),
    BLANK,
    rule('Contact'),
    kv('Email', 'pesarauniversity@gmail.com'),
    kv('LinkedIn', 'rivindu-pesara-myprofile'),
    kv('GitHub', 'RividuPesara'),
    kv('Portfolio', 'rividupesara-portfolio.vercel.app'),
]

PANEL_Y0 = ART_Y0 + ((ART_ROWS - len(PANEL)) // 2) * LINE_H


def build(palette):
    art_lines = ART.split('\n')
    out = []
    out.append("<?xml version='1.0' encoding='UTF-8'?>")
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" '
               f'font-family="ConsolasFallback,Consolas,DejaVu Sans Mono,monospace" '
               f'width="{WIDTH}px" height="{HEIGHT}px" font-size="16px">')
    out.append('<style>')
    out.append("@font-face {")
    out.append("src: local('Consolas'), local('Consolas Bold');")
    out.append("font-family: 'ConsolasFallback';")
    out.append('font-display: swap;')
    out.append('-webkit-size-adjust: 109%;')
    out.append('size-adjust: 109%;')
    out.append('}')
    out.append('.key {fill: %s;}' % palette['key'])
    out.append('.value {fill: %s;}' % palette['value'])
    out.append('.addColor {fill: %s;}' % palette['add'])
    out.append('.delColor {fill: %s;}' % palette['del'])
    out.append('.cc {fill: %s;}' % palette['cc'])
    out.append('.hdr {fill: %s;}' % palette['key'])
    out.append('.ascii {fill: %s;}' % palette['art'])
    out.append('text, tspan {white-space: pre;}')
    out.append('</style>')
    out.append(f'<rect width="{WIDTH}px" height="{HEIGHT}px" fill="{palette["bg"]}" rx="15"/>')

    out.append(f'<text x="{ART_X}" y="{ART_Y0}" class="ascii">')
    for i, line in enumerate(art_lines):
        out.append(f'<tspan x="{ART_X}" y="{ART_Y0 + i * LINE_H}">{line}</tspan>')
    out.append('</text>')

    out.append(f'<text x="{PANEL_X}" y="{PANEL_Y0}" fill="{palette["fg"]}">')
    for i, line in enumerate(PANEL):
        out.append(f'<tspan x="{PANEL_X}" y="{PANEL_Y0 + i * LINE_H}">{line}</tspan>')
    out.append('</text>')
    out.append('</svg>')
    return '\n'.join(out)


if __name__ == '__main__':
    import sys
    dest = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(f'art: {ART_COLS} cols x {ART_ROWS} rows | panel x={PANEL_X} | svg {WIDTH}x{HEIGHT}')
    for name, palette in PALETTES.items():
        with open(f'{dest}/{name}', 'w', encoding='utf-8') as f:
            f.write(build(palette))
        print('wrote', name)
