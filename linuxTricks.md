# Linux tricks

Hey guys,
Here is some linux command line tricks, executable in *Ubuntu Linux* terminal:


1. Super key: Opens Activities search
2. Ctrl+Alt+T: Ubuntu terminal shortcut
3. Super+L or Ctrl+Alt+L: Locks the screen
4. Super+D or Ctrl+Alt+D: Show desktop
5. Super+A: Shows the application menu
6. Super+Tab or Alt+Tab: Switch between running applications
7. Super+Arrow keys: Snap windows
8. Super+M or Super+V: Toggle notification tray
9. Super+Space: Change input keyboard (for multilingual setup)
10. Alt+F2: Run console
11. Ctrl+Q or Ctrl+W or Alt+F4: Close an application window
12. Ctrl+Alt+arrow: Move between workspaces
13. Ctrl+Alt+Del: Log out
14. Alt+Esc: as a web dev. You can quickly switch between two applications.
15. cd -: Switch back to the last working directory
16. cd ~ or cd: Go back to home directory
17. ls -l or ll: List the contents of a directory
18. command_1; command_2; command_3: Running multiple commands in one single command
19. command_1 && command_2: Running multiple commands in one single command only if the previous command was successful
20. Ctrl+r search_term: Easily search and use the commands that you had used in the past
21. Ctrl+A and Ctrl+E or Home and End key: Move to beginning or end of line
22. !$ or Alt+. : Reuse the last item from the previous command with !$
23. !! : Reuse the previous command in present command with !!
24. alias gerp=grep: Using alias to fix typos
25. yes | command_or_script: Using yes command for commands or scripts that need interactive response
26. > filename: Empty a file without deleting it
27. grep -Pri Search_Term path_to_directory: Find if there are files containing a particular text
28. pipe: 
29. Shift+Insert: Inserting the copy buffer
30. sudo apt update: 
31. sudo apt upgrade: 
32. sudo apt full-upgrade: 
33. sudo apt update && sudo apt upgrade -y
34. sudo apt install <package_1> <package_2> <package_3>
35. sudo apt install <package_name> --no-upgrade: install a package, but don’t want to upgrade it, if it is already installed.
36. sudo apt install <package_name> --only-upgrade: upgrade a package but don’t want to install it (if it’s not already installed)
37. sudo apt install <package_name>=<version_number>: install a specific version of an application
38. sudo apt purge <package_name>: removes everything related to a package including the configuration files.
39. apt remove: just removes the binaries of a package. It leaves residue configuration files.
40. apt show <package_name>: show information about the given package(s) like its dependencies, installation and download size, different sources the package is available from, the description of the content of the package among other things
41. apt list --upgradeable: see all the packages that have a newer version ready to be upgraded
42. apt list --installed: all the installed packages on the system
43. apt list --all-versions: list all the packages available for your system
44. sudo apt autoremove
45. sudo apt-get autoremove
46. sudo du -sh /var/cache/apt: size of APT cache in Ubuntu
47. sudo apt-get autoclean: remove only the outdated packages
48. sudo apt-get clean: clean out the cache in its entirety
49. du -sh ~/.cache/thumbnails: check the size of thumbnail cache in your user account at the location ~/.cache/thumbnails
50. rm -rf ~/.cache/thumbnails/*: clear the thumbnail cache 
51. sudo dpkg --list 'linux-image*': List all installed Linux kernels 
52. sudo apt-get remove linux-image-VERSION: Removing the old Linux kernels that you manually installed
53. sudo apt-get remove package-name1 package-name2: remove a program
54. du -h /var/lib/snapd/snaps: Shows all the older versions of your snap apps










