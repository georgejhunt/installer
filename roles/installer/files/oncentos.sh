#!/bin/bash -x
# run this script after stock install of CentOS

# Absolute path to this script.
SCRIPT=$(readlink -f $0)
# Absolute path this script is in.
SCRIPTPATH=`dirname $SCRIPT`

yum install -y git ansible tree vim mlocate

mkdir -p /opt/schoolserver
cd /opt/schoolserver
git clone https://github.com/XSCE/xsce --depth 1
cd xsce
./runtags download,download2

# create a grub config file that uses devices rather than UUIDs
grep UUID /etc/default/grub
if [ $? -ne 0 ]; then
  echo GRUB_DISABLE_UUID=true >> /etc/default/grub
fi
grub2-mkconfig -o /boot/grub2/grub.cfg

echo "all done"
