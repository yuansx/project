TSEERAPI_INSTALL_PATH=/data/tseer_test/Tseer/api/cplus
CCFLAGS=--std=c++11 -g
LIBS=-ltseerapi

all: agentApi_single agentApi_multi pureApi_single pureApi_multi

agentApi_single: agentApi_single.o
	g++ -L${TSEERAPI_INSTALL_PATH}/lib $< -o $@ ${LIBS}

agentApi_multi: agentApi_multi.o
	g++ -L${TSEERAPI_INSTALL_PATH}/lib $< -o $@ ${LIBS}

pureApi_single: pureApi_single.o
	g++ -L${TSEERAPI_INSTALL_PATH}/lib $< -o $@ ${LIBS}

pureApi_multi: pureApi_multi.o
	g++ -L${TSEERAPI_INSTALL_PATH}/lib $< -o $@ ${LIBS}

%.o: %.cc
	g++ -I ${TSEERAPI_INSTALL_PATH}/include ${CCFLAGS} -c $< -o $@ ${LIBS}

clean:
	rm -rf routersCache agentApi_single agentApi_multi pureApi_multi pureApi_single *.o
