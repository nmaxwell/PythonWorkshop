
import os
os.system("g++ -O3 LinAlg.c -c -fPIC")

#Mac OSX:
os.system("g++ -dynamiclib -arch x86_64 -current_version 1.0 LinAlg.o -o liblinalg.dynlib ")

#Linux:
#os.system("g++ -shared -Wl,-soname,liblinalg.so.1 -o liblinalg.so.1.0 LinAlg.o")


