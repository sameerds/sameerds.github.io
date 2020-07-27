The Debian chroot install
#########################
:date: 2003-08-11 12:11
:author: sameer
:category: Uncategorized
:tags: computers
:slug: the-debian-chroot-install
:status: published

| The setting:
| Existing Debian unstable installation on a 20GB hard-disk, and a new 40GB hard-disk with a small Windows partition.

| The task:
| Installing Debian on the new hard-disk and shifting over to it in the "near future". But I want to do this without having to go through the painful bootable CD and stuff. Also, I have already partitioned the new hard-disk and formatted it with Reiserfs 3.6, which is unfortunately not supported by my old, kernel 2.2 based Debian boot CD.
| 
| The process:
| As Karsten M. Self at `TwikiIWeThey <http://twiki.iwethey.org/twiki/bin/view/Main/DebianChrootInstall>`__ says ...

   On the other hand, if you're experience with Debian, bored with convention, interested in a new challenge or feel that this method suits your current situation, read on. This method works in instances where a traditional Debian install doesn't, or would not be appropriate.

But actually I took his advice and decided to follow the `section <http://www.debian.org/releases/stable/i386/ch-preparing.en.html#s-linux-upgrade>`__ on "zero-downtime" "cross-root" install in the Debian Installation Manual.

| Hard-disk partitions mounted under /mnt/debinst
| ``apt-get install debootstrap``
| The ``debootstrap`` manual open in MozillaFirebird
| *and so it begins ...*
