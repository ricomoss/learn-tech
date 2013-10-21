==========================
Learn SQL: Lesson 4
==========================

And Finally...
==================================
At this point you should have all the tools necessary to query a database to retrieve data.  The last
thing you need to know is how to output all that useful information to a file.  There are several
common file formats used for reading database information.  Which format you use depends on what
you are trying to do.

1. Redirect to File
    Let's look at a straight output of the terminal information.::

        \o <filename>
        SELECT * FROM leads_lead LIMIT 1;
        \q
   
    This would cause the output of the ``SELECT`` statement to be output into ``<filename>``.
    
    .. note::
        The output in the file will look identical to what it would look like in the terminal.

        
2. Output Formatted as CSV
    The results of your query may be nice and readable, but it isn't useful if you want to transfer that
    data to a computer.  It is useful in cases like these to output the results as a CSV file.::
    
        \copy (SELECT * FROM leads_lead LIMIT 1) TO '~/tmp.csv' WITH CSV;
        
    You will notice the information is *not* readable, but can be imported into another database.  This
    case may not seem as useful as the redirect method, but it's actually far more powerful because it's
    in a format that is ready to be transfered to a computer.  If you get a client requesting specific
    information it's preferable to provide them the results as a ``CSV`` file rather than a readable one.
    
3. Don't Be That Person...
    Often developers or other technical people will request a ``CSV`` file for data processing.  This does
    not mean ``.xls`` or any other formatted file.  ``CSV`` is a global standard for the formatting of
    data.  ``CSV`` files can be handled by all programs and code, while ``.xls`` (or other formats) is
    *very* hit or miss.
    
