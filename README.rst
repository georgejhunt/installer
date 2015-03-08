
How to Install XSCE Offline
===========================

Instructions for Using Image Downloaded from Unleashkids.org
------------------------------------------------------------
The download is 2GB, and with a fairly fast internet connection can take more that 20 minutes. The images are located at http://download.unleashkids.org/xsce/downloads/installer/ 

I discovered that compressing only saved 10%, and added additional complexity to the process.

On a linux machine, once the image is local, copy the image to a USB stick by doing the following
  dd if=<downloaded image file> of=<device name without any partition -- for example /dev/sdb> bs=1M

Once the USB is available, set the loader to boot in MBR (perhaps called legacy) mode, and set the boot preference to boot first from USB stick.

The USB stick is relatively dangrous is left laying around. If a machine is set to boot from USB stick, and if this USB stick is in the machine when it is booting, it would wipe out whatever is on the hard disk.  So I have forced the user to have a monitor, and keyboard attached, and to confirm that the hard disk should be 'erased'.

The initial image may need some tweaking so that the networking autocofigures correctly. After initial boot, log on as root with passwork fedora, connect the network adapters that will be used, and run the following commands::
  
  cd /opt/schoolserver/xsce/
  ./runtags prep,network,gateway

 
Overall Strategy
----------------
The code for creating an offline install is copied by ansible to {{ XSCE_BASE }}/xsce/scripts/installer/.

The script "mkstick" downloads Tiny Core Linux, and some version of a root file system for installation onto a USB stick. By default, "mkstick" downloads the "netinst" version of the Fedora Core version that is currently used by XSCE. The "PAYLOAD" variable specifies the name of the rootfs that will be incorporated in the stick.

The installation,performed by the USB stick onto the target machine, can be either 32bit or 64bit, and can install loaders that use mbr, or UEFI, firmware loaders.

After the "netinst" version has been copied by Tiny Core onto the target machine, and after the target machine is configured to the satisfaction of the user, the USB stick is used as a shuttle to bring the configured version of the root file system, back to the cache, on the desktop machine.  That cache is then fully prepared to generate and replicate offline install USB sticks.


Functions of the Various Scripts
++++++++++++++++++++++++++++++++
mkstick
  This is the main script to generate a USB with the Tiny Core loader. It requires that the generating machine be online, and that the operating system be the same as the target machine. if /etc/xsce/imagename exists, but <USB>/tce/tgzimagename does not, then "mkstick" becomes a replicator of offline install sticks from data in the cache.

loadOS
  Is copied onto the USB stick, and run by the Tiny Core operating system to partition, format, and copy the target machine root file system, and set up the boot loader for that OS.

cachify -- Also gets configured RootFS
  Also runs on the Tiny Core OS, to collect up the fully configured target machine so that it may be copied up to the cloud, and downloaded by others, as an offine install. There is interaction which records the fedora version, and architecture (32 or 64 bit) in the file /tce/tgzimagename. Once this file exists, the functin of "mkstick" changes. Thereafter "mkstick" replicates data out of the cache for the purpose of replicating offline install sticks.

extlinux.conf
  This is the boot loader configuration file for the extlinux boot loader which occupies the boot sector of the USB stick

grub.cfg.target
  Grub stands for the Grand Unified Boot loader. The mbr version of the boot loader is copied to the first sector of the hard disk(mbr), and the rest of the grub program is copied to the space just after the master boot record (mbr).
  
  
grub.cfg.target.efi
  An efi (or UEFI) boot loader follows a new standard for the interface between the firmware and the OS loader. The firmware can find what it needs to load if a partition is formated with FAT 32 fomrat, has a special and unique identifier, and it partitioned with gpt partition format.

Reminders for How to Create the Bootable Installer
=================================================
* Download the netinstall versions of Fedora Core. On FC21, these are classified as Server installs.
* "dd" the version (i686 or x86_64) onto a USB stick. (this is normal install onnew hardware)
* Install each, selecting to generate one partition (/). Do not do automatic partitioning, and select "standard" rather than "LVM" partition type.
* Set root password (my first images have root password set to fedora), and create xsce-admin user/password.
* Turn on "keepcache=1" in /etc/yum.conf.

  1. install git, ansible
  #. add network adapter, if gateway autoconfig is wanted
  #. clone xsce into /opt/schoolserver, cd to xsce, runansible
  #. git clone https://github.com/XSCE/installer 
  #. "./runtags installer" 
  #. cd to /opt/schoolserver/xsce/scripts/installer
  #. "./mkstick" -- lots of downloads, allow 50 minutes, or more if slow internet connection -- only takes long time first time populating cache.

* Start up Tiny Core.
* Got to /mnt/sdb2/tce, and run "fetch_target". Supply ARCH and filename (netinst).
* Move the USB stick back to desktop, and run cachify, which copies the rootfs to the cache, and also to unleashkids.org.

Notes for Generating Raspberry Pi 2 Image
=========================================
* Start with minimal FC21 image (kernel,and modules subsitituted at http://www.digitaldreamtime.co.uk/images/Fidora/21/
* Declare the platform in vars/local_vars to be "rpi2"

