select p.number, p.name, u.username from pokemon_pokemon as p
inner join auth_user as u on u.id = p.user_id
where p.number in (1, 2)


select c.text, c.create_dt, p.number, p.name, cu.username, pu.username from pokemon_comment as c
inner join pokemon_pokemon as p on p.number = c.pokemon_id
inner join auth_user as cu on cu.id = c.user_id -- comment user
inner join auth_user as pu on pu.id = p.user_id -- pokemon user
limit 100


select * from my_table as t
left join pokemon_pokemon as p on p.number = t.pokemon_id


select * from pokemon_pokemon as p
left join my_table as t on p.number = t.pokemon_id
where t.id is null

select "a"

