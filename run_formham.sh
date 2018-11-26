#!/bin/bash

#to kill the whitespaces in names
#for f in *; do mv "$f" `echo $f | tr ' ' '_'`; done


for i in `seq 1 2581`;
do
	python formham.py $i
done 
