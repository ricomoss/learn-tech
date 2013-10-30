==========================
Learn SQL: Lesson 3
==========================

Even More Syntax
==================================
Up to this point we have learned how to inspect the database schema so we can make desicions about the relationships
of data.  We've also covered how to query data from a table and limit, order and filter the results.  Relational
databases are powerful because of their way to manage relationships!  Queries to a single table, however useful,
are only a small portion of the power.  We want to query from multiple tables across multiple relationships.


1. Joining Tables
    When two tables are joined in a query we are observing results of relationships.  The joining occurs
    at the same point in the SQL syntax as when you define the table.  You can think of the joining of two
    or more tables as a creation of a temporary "table".::

        SELECT * FROM <table>;
    
        When joining two tables:
        SELECT * FROM <table1> JOIN <table2> ON <foreign key1> = <foreign key2>;
   
    We know from the *leads_lead* schema inspection (*\d leads_lead*) that it has a foreign key to the
    *contracts_offer* table through the field *offer_id*.  We can use this foreign key to join the two
    tables together.::
   
        SELECT * FROM leads_lead JOIN contracts_offer ON offer_id = id;
        
    This is ambiguous!  There exists an "*id*" field in both of these tables.  How can we specify which
    "*id*" we are talking about?  We'll use *aliases*.::
    
        SELECT * FROM leads_lead l JOIN contracts_offer o ON l.offer_id = o.id;
        
    .. note::
        You can use the entire table name rather than aliasing them, but that is a lot of typing.
        
        
2. Using Aliases Effectively
    The output of a '\*' query often gives too much information.  Usually you'll be interested in just a few
    fields from each table.  You can use the aliases to get those fields easily.::
    
        SELECT l.id, l.sold_at, o.id, o.contract_id, o.product_id, o.status
        FROM leads_lead l
          JOIN contracts_offer o ON l.offer_id = o.id
        WHERE l.testing = False
        LIMIT 5;
 
    The output here has two different '*id*' fields.  This is not ambiguous to the database as we used
    aliases to distinguish them in the query.  They are still ambigous to the person reading the results!
    We can alias the results too.::
    
        SELECT l.id AS lead_id, l.sold_at, o.id AS offer_id, o.contract_id, o.product_id, o.status AS offer_status
        FROM leads_lead l
          JOIN contracts_offer o ON l.offer_id = o.id
        WHERE l.testing = False
        LIMIT 5;
    
        
3. Chain the Joins
    You can keep joining as far down the relationship chain as you want.::
    
        SELECT l.id AS lead_id, l.sold_at, o.id AS offer_id, o.contract_id,
               o.status AS offer_status, p.id AS product_id, p.campus_id,
               p.name AS product_name
        FROM leads_lead l
          JOIN contracts_offer o ON l.offer_id = o.id
          JOIN products_product p ON o.product_id = p.id
        WHERE l.testing = False
          AND (o.status = 'active' OR o.status = 'paused')
          AND p.vertical = 'education'
        LIMIT 5;
    
4. Filtering with Lists
    It is quite cumbersome to filter against the same field with multiple possible values.  Instead we can use
    the *IN*.::
        
        SELECT l.id AS lead_id, l.sold_at, o.id AS offer_id, o.contract_id,
               o.status AS offer_status, p.id AS product_id, p.campus_id,
               p.name AS product_name
        FROM leads_lead l
          JOIN contracts_offer o ON l.offer_id = o.id
          JOIN products_product p ON o.product_id = p.id
        WHERE l.testing = False
          AND o.status IN ('active', 'paused')
          AND p.vertical = 'education'
        LIMIT 5;
        
    This can be very helpful for searching the *hstore* fields.::
    
        SELECT l.id AS lead_id, l.sold_at, o.id AS offer_id, o.contract_id,
               o.status AS offer_status, p.id AS product_id, p.campus_id,
               p.name AS product_name, l.data->'city' AS lead_city,
               l.data->'state' AS lead_state
        FROM leads_lead l
          JOIN contracts_offer o ON l.offer_id = o.id
          JOIN products_product p ON o.product_id = p.id
        WHERE l.testing = False
          AND o.status IN ('active', 'paused')
          AND p.vertical = 'education'
          AND lower(l.data->'city') SIMILAR TO '%portland%'
        LIMIT 5;
    
Homework...oh, no!

For the next lesson you'll need to demostrate how to get the following queries:

-  What are the 10 most recent buyer contracts ordered by RPL (most to least)?
-  How many buyer contracts have RPL less than $30 and are in a group?
-  For the 10 most recent leads, what were the offers, contracts, products and ads associated with them?
-  What are the different types of deliveries in Proton?
-  What were the reasons for the last 5 failed deliveries?
