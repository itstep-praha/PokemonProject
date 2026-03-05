-- select [názvy sloupců (* = všechny sloupce)] from nazev_tabulky

select * from pokemon_pokemon
order by name

select image, name from pokemon_pokemon
limit 5

select * from pokemon_pokemon
where number > 100 and number < 106

select * from pokemon_pokemon
where create_dt > '2026-03-04 13:03'

SELECT * FROM pokemon_pokemon
ORDER BY create_dt desc
LIMIT 100

select number, name, length(name) from pokemon_pokemon
limit 1000

select min(number), max(number) from pokemon_pokemon

select min(number), max(number) from pokemon_pokemon
where create_dt < '2026-03-04 13:03'

select sum(number), count(1) from pokemon_pokemon
where create_dt < '2026-03-04 13:03'

select avg(number) from pokemon_pokemon
where create_dt < '2026-03-04 13:03'

select
	sum(length(name)),
	avg(length(name)),
	min(length(name)),
	max(length(name))
from pokemon_pokemon

select SUBSTR(name, 1, 1), count(1), max(number) from pokemon_pokemon
group by SUBSTR(name, 1, 1)
