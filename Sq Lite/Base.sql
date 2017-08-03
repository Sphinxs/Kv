
-- Base De Dados

create table if not exists Dice (
    id Integer Primary Key Autoincrement Not Null,
    name Text Not Null,
    age Integer Default 1,
    cpf Int Unique
);

alter table Dice rename to Data;


insert into Data ( name, age, cpf ) values ( 'Yoda', 111, 1111 );

insert into Data ( name, age, cpf ) values ( 'Darth', 222, 2222 );

insert into Data ( name, age, cpf ) values ( 'Leia', 333, 3333 );


-- select Data.name, Data.cpf from Data;

-- select Data.name from Data where id = 1;

-- select * from Data order by age desc;

-- select * from Data limit 2;

-- select Data.name from Data order by name asc limit 2;

select * from Data;


alter table Data add column nick Text;

update Data set name = 'Chew' where Data.cpf is 1111 limit 1;

delete from Data where id is 1;


drop table Data;
