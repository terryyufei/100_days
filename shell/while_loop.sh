#!/bin/bash

#execute a set of command repeatedly until some condition occurs

a=0

while [ $a -lt 10 ]
do
	echo $a
	a=$(expr $a + 1)
done
