TSEERAPI_INSTALL_PATH=/data/tseer_test/Tseer/api/cplus
CCFLAGS=--std=c++11 -g
SRC=$(shell ls *.cc)
LIBS=-ltseerapi

all: $(patsubst %.cc,%, $(SRC))

%: %.o
	g++ -L${TSEERAPI_INSTALL_PATH}/lib $< -o $@ ${LIBS}

%.o: %.cc
	g++ -I ${TSEERAPI_INSTALL_PATH}/include ${CCFLAGS} -c $< -o $@ 

clean:
	rm -rf *.o $(patsubst %.cc,%, $(SRC))
