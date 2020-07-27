No Mono!
########
:date: 2009-07-03 09:31
:author: sameer
:category: Uncategorized
:tags: mammon
:slug: no-mono
:status: published

Almost everyone who uses the Gnome desktop is familiar with one of either Tomboy or F-Spot ... two tools that have become poster boys of the `Mono project <http://www.mono-project.com/>`__. Well, I decided to stop using them. Not only that, I decided to purge the root of evil, which is the Mono project itself from my Desktop. The philosophical and legal mind-bending around Mono is old news for those who are in touch with the times, but I had chosen to ignore all that till now, but not anymore. I just purged Mono and anything that depends on it from my desktop.

What triggered this allergic reaction was a `post on Groklaw <http://www.groklaw.net/article.php?story=2009062823330395>`__ about a patch to the VFAT filesystem in the Linux kernel that circumvents Microsoft's patent on long file names in FAT. The patent is about storing both the long name and the short name of the file on disc. The patch beats that by storing only one of the two. How lame is that!

Here's a bunch of opinions about the whole issue, that started with `Microsoft suing TomTom <http://groklaw.net/staticpages/index.php?page=archives&year=-1&use_s_page=TomTomTL>`__ over eight software patents.

-  | `SFLC: Settled, But Not Over Yet <http://www.softwarefreedom.org/news/2009/mar/30/settled-not-over-yet/>`__

      The FAT filesystem patents on which Microsoft sued are now and have always been invalid patents in our professional opinion. SFLC remains committed to protecting the interests of our clients and the community. We will act forcefully to protect all users and developers of free software against further intimidation or interference from these patents.

-  | `Bruce Perens: Microsoft and TomTom Settle, Justice and Linux Lose <http://itmanagement.earthweb.com/osrc/article.php/12068_3812891_1/Bruce-Perens-Microsoft-and-TomTom-Settle-Justice-and-Linux-Lose.htm>`__

      Justice lost because there's been no trial to overturn the FAT filesystem patents. As venture capitalist Larry Augustin wrote: "Those of us who have PhDs in computer disciplines and have studied operating systems and file systems, don't see anything particularly innovative in FAT or its extension to support longer file names, FAT32."

      And let's not forget Microsoft. All of that talk about interoperability with Linux coming from them? It was just talk, because they've shown that anyone who tries to interoperate with Microsoft technology even as simple as the FAT filesystem will eventially be sued, or pushed into licensing, for their efforts. The way they act, the Microsoft-internal definition of "interoperability" must be "making the whole world owe us."

      And so, you should be wary of FAT, Office Open XML, .NET (including Mono), Silverlight, and of Microsoft's participation in standards committees that don't have a clear royalty-free committment, or, as is the case for Office Open XML, when the royalty-free committment is less than complete. These technologies leave the door open for submarine patents to sink your business.

-  | `Microsoft Roils the World with FAT Patents <http://www.huffingtonpost.com/brian-kahin/microsoft-roils-the-world_b_171985.html>`__

      1. Microsoft has abandoned its long history of not suing on software patents, in order to attack the Linux operating system. (Other patents at issue are specific to GPS systems.)

      5. By demonstrating its willingness to sue a small company, Microsoft can induce others to settle, while undermining confidence in the market for embedded Linux. By contrast, when IBM sought to impress the world with its patent portfolio, it at least picked on Amazon -- a company able to defend itself and with a reputation for asserting patents aggressively. (Remember the one-click ordering patent that Amazon used in its holiday-season attack on Barnes and Noble?).
