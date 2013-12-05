voms-backup-server-testing
==========================

## Instructions for testing the new VOMS servers

This setup assumes that you are testing on a configured UI, and that you
have your user cert all ready to go. If you can do:

'''bash
voms-proxy-init --voms vo.southgrid.ac.uk
'''

(for example) and get a SouthGrid VO proxy, then you should be able to use
these files to test the other two VOMS servers without reconfiguring the
UI.

### Step 1

Set the X509_VOMS_DIR variable to point to the included `vomsdir`. E.g., if
you are in the directory containing this README file:

'''bash
export X509_VOMS_DIR=$(pwd)/vomsdir
'''

### Step 2

Test the Oxford VOMS server:

'''bash
voms-proxy-init --debug  --vomses ./voms02/vo.southgrid.ac.uk  --voms vo.southgrid.ac.uk
'''

(change the appropriate VO name bits to refer to a VO of which you are a
member)
 
### Step 3

Test the Imperial VOMS server:

'''bash
voms-proxy-init --debug  --vomses ./voms03/vo.southgrid.ac.uk  --voms vo.southgrid.ac.uk
'''

### Step 4

Please fill in the results on the wiki page:

* [https://www.gridpp.ac.uk/wiki/VOMSdeployment2013#Test_Status]

Finally, if you are a member of more than one of the GridPP VOMS hosted
VOs, return to step 2 and repeat for the other VO(s).
