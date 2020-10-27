#!/bin/bash

BASE_NAME="base"

for BRANCH in $(ls .git/refs/heads);
do
    git checkout $BRANCH
    git merge -m "Merged commits in $BASE_NAME into branches" $BASE_NAME
    if [ $? -eq 0 ]
    then
	git push origin $BRANCH
    fi
done

git checkout $BASE_NAME

