show databases;
use e_commerce;
desc User;
select * from User;
select user_id, first_name, last_name, email  from User where user_id = 7  ;
select user_id, first_name, last_name, email  from User where last_name = 'Gupta'  ;
select user_id, first_name, last_name, email ,  date_of_birth  from User where  date_of_birth > '2000-12-31' order by  date_of_birth desc ;

select user_id, first_name, last_name, email,  date_of_birth, disabled 
 from User 
 where  date_of_birth < '2000-12-31' and disabled = 1 
 order by  date_of_birth  ;
 show tables;
 select * from product;
 
 show databases;
 use e_commerce;
 show tables;
 select * from product;
 select * from category;
 select cgs.category_name , sum(prd.price)
 from category as cgs 
 inner join product as prd
 group by cgs.category_name  ;
 
 
 

 
 
 
 
 
 