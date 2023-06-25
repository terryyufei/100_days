#!/bin/bash

#Define function

Hello(){
	echo "Hello $1 $2"
	return 10
}

#Invoke the function
Hello Terry Sophia

#capture value returned previously
ret=$?
echo "Return value is $ret"
