# Linux command line to *install* and *run* apps

Hey guys,
Here is some command lines to *install* and *run* apps in *Ubuntu Linux* terminal:

**Attention**: Always run **sud apt update && sudo apt full-upgrade** or **sudo apt-get update && sudo apt-get upgrade** before installing any new application to download package information from all configured sources at */etc/apt/sources.list* file.


1. **Visual Studio Code**, a modern code editor

	Execution: `code`\
	Installation:
		
	
		sudo apt install code
	
2. **Typora**, a markdown editor

    Execution: `typora`\
    Installation: 
	
		sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
		sudo add-apt-repository 'deb https://typora.io ./linux/'
		sudo apt update
		sudo apt install typora
	
3. **Eclipse IDE**, the most widely used Java integrated development environment (IDE)

    Execution: `eclipse`\
    Installation: 
    
		sudo apt install default-jre
		sudo snap install --classic eclipse
	
4. **Skype**, 

   Execution: `skype` or `skypeforlinux`\
   Installation: 
   >	From *snap* repository: 

   		sudo snap install skype --classic