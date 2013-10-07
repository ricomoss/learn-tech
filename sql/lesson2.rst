==========================
Learn SQL: Lesson 2
==========================

More Syntax
==================================

1. Ordering
    The results of a query are generally returned in order of the table's primary key ascending.  Often you will
    want to customize the order the data is returned.::

        SELECT * FROM leads_lead ORDER BY created_at;
    
        Force data to be ordered descending:
        SELECT * FROM leads_lead ORDER BY created_at DESC;
        
        Order by data in an hstore field:
        SELECT * FROM leads_lead ORDER BY data->'last_name';

    .. note::
        The default "ORDER BY" results come in ascending.


2. Limiting
    It is often useful to limit the number of results to make the results more readable.::
    
        SELECT * FROM leads_lead ORDER BY data->'last_name' LIMIT 10;
        
        SELECT * FROM leads_lead ORDER BY data->'last_name' DESC LIMIT 10;
    

3. Searching By Similiarities
    Often you will be searching for data with string values similar to a specific value.  Say, a city name
    with or without capitalization.::
    
        SELECT * FROM leads_lead WHERE lower(data->'city') LIKE 'portland';
        
        Use wildcards to search for strings when you know a portion of what you are looking for:
        SELECT * FROM leads_lead WHERE lower(data->'city') LIKE '%portland%';
        

4. Putting It All Together
    There is an order to the way queries are constructed.  When putting multiple commands together
    you should ensure you are using the correct construction or you will get a syntax error.::
    
        SELECT <field1>, <field2> FROM <table>
        [WHERE] <logical clause> [AND] <logical clause>
        [ORDER BY] <ordering parameter> [DESC]
        [LIMIT] <number of results>;

    Let's do some searches using "WHERE", "ORDER BY", "LIMIT", "DESC" and "LIKE".::
    
        SELECT * FROM leads_lead
        WHERE testing = False;
        
        SELECT * FROM leads_lead
        WHERE testing = False
        ORDER BY created_at;
        
        SELECT * FROM leads_lead
        WHERE testing = False
        ORDER BY created_at DESC;
        
        SELECT * FROM leads_lead
        WHERE testing = False
        ORDER BY created_at DESC
        LIMIT 5;
        
        SELECT * FROM leads_lead
        WHERE testing = False
            AND lower(data->'city') LIKE '%portland%'
        ORDER BY created_at DESC
        LIMIT 5;

    .. note::
        As the queries get longer it's conventional to break them up with newlines for readability.

