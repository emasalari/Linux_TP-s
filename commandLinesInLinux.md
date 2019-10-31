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
   >	From *the Skype website*
   
			lscpu: to fetch CPU details from the files sysfs and /proc/cpuinfo
			sudo dpkg --add-architecture i386: to enable multiarch in order to achieve better compatibility for programs on your 64-bit Ubuntu system	
			wget https://repo.skype.com/latest/skypeforlinux-64.deb
			sudo apt-get install gdebi: installing the downloaded .deb package
			sudo gdebi skypeforlinux-64.deb: download the Skype package through gdebi