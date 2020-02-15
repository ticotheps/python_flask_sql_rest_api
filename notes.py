"""
(1) What is `Flask`?
    - Python web framework (i.e. - Djanjo)
    
(2) `Flask` vs `Django`
    - Django
        - High-level framework.
        - Very "opinionated".        
        - Comes ready to "plug-n-play" right "out-of-the-box".
        - Contains pre-determined ways of accomplishing most tasks.
    - Flask
        - Low-level framework.
        - Allows more freedom and customization with development.
            - Similar in many ways to Node.js.

(3) What is `SQLAlchemy`?
    - An ORM (Object Relational Mapper)
        - Used with Flask to manipulate the SQL database.
        - Doesn't require raw SQL queries to manipulate the database (i.e. - 
        Sequelize, Mongoose, built-in ORM included with Django).
        - Much like just another abstraction layer between server and 
        database.
    
(4) What is `Marshmallow`?
    - An ORM (Object Relational Mapper) & An ODM (Object Document Mapper)
        - Serializes and De-serializes Data.

(5) What is `serialization` and `deserialization`?
    - Serialization
        - In the context of data storage, this is the process of translating data
        structures or object state into formats that can be stored or transmitted
        and reconstructed later.
    - Deserialization
        - The reconstructing of stored data into a human-readable format. 
            - i.e. - "pickling"
                - The Python Pickle Module
                    - An object-oriented way to store Python objects directly in
                    a special storage format.
                    - Stores and reproduces Python lists and dictionaries very
                    easily.
                    - "Pickles" can only store an attribute's values.
                    - "Pickles" CANNOT store file handles or connection sockets.
"""