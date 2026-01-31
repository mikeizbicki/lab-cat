'''
This program prints stdin to the screen.
'''
import sys

# Stream data in fixed-size chunks to achieve O(1) memory usage
# regardless of input size, rather than loading entire file into memory


def cat(file):
    while True:
        chunk = file.read(8192)
        if not chunk:
            break
        sys.stdout.buffer.write(chunk)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
