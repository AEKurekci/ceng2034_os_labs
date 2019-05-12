import os, fnmatch
import time

print("a.txt file last change time:");
a=os.stat('./a.txt');
print(time.ctime(a[7]));
print("-----------------------");
print("b.txt file last change time:");

b=os.stat('./b.txt');
print(time.ctime(b[7]));



print("-----------------------");
print("0.py file last change time:");

time0=os.stat('./0.py');
print(time.ctime(time0[7]));

print("-----------------------");
print(fnmatch.filter(os.listdir('.'), '*.txt'));
