#!/bin/bash

# remember to do:
#voms-proxy-init --voms $VO

for wms in $(lcg-infosites  wms ); do
export GLITE_WMS_WMPROXY_ENDPOINT=$wms
    for ce in $(lcg-infosites  ce | awk '{print $6}'); do 
	glite-wms-job-submit  -a -o jobIDfile  -r $ce helloworld.jdl 
    done
done

# Then to check job status do:
#glite-wms-job-status -i jobIDfile

# THen get output with:
#glite-wms-job-output -i jobIDfile
