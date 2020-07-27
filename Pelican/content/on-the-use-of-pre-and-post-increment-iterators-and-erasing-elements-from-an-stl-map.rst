on the use of pre- and post- increment iterators, and erasing elements from an STL map
######################################################################################
:date: 2008-03-06 12:28
:author: sameer
:category: Uncategorized
:tags: cplusplus, iterators, programming
:slug: on-the-use-of-pre-and-post-increment-iterators-and-erasing-elements-from-an-stl-map
:status: published

After spending a tense 2-3 hours trying to track down a segmentation fault, here's what I found. The explanation is subtle and obscure enough to be documented in every text book that ever claims to teach "proper" C/C++ programming practices! Maybe they already do that, and I didn't happen to read the right books. I do admit to learning most of my programming skills on the fly from existing good code.

Consider the following function calls:

#. ``f(++i);``
#. ``f(i++);``

Common understanding of these calls translates them to the following:

#. ``i += 1; f(i);``
#. ``f(i); i += 1;``

But that is not so! The post-increment operator used in the second call behaves in a more complicated way! What it really does, is to increment ``i`` *after* the arguments to ``f()`` are created, but *before* the function is called. Thus the correct translation of the second function call is:

``temp = i; i += 1; f(temp);``

This doesn't look too different, but the subtlety involved would have saved me those couple of hours wasted in debugging. It happened when I was iterating over an STL map and wanted to delete some members, as follows, in pseudo-code:

``for (map::iterator i = map.begin(); i != map.end(); ++i) {   if (test(i))     erase(i); }``

The problem is that ``map.erase()`` invalidates the iterator passed to it. So the ``++i`` at the start of the next iteration no longer points to a valid iterator. The correct way to do this is:

``for (map::iterator i = map.begin(); i != map.end();) {   if (test(i))     erase(i++);   else     ++i; }``

Note the use of the pre-increment operator in the ``else`` part, since that saves the unnecesary creation of a temp variable. It is definitely a good practice to *always* use the pre-increment operator unless you are sure you need post-increment.

The story doesn't end here. What if ``f()`` expected a reference as its argument? It does receive a temporary copy and any changes the function makes will be lost. But the fact is that it *can't* make those changes. It is important to note that the "translation" involving the variable ``temp`` is just a vague interpretation. That *pseudo-*\ variable ``temp`` is actually an ``rvalue`` and cannot be assigned this way ... it's just a way of showing something that the compiler does internally. The post-increment operator returns an ``rvalue`` and that can only be passed as a ``const`` reference to the function. The function being called has to be declared accordingly!

These facts were learnt from an old `discussion <http://coding.derkeiler.com/Archive/C_CPP/comp.lang.cpp/2004-05/1726.html>`__ that I chanced upon while searching.
