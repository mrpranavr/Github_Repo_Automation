#!/bin/bash



create() {
    if [[ $1 == "" ]] ; then
    echo 'Enter repository name as first parameter'
    exit 1
    

    elif [[ $2 == "" ]] ; then
    echo 'Enter destination folder name as second parameter'
    exit 1
    
    else
    GIT_PATH="https://github.com/Enter_github_username_here/"$1".git"

    cd
    # python Enter the path to the python file here and uncomment this line/makerepo.py $1 $2
    cd $2/$1
    git init
    touch README.md
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin $GIT_PATH
    git push -u origin main
    code .
    fi
}

# source ~/newcommand.sh

helpme() {
    echo "first parameter - Repo name. Provide proper repo name, no spaces allowed"
    echo "second parameter - local destination directory path."
}

