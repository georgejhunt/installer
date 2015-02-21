
How to Install XSCE Offline
===========================

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

get_mydata -- Also gets configured RootFS
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
* Set root password, and create xsce-admin user/password.
* Turn on "keepcache=1" in /etc/yum.conf.
* On a desktop, or laptop, perhaps in a virtual machine, load the FC OS version that will become the target version
** install git, ansible
** clone xsce into /opt/schoolserver, runtags installer
** "./runtags installer" -- lots of downloads, allow 50 minutes, or more if slow internet connection -- only takes long time first time populating cache.
* Start up Tiny Core.
* Got to /mnt/sdb2/tce, and run "fetch_target". Supply ARCH and filename (netinst).
* Move the USB stick back to desktop, and run get_mydata, which copies the rootfs to the cache, and also to unleashkids.org.

