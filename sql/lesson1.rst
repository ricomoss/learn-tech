==========================
Learn SQL: Lesson 1
==========================

Motivation
==================================

Databases are an integral part of business needs.  If a company stores data they use a database - they are used
everywhere.  The more you understand how databases work and how to access and use them the more powerful your
professional skills will be.

There are several aspects to the fundamental use of a database.  Some people use them for building reports.
Others use them for mass data storage.  Databases can be used to simplify complex relationships.
No matter how you want to use a database the way you add, modify or view the data all comes down to
a simple syntax: SQL.

.. note::
    These lessons will focus on SQL databases.  There are NoSQL databases that are available, however.
    
    
What is SQL?
==================================

The acronym SQL (Structured Query Language) is a generic term for a syntax used to query a database.  If you
want information to go into or come out of a database you must "query" for it.  There are several databases
that use SQL for their query language (i.e. PostgreSQL, MySQL, Oracle, etc).  We will be using a PostgreSQL
database, but the SQL syntax discussed here can be used almost universally throughout all these databases.

Database
==================================

A database is a collection of tables containing structured information.  Tables contain fields which
represent specific information to build relationships.  Below is an example heirarchy for the database
we will be using for examples::

    (database)
    - proton:
        (table)
        - leads_lead:
            (fields)
            - id (INTEGER) (PRIMARY KEY)
            - created_at (DATETIME)
            - update_at (DATETIME)
            - offer_id (INTEGER) (FOREIGN KEY)
            - data (HSTORE)
            - info_id (INTEGER) (FOREIGN KEY)
            - response (CHAR 255)
            - payout (NUMERIC(20, 2))
            - sold_at (DATETIME)
            - testing (BOOLEAN)
            - external_uid (CHARACTER 255)
            - mfbsid (CHARACTER 12)
            - ad_id (INTEGER) (FOREIGN KEY)
            - ip (INET)
            - capture_url (CHAR 200)
            - margin (NUMERIC(20, 2))

.. note::
    We will not be discussing how to create databases, tables or fields (or how to modify them).

Nomenclature
==================================

All table names and fields should always be named in such a way as to make it completely obvious by reading it 
what it means.  If you are going to store information about hotdogs in a table the table should be named "hotdogs".
It is generally frowned upon to use capitilization when creating names in databases (database name, 
table name, field name, etc).

It is common to use "_" (underscore) to create application disctinction among tables.

For example, in Proton there are several applications all working together to form the Proton project.  These
applications include Leads, Relationships, Contracts, Analytics, etc.  So, in order to maintain the database
in a clear and understandable fashion the tables dealing with all the information from the Leads app will begin
with "leads\_".

You may have noticed the table above was named "leads_lead".  That simply means it's the lead table within the
Leads application.  If you are searching for buyer contracts you would search "contracts_buyercontract".

Schema
==================================

The overall organization of the data within the database is called the Schema.  It is important to understand
the database schema if you want to be able to effectively search for data within the database.  This is often
the most difficult part of using a database.  The commands to get the information never changes between
databases - it's the schema that changes.

At one company the user information might be in a table called "registered_users".  This table might include
only name, username, email and password (all password information is always encrypted).

At a second company the user information might be in a table called "users".  This table might include first name, 
last name, email, address, phone, password and birth date.

What information is available in which tables depends on the Schema.  The Schema is designed by the engineers 
who created and designed the application that uses it.

1. Transversing the Schema
    PostgreSQL has several ways to help you transverse the Schema to help you understand (by visual inspection) 
    where the data might be held.  It's always best to reference a Schema visual aid (they are usually available
    from a tech department).  In the event that you are unable to get such a reference you can use the following
    commands to help understand the structure of the schema.::

        List all the tables:
        proton=# \d
    
        Describe a table in more details:
        proton=# \d <table name>
        
    .. note::
        You'll notice other information here but it's beyond the scope of these lessons.
        Focus on "Name", which represents the table name.
            
    .. note::
        This will provide details for every field in the table, including information 
        about foreign keys.  Again, some of the information provided by this command is
        beyond the scope of these lessons.

    .. note::
        The commands listed above are proprietary to the PostgreSQL database.  For instance, in MySQL
        these commands would be "SHOW TABLES" and "DESCRIBE <table name>", respectively.  These commands
        are not SQL commands - they are database specific commands.
        

2. Understanding the Schema
    Let's look at the output of the \\d <table name> above using the leads_lead table.::
    
        proton=# \d leads_lead
        
    The schema for the leads_lead table includes many foreign keys. Foreign keys are a way
    for a database to connect relationships across many tables.  You will notice there is a
    foriegn key to the contracts_offer table through the offer_id field in the leads_lead table.
    
    This simply means that you can look at the leads_lead table and see an offer_id of XYZ and know that it
    corresponds to the "(id)" field of the contracts_offer table.  This tells you the relationship
    between leads_lead and contracts_offer.
    
    .. note::
        You'll notice contraints, btree, etc.  These are outside the scope of these lessons.
        
Querying the Database
==================================

Finally we have enough information to query the database.  The primary functionality we will be using is
the "SELECT" statement.  This will allow us to read from the database and organize the output for
easy viewing, reporting and interpretation.

Let's start with the leads_lead table.  We'll select all fields from the leads_lead table for a 
specific lead.::

    proton=# SELECT * FROM leads_lead WHERE id = 115;
    

Let's search for all leads from Avenel.::

    proton=# SELECT * FROM leads_lead WHERE data->'city' = 'Avenel';
    
We'll continue with more querying in lesson2.
