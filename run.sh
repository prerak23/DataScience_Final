#!/bin/bash
if [ $1 = 'i' ]
then
	oarsub -q production -p "GPU <> 'NO'" -l "nodes=1,walltime=$2" -I
elif [ $1 = 'p' ]
then 
	oarsub -q production -p "GPU <> 'NO'" -l "nodes=1,walltime=$2" /home/psrivastava/DataScience/DataScience_Final/get_text.py
else
	echo nothing
fi



