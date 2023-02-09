DROP SCHEMA IF EXISTS swe_vending;
CREATE SCHEMA swe_vending;
USE swe_vending;
create table if not exists product ( product_id int auto_increment NOT NULL, product_name varchar(100), product_price int, primary key (product_id), constraint u_product unique (product_id));
create table if not exists vending_machine (vending_id int auto_increment NOT NULL,vending_location varchar(100),primary key (vending_id),constraint u_vending unique (vending_id));
create table if not exists stocking(stocking_id int auto_increment NOT NULL,vending_id int NOT NULL,product_id int NOT NULL,product_amount int,primary key (stocking_id),constraint u_stocking unique (stocking_id),constraint fk_vending foreign key(vending_id) references vending_machine(vending_id) ON DELETE CASCADE,constraint fk_product foreign key(product_id) references product(product_id) ON DELETE CASCADE);
create table if not exists purchase(purchase_id int auto_increment primary key, time_stamp DATETIME, vending_id int NOT NULL,product_id int NOT NULL,quantity_amount int,stock_state varchar(255), constraint vending_fk foreign key(vending_id) references vending_machine(vending_id) ,constraint product_fk foreign key(product_id) references product(product_id));
