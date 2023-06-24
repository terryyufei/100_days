#!/bin/bash

a=0

while [ "$a" -lt 10 ]  #first loop
do
	b="$a"
	while [ "$b" -ge 0 ] #second loop
	do
		echo -n "$b"
		b=$(expr $b - 1)
	done
	echo
	a=$(expr $a + 1)
done
