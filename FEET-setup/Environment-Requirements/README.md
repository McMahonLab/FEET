# Look through `FEET/Scripts/PipelineScript.txt` to see required bash commands and functionality

### Required command: Readarray
### alternatively, if supported by your server, the script can be modified to the following change:
readarray -t Examples < <()
Examples=$()
## However, you must make sure that variables that are generated as output from another command are being read as variables and not just one long string.

# Other bash requirements:
## basic bash commands
## egrep
## grep
## tr
## awk

# environment dependencies:

Python (Python-2.7.15 works, and probably most others.)
FeGenie (and it's dependencies)
hmmer
diamond
prodigal
blast
r


