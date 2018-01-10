#!/usr/bin/python3
import sys
current_word = None
current_count = 0
word = None
for line in sys.stdin:
    line = line.strip()
    if '\t' in line:
      word, count = line.split('\t', 1)
      print(word)
    else:
      continue
    try:
        count = int(count)
        print(count)
    except ValueError:
        continue
    if current_word == word:
        current_count += 1
    else:
        if current_word:
            print ('%s\t%s' % (current_word, current_count))
        current_count = 1
        current_word = word
if current_word == word:
    print ('%s\t%s' % (current_word, current_count))
