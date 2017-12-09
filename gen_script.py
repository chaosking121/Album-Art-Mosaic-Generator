import os

if __name__ == '__main__':

    entries = set()

    with open('actual.txt', 'r') as playlist, open('parsed.sh', 'w') as output:

        output.write('#!/usr/bin/env bash\n\n')

        for line in playlist:
            try:
                sections = line.split('/')

                artist = sections[3]

                album = sections[4]
                album = album[album.find('] ') + len('] ') : album.find(' (Disc')]

                artist = ''.join([c for c in artist if c.isalpha() or c.isdigit() or c==' ']).rstrip()
                album = ''.join([c for c in album if c.isalpha() or c.isdigit() or c==' ']).rstrip()

                entries.add((artist, album))

            except UnicodeDecodeError:
                pass

        for (artist, album) in entries:
            output.write('sacad "{}" "{}" 500 pics/{}.png >> /dev/null\n'.format(artist.lower(), album.lower(), album.replace(' ', '_').lower()))

    os.chmod('parsed.sh', 0o744)