
helloworld.o:helloworld.c
	gcc -c helloworld.c -o helloworld.o

func.o:func.c
	gcc -c func.c -o func.o

ALL:helloworld.o func.o
	gcc helloworld.o func.o -o helloworld -Wall 

clean:
	rm -rf helloworld *.o *.tgz target

tar:
	mkdir target -p
	cp helloworld target
	tar zcvf target.tgz target
