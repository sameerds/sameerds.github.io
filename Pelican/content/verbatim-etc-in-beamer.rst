verbatim, etc. in beamer
########################
:date: 2009-07-02 16:32
:author: sameer
:category: Uncategorized
:tags: beamer, latex, presentations
:slug: verbatim-etc-in-beamer
:status: published

I have been unsuccessful at creating a ``verbatim`` environment in a beamer frame. The manual says that it is fully supported, and all you have to do is set the ``[fragile]`` argument for that slide. So the following is supposed to work. (Note the weird indenting, since ``verbatim`` has to be at the beginning of the line.)

::

     begin{frame}[fragile]
       frametitle{Euclid says ``hello''}
       begin{verbatim}
   blah...
   and blah...
   end{verbatim}
     end{frame}

Well, I tried compiling it, and it doesn't. LaTeX exits with the following error.

::

   Runaway argument?
   ! File ended while scanning use of next.

It took some time to get to the bottom of this. The problem is that a fragile frame *must* end at the start of a new line! I am an indentation-freak ... I indent LaTeX files even when Emacs doesn't. So I ended up with the ``end{frame}`` indented by a couple of spaces. That's what choked LaTeX. So the above example works when changed as follows:

::

     begin{frame}[fragile]
       frametitle{Euclid says ``hello''}
       begin{verbatim}
   blah...
   and blah...
   end{verbatim}
   end{frame}

Posting this here for the record, with the hope that it will show up in the search results when some other poor sod is bugged by the same problem!
