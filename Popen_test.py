#!/usr/bin/env python3

import subprocess
#child1 = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
#child2 = subprocess.Popen(['wc'], stdin=child1.stdout, stdout=subprocess.PIPE)
#out = child2.communicate()
#print(out)

def test_popen():
    child = subprocess.Popen(['mysql','-uroot','-pJcloud00'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = child.communicate(input=b'use test;\n show tables;\nexit\n')
    print(stdout.decode())

if __name__ == '__main__':
    test_popen()


