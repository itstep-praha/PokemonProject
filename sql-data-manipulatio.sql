-- insert - vkládá nové řádky
-- update - upravuje hodnoty u existujících záznamů
-- delete - maže záznamy


--insert into pokemon_pokemon (
--number, image, name, slug, create_dt, user_id
--) values (
--1001, '', 'Firesaur', 'firesaur', DATE('now'), 1
--)

select * from pokemon_pokemon where number > 151
select * from pokemon_pokemon where number = 1001

update pokemon_pokemon set name='FireDrake', slug='firedrake'
where number = 1001

-- !!! pozor vždy dělat update s podmínkou where, jinak se to udělá pro všechny řádky
-- update pokemon_pokemon set image=''

select * from pokemon_pokemon
where slug like 'test%'

delete from pokemon_pokemon
where slug like 'test%' -- slug začíná na test...
--where number in (1000, 9999)
