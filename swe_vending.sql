DROP SCHEMA IF EXISTS swe_vending;
CREATE SCHEMA swe_vending;
USE swe_vending;


DROP TABLE IF EXISTS product;
create table product
(
	product_id int auto_increment NOT NULL,
    product_name varchar(100),
    product_price float,
    primary key (product_id),
    constraint u_product
		unique (product_id)	
);

DROP TABLE IF EXISTS vending_machine;
create table vending_machine
(
	vending_id int auto_increment NOT NULL,
    vending_location varchar(100),
    primary key (vending_id),
    constraint u_vending
		unique (vending_id)	
);

DROP TABLE IF EXISTS stocking;
create table stocking
(
	stocking_id int auto_increment NOT NULL,
    vending_id int NOT NULL,
    product_id int NOT NULL,
    product_amount int,
    primary key (stocking_id),
    constraint u_stocking
		unique (stocking_id),
	constraint fk_vending
		foreign key(vending_id)
        references vending_machine(vending_id),
	constraint fk_product
		foreign key(product_id)
        references product(product_id)
);