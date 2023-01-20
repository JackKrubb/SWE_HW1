Software Engineering HW1 

Testing using Postman 

Checklist:
1. Vending Machine (vending_location)
    - User can CREATE/ADD new vending machines specifying vending machine location 
        - 127.0.0.1:5000/vending/create-vending
        - POST method
        - Key: vending_location value: "location name"
    - User can READ/RETRIEVE specific vending machine as well as all vending machines
        - 127.0.0.1:5000/vending/single/<id> OR 127.0.0.1:5000/vending
        - GET method
    - User can UPDATE/EDIT vending machine location
        - 127.0.0.1:5000/vending/edit-vending/<id>
        - POST method
        - Key: vending_location value: "new location name"
    - User can DELETE vending machines
        - 127.0.0.1:5000/vending/delete-vending/<id>

2. Products (product_name, product_price)
    - User can CREATE/ADD new products specifying product name and price
        - 127.0.0.1:5000/product/add-product
        - POST method
        - Key: product_name value: "name" Eg. Potato Chips
        - Key: product_price value: <float num> Eg. 15.53
    - User can READ/RETREIVE specific product or all products ordered by its prices
        - 127.0.0.1:5000/product/single/<id> OR 127.0.0.1:5000/product
        - GET method
    - User can UPDATE/EDIT product's name and price
        - 127.0.0.1:5000/product/edit-product/<id>
        - POST method
        - Key: product_name value: "name" Eg. Potato Chips
        - Key: product_price value: <float num> Eg. 15.53
    - User can DELETE product
        - 127.0.0.1:5000/product/delete-product/<id>

3. Stocking (vending_id, product_id, product_amount)
    - User can CREATE/ADD new stocks for specific vending machine and product and product amount
        *If stocking already existed, the product amount will add up cumulatively 
        - 127.0.0.1:5000/stock/add-stock
        - POST method
        - Key: vending_id value: <int>
        - Key: product_id value: <int>
        - Key: product_amount value: <int>
    - User can READ/RETRIEVE all stocks from all vending machine
        - 127.0.0.1:5000/stock
    - User can READ/RETRIEVE all stocks from one specific vending machine
        - 127.0.0.1:5000/stock/single-stock
        - GET method
        - Key: vending_id value: <int>
        - Key: product_id value: <int>
    - User can READ/RETRIEVE one stock from one specific vending machine
        - 127.0.0.1:5000/stock/single-vend
        - GET method
        - Key: vending_id value: <int>
    - User can UPDATE/EDIT stock amount
        - 127.0.0.1:5000/stock/edit-stock
        - POST method
        - Key: vending_id value: <int>
        - Key: product_amount value: <int>
    - User can DELETE specific stocking
        - 127.0.0.1:5000/stock/delete-stock
        - Key: stocking_id value: <int>

HOW TO RUN:
1. Run `swe_vending.sql` script to create a database locally
2. Run app.py by typing `python3 app.py`