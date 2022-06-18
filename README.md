<head>
  <h1 align = "center"><b>Github repo automation</b></h1><br>
</head>

<p align="center"><b>
A bash script that calls the python file that automates the entire process of making a new github repository and doing the initial commit from the local device.
</b>

 &nbsp;
  <br>
  <p align = "center">
    <img src = "Automation logo.png" width = 40%>
</p>
  
## Requirements
- A terminal that can run linux commands (otherwise it wont work)
- Python installed. Also install selenium package by using `pip install selenium`
  
## Arguments
- First argument is the <b>Repo name</b>. Enter proper repo name, ie. No whitespaces and only underscore and so on...
- Second argument is the <b>path to the folder</b> where you want to create this project in your local machine. Eg. `D:/Projects/new_project`

The terminal will exit of any of the parameters are not provided.
  
## How to setup ?
1. Clone the repo to a folder 
2. Move the `gitrepo.sh` shell file from the current folder and put it in your user directory (This is to make the shell file accessible on start of terminal)
3. Make the following changes in the shell script:
    - In `GIT_PATH` variable , add your github userID
    - Uncomment the python file excecution line and add the path of the makeRepo.py file 

4. In the `makeRepo.py` file, add your github <b>username and password</b>

## Automation time !!!
- Open the terminal from anywhere on system.
- enter command `. gitrepo.sh` or `source ~/gitrepo.sh`
- enter `create repo_name_here file_path_here`

