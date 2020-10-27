#!/bin/bash

BASE_NAME="base"

for BRANCH in $(ls .git/refs/heads);
do
    git checkout $BRANCH
    git merge -m "Merged commits in $BASE_NAME into branches" $BASE_NAME
    if [ $? -ne 0 ]
    then
	echo MERGE PROBLEM! Check git output and resolve, then rerun this script
	exit 1
    fi
    git push origin $BRANCH

done

git checkout $BASE_NAME

