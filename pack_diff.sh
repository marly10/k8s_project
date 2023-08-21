#!/bin/bash

# Remote server details
# make these more dynamic
remote_user="ubuntu"
remote_ip="ec2-204-236-166-123.us-west-1.compute.amazonaws.com"
remote_path="/home/ubuntu/installed_packages.txt"
ssh_key="/Users/triciamckenzie/.ssh/new_key.cer"

# Local file details
local_path="/Users/triciamckenzie/Public/installed_packages.txt"

# Temporary local file for comparison
temp_local_path="/tmp/installed_packages.txt"

# Copy remote file to temporary local file
scp -i $ssh_key $remote_user@$remote_ip:$remote_path $temp_local_path

# Compare the contents of the remote and local files
diff_output=$(diff $temp_local_path $local_path)

# Check if there are differences
if [ -n "$diff_output" ]; then
    echo "Files are different. Deleting old file and copying new file..."
    rm $local_path
    scp -i $ssh_key $remote_user@$remote_ip:$remote_path $local_path
else
    echo "Files are the same. No need to copy."
fi

# Clean up temporary local file
rm $temp_local_path
