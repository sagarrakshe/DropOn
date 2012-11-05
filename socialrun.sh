#!/bin/sh
#
# clone this repository after merging all requests
# Create  mountdir if not present
mkdir -p mountdir
# Mount socialfs direcotry
# -o nonempty suggests directory can be nonempty also
./socialfs.py -o nonempty  mountdir
#
#Check /home/$USER/social.log
# After mounting for all filesystem logs
#
#


#
#Right now socialrun is under test ,after whole package is complete
#socialrun will be final executable for user
