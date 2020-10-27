#!/bin/bash

BASE_NAME="base"
SHOULD_PUSH=${SHOULD_PUSH:-false}

for BRANCH in $(ls .git/refs/heads);
do
    git checkout $BRANCH
    git merge -m "Merged commits in $BASE_NAME into branches" $BASE_NAME
    if [ $? -ne 0 ];
    then
	echo MERGE PROBLEM! Check git output and resolve, then rerun this script
	exit 1
    fi
    if [ $SHOULD_PUSH == true ]
    then
	git push origin $BRANCH
    fi

done

git checkout $BASE_NAME

