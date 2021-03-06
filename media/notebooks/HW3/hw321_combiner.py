#!/usr/bin/env python
import sys

cur_key = None
cur_count = 0
sys.stderr.write("reporter:counter:Combiner Counters,Calls,1\n")

for line in sys.stdin:
    key, value = line.split()
    if key == cur_key:
        cur_count += int(value)
    else:
        if cur_key:
            print '%s\t%s' % (cur_key, cur_count)
        cur_key = key
        cur_count = int(value)

print '%s\t%s' % (cur_key, cur_count)