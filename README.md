# BusinessAnalysisScrape # 
This documentation serves as a web scraping outline for anyone working with FitKO and is new to webscraping in python. The documentation provided will go over how to scrape contact information from local businesses for informational purposes only. Note that each scraping project is different and the toolset used will differ based on company needs. The web scraper in this example is written using the scrapy framework and is focused on obtaining general information from fitness centers in NYC. The information is then formatted in a JSON file and CSV file.  

# About # 
The Business Analysis tool is a web scraper built using python and scrapy library to scrape for fitness centers in NYC. The web scraper scrapes for the following information 
1.  Business name 
2.  Location 
3.  Contact information 
4.  Hours of operation 

# Getting Started # 

### Prerequisites ### 
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
##### Activating Virtual Environment ##### 
Once the virtual environment has been created, you will need to activate it before you can install or use packages. Activating the the virtual environment will allow you to place your pip executables in the shells PATH. 

To actiave the virtual environment, you will need to go to your virtual environment directory that was created and then to the Scripts directory. 

```
C:> ./env/Scripts/activate
```

##### Setting Execution Policies in Powershell #####

In the event that the script is not able to activate, you will need to [Set-ExecutionPolicy](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.1) and setting the ExecutionPolicy to RemoteSigned. 
> Powershell's execution policy is a safety feature that controls the conditions under which it loads configuration files and loads scripts. 


```
Set-ExecutionPolicy
   [-ExecutionPolicy] <ExecutionPolicy>
   [[-Scope] <ExecutionPolicyScope>]
   [-Force]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

##### Installing Scrapy ##### 
Now that the virtual environment has been activated, you can start installing packages. The webscraping application will be used to extract information from websites, hence scrapy is used. To install scrapy, the following command is used 
```
C:> pip install scrapy 
```

# Fitness Center Scraping #
##### Creating Project #####

In order to create the webscraping project, you need to use the scrapy command-line tool. In the command line, the following command is used 
```
C:> scrapy startproject <project_name> [project_dir]
```
* ``` startproject: ``` Creates a new project named project_name under the project_dir directory. If the project_dir name was not specified, then it inherits the name of the project_name 

After creating the project, you need to navigate to the project directory using the ```cd``` command. 
```
C:> cd fitnessCenters/business_information 
```
Now you can control and manage the scrapy tools. 

##### Generating Spiders #####

Spiders are classes and are the blueprints in which objects are created. Objects inherit the spiders behaviours 

```
C:> scrapy genspider [-t template] <name> <domain>
```
* ``` name: ``` Creates a unique name for the spider to instantiate. The name must be declared when generating spider as this will allow the scraping process to continue. 
* ``` domain: ``` The domain is the url of the page being scraped. By default, the domain generates the ``` [allowed_domains] ``` and ``` [start_urls] ``` attributes. 





# Built Using # 
* [Python](https://www.python.org/) 
* [JSON](https://www.json.org/json-en.html) 
* [Excel](https://www.microsoft.com/en-us/microsoft-365/excel) 
* [Scrapy](https://www.python.org/) 
