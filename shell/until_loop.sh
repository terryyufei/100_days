#!/bin/bash

#executes a set of commands until a condition is true

a=0

until [ ! $a -lt 10 ]
do
	echo $a
	a=$(expr $a + 1)
done
