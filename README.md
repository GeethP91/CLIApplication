# Random Number Shuffle CLI Using Python

Building a simple CLI that prints the numbers from 1 to 10 in random orders to the terminal using Python

1.Setup the filesystem structure
  CLIApplication/
   |---> Readme.md
   |---> install.sh
   |---> rndmcli/
         |--->__init__.py
         |--->__main__.py
   |---> setup.py

Name of the CLI can be anything as per your choice. I named it "rndmcli"

2. I am creating the CLI to generate the random numbers in the range between 1 to 10.
   I have one sub-directory "rndmcli" that contains the package
   
   a.__init__.py
     
     The file tells python that directory contains a package. 
     I have kept it empty since I am not initializing the package with a code.

   b.__main__.py
     
     Through the setup configuratin file in the root directory setup.py __main__.py will be indicated as the entry point to the CLI.
     The main file contains the modules that needs to be imported. In this case, I am importing sys and random modules to implement module members like a simple
     random function.
     
3. setup.py
    
   This contains the instructions to python on how to handle it
   a. Importing setup function from setuptools package
   b. Packages argument is a list that indicates all of the include packages. Here the package is name "rndmcli"
   c. entry_points indicates with a string what the application will be called and what shpuld be invoked when called.
      here the application is called rndmcli and when executed it will run the main function in the __main__.py which is part of the rndmcli package.

4 install.sh
   
  To install the Python CLI app is to use pip3. On running "pip3 install -e ." will install the application using the setup.py.
  Only run install.sh script on the machine to install the application andit can be modified to uninstall the application
 

Results in Ubuntu

root@ubuntu:~/CLIApplication# rndmcli
Random List
[8, 3, 5, 7, 6, 4, 1, 0, 9, 2]

root@ubuntu:~/CLIApplication# rndmcli
Random List
[6, 5, 0, 2, 4, 9, 1, 3, 8, 7]

root@ubuntu:~/CLIApplication# rndmcli
Random List
[8, 6, 4, 1, 0, 9, 7, 2, 3, 5]

root@ubuntu:~/CLIApplication# rndmcli
Random List
[2, 5, 0, 4, 7, 1, 6, 9, 8, 3]
  

Steps To Run the CLI
---------------------
git clone https://github.com/GeethP91/CLIApplication.git
cd CLIApplication
run ./install.sh
