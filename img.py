# Convert image to Alto format

from PIL import Image
import sys

# Substitute desired name below
file = "/Users/ken/Desktop/alto2.jpg"

im = Image.open(file)

max = 576 + 32
max = 606
w, h =  im.size
h = h * max / w
w = max
print 'words:', (w + 15) / 16 * h
im = im.resize((w, h))
im = im.convert(mode="L")
im = im.convert(mode="1")

pixels = list(im.getdata())
f = open('img', 'w')

def toWord(n):
  return chr(n >> 8) + chr(n & 255)
f.write(toWord(w))
f.write(toWord(h))

wordsPerLine = (w + 15) / 16

print 'w: %d, h: %d, wordsPerLine: %d' % (w, h, wordsPerLine)
print 'length should be', (wordsPerLine * h + 2) * 2
for y in range(0, h):
  data = [0] * wordsPerLine
  for x in range(0, w):
    if pixels[y*w+x] == 255:
      data[x / 16] |= 1<<(15 - (x & 15))
  f.write(''.join(map(toWord, data)))
