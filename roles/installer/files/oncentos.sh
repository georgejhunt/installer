#!/bin/bash -x
# run this script after stock install of CentOS

# Absolute path to this script.
SCRIPT=$(readlink -f $0)
# Absolute path this script is in.
SCRIPTPATH=`dirname $SCRIPT`

yum install -y epel-release
yum install -y git ansible tree vim mlocate

mkdir -p /opt/schoolserver
cd /opt/schoolserver
if [ ! -d /opt/schoolserver/xsce ];then
  git clone https://github.com/XSCE/xsce --depth 1
fi
cd xsce
./runtags download,download2
./install-console

echo "all done"
