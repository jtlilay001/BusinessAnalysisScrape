# BusinessAnalysisScrape # 
This documentation serves as a web scraping outline for anyone who is working with FitKO and is new to webscraping or programming in python. The documentation provided will go over how to scrape contact information from businesses for marketing purposes. Note that each scraping project is different and the toolset used will differ based on company needs. The web scraping application for this purpose is written using the scrapy fraamework and is focused on obtaining contact information for fitness centers in NYC.  

# About # 
The Business Analysis tool is a web scraper built using python to scrape for fitness centers in NYC. The web scraper was built using the scrapy framework and scrapes for the following information 
1.  Business name 
2.  Location 
3.  Contact information 
4.  Hours of operation. 

The program uses the location of the fitness center and saves it inside a county list. 

# Getting Started # 
##### Installing Python
Before starting the web scraping process, Python first needs to be installed; this can be done by downloading python directly from their website [python](https://www.python.org/downloads/). After installing python, make sure that python is installed by running the local command on the command line. 
```
C:> py --version
```
##### Installing Pip #####
After succesfully installing python, you can check to see whether the package installer for python has been installed. This is done by running the following command on the command line 
```
C:> py -m pip --version 
```
If you received an error, saying that pip is not recognized or installed, you will need to isntall pip. There are two ways of installing pip, the first includes the use of a module called [ensurepip](https://docs.python.org/3/library/ensurepip.html#module-ensurepip), while the second alternative involves the use of [get-pip.py](https://github.com/pypa/get-pip).  

##### Creating a directory #####
Package modules are often installed within a virtual environment. The virtual environment is used to manage packages for different projects. By installing a virtual environment, you are preventing python packages from installing globally which could break any existing projects if they're using different versions of the same package. 

A virtual environment is created in a directory. The directory can be created using the ```mkdir``` command in the command line. After creating the directory, you can change the directory to the newly created directory using the ```cd``` command. 

##### Installing Virtualenv #####
After creating the directory, you can go ahead and install the virtual environment. Depending on the version of python that you installed, the command will differ. For users using Python 2, you need to install a virtual environment before creating a virtual environment. The following command is used to install the virtual environment 

```
C:> py -m pip install --user virtualenv
```
If you are using Python 3, then you can use the ```venv``` module which will create and manage the virtual environment for your project. 

##### Creating Virtual Environment #####
To create a virtual environment in the project directory, run ```virtualenv``` or ```venv``` followed by the name of the virtual environment. Note that the name of the virtual environment can be called whatever you want depending on the version of python that you're using. 

```
C:> py -m venv env
```

To actiave the virtual environment, you will need to go to your virtual environment directory that was created and then to the Scripts directory. 

```
C:> ./env/Scripts/activate
```
##### Setting Execution Policies in Powershell #####

In the event that the script is not able to activate, you will need to [Set-ExecutionPolicy](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.1) 
> Powershell's execution policy is a safety feature that controls the conditions under which it loads configuration files and loads scripts. 
It’s intended to prevent any malicious scripts from running. In order to enable the virtual environment, the RemoteSigned policy needs to be enforced. The RemoteSigned policy allows scripts to run. 

```
Set-ExecutionPolicy -ExecutionPolicy <PolicyName> -Scope <scope>
```

##### Activating Virtual Environment ##### 
Once the virtual environment has been created, you will need to activate it before you can install or use packages. Activating the the virtual environment will allow you to place your pip executables in the shells PATH. 


##### Installing Scrapy ##### 






# Built Using # 
* [Python](https://www.python.org/) 
* [Excel](https://www.microsoft.com/en-us/microsoft-365/excel) 
* [Scrapy](https://www.python.org/) 
