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

CHAR_W    = 9.59
ART_FS    = 11
ART_LH    = 14
ART_X     = 15
ART_Y0    = 34
PANEL_FS  = 16
PANEL_LH  = 20
PANEL_W   = 54
WIDTH     = 985
HEIGHT    = 530
PANEL_X   = int(WIDTH - 15 - PANEL_W * CHAR_W)
ART_ROWS  = len(ART.split('\n'))
ART_COLS  = max(len(l) for l in ART.split('\n'))

PALETTES = {
    'dark_mode.svg': {
        'bg': '#161b22', 'fg': '#c9d1d9', 'key': '#ffa657', 'value': '#a5d6ff',
        'cc': '#616e7f',
    },
    'light_mode.svg': {
        'bg': '#f6f8fa', 'fg': '#24292f', 'key': '#953800', 'value': '#0a3069',
        'cc': '#c2cfde',
    },
}

def dots(n):
    return ' ' + '.' * max(0, n - 2) + ' ' if n > 2 else {0: '', 1: ' ', 2: '. '}[max(0, n)]


def kv(key, value):
    keys = key.split('.')
    klen = sum(len(k) for k in keys) + (len(keys) - 1)
    kmarkup = '.'.join(f'<tspan class="key">{k}</tspan>' for k in keys)
    d = dots(PANEL_W - 2 - klen - 1 - len(value))
    return (f'<tspan class="cc">. </tspan>{kmarkup}:'
            f'<tspan class="cc">{d}</tspan><tspan class="value">{value}</tspan>')


def rule(label):
    text = f'- {label} '
    return f'<tspan class="hdr">{text}</tspan>' + '\u2014' * max(0, PANEL_W - len(text) - 3) + '-\u2014-'


def title(name):
    return f'<tspan class="key">{name}</tspan> ' + '\u2014' * max(0, PANEL_W - len(name) - 4) + '-\u2014-'


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

PANEL_Y0 = ART_Y0 + (HEIGHT - ART_Y0 - len(PANEL) * PANEL_LH) // 2


def build(palette):
    out = ["<?xml version='1.0' encoding='UTF-8'?>"]
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" '
               f'font-family="ConsolasFallback,Consolas,DejaVu Sans Mono,monospace" '
               f'width="{WIDTH}px" height="{HEIGHT}px" font-size="{PANEL_FS}px">')
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
    out.append('.cc {fill: %s;}' % palette['cc'])
    out.append('.hdr {fill: %s;}' % palette['key'])
    out.append('text, tspan {white-space: pre;}')
    out.append('</style>')
    out.append(f'<rect width="{WIDTH}px" height="{HEIGHT}px" fill="{palette["bg"]}" rx="15"/>')

    out.append(f'<text x="{ART_X}" y="{ART_Y0}" fill="{palette["fg"]}" font-size="{ART_FS}px">')
    for i, line in enumerate(ART.split('\n')):
        out.append(f'<tspan x="{ART_X}" y="{ART_Y0 + i * ART_LH}">{line}</tspan>')
    out.append('</text>')

    out.append(f'<text x="{PANEL_X}" y="{PANEL_Y0}" fill="{palette["fg"]}">')
    for i, line in enumerate(PANEL):
        out.append(f'<tspan x="{PANEL_X}" y="{PANEL_Y0 + i * PANEL_LH}">{line}</tspan>')
    out.append('</text>')
    out.append('</svg>')
    return '\n'.join(out)


if __name__ == '__main__':
    import sys
    dest = sys.argv[1] if len(sys.argv) > 1 else '.'
    art_px = ART_X + ART_COLS * ART_FS * 0.688
    print(f'svg {WIDTH}x{HEIGHT} | art ends ~{art_px:.0f}px | panel x={PANEL_X} | '
          f'art rows {ART_ROWS} -> {ART_Y0 + (ART_ROWS - 1) * ART_LH}px')
    for name, palette in PALETTES.items():
        with open(f'{dest}/{name}', 'w', encoding='utf-8') as f:
            f.write(build(palette))
        print('wrote', name)
