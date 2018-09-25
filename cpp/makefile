CCFLAGS=--std=c++11 -g

SRC=$(shell ls *.cc)

all: $(patsubst %.cc,%, $(SRC))

%: %.o
	g++ $< -o $@

%.o: %.cc
	g++ ${CCFLAGS} -c $< -o $@

clean:
	rm -rf *.o $(patsubst %.cc,%, $(SRC))
