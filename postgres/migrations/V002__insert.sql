INSERT INTO public.katalog(
	name, parent_id)
	VALUES 
    ('movie reviews', 0),
    ('music tops',0),
    ('games soundtracks',0),
    ('80s',1),
    ('90s',1),
    ('00s',1),
    ('10s',1),
    ('Billboard Hot 100',2),
    ('Rolling stones',2),
    ('Forza horizon',3)
    ;
INSERT INTO documents(
    name, format, size, hash, parent_katalog_id
    )
    VALUES 
    ('Blade Runner', 'txt', 676688, '59147331',4),
    ('Raiders of the Lost Ark', 'txt', 878714, '14396977',4),
    ('Scarface', 'txt', 880529, '90129101',4),
    ('The Shawshank Redemption', 'txt', 608850, '2042647',5),
    ('Schindlers List ', 'txt', 640493, '54973792',5),
    ('Toy Story', 'txt', 680998, '57602299',5),
    ('Inglourious Basterds', 'txt', 518581, '15200368',6),
    ('No Country for Old Men', 'txt', 864529, '7147076',6),
    ('Once Upon a Time... in Hollywood', 'txt', 995981, '48987209',7),
    ('Billboard Hot 100 WEEK OF JUNE 1, 2024', 'txt', 79221, '67759989',8),
    ('The 500 Greatest Songs of All Time', 'txt', 849543, '95051009',9),
    ('Arctic Monkeys - R U Mine?', 'mp4', 905174, '8706123',10),
    ('The Black Keys - Lonely Boy', 'mp4', 539329, '13692888',10)
    ;
