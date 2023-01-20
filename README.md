Software Engineering HW1 

Checklist:
1. Vending Machine (vending_location)
    - User can CREATE/ADD new vending machines specifying vending machine location 
    - User can READ/RETRIEVE specific vending machine as well as all vending machines
    - User can UPDATE/EDIT vending machine location
    - User can DELETE vending machines

2. Products (product_name, product_price)
    - User can CREATE/ADD new products specifying product name and price
    - User can READ/RETREIVE specific product or all products ordered by its prices
    - User can UPDATE/EDIT product's name and price
    - User can DELETE product

3. Stocking (vending_id, product_id, product_amount)
    - User can CREATE/ADD new stocks for specific vending machine and product and product amount
        *If stocking already existed, the product amount will add up cumulatively 
    - User can READ/RETRIEVE all stocks from all vending machine
    - User can READ/RETRIEVE all stocks from one specific vending machine
    - User can READ/RETRIEVE one stock from one specific vending machine
    - User can UPDATE/EDIT stock amount
    - User can DELETE specific stocking

HOW TO RUN:
1. Run `swe_vending.sql` script to create a database locally
2. Run app.py by typing `python3 app.py`