INSERT INTO public.katalog(
	name, parent_id)
	VALUES 
    ('movie_reviews', 0),
    ('music_tops',0),
    ('games_soundtracks',0),
    ('80s',1),
    ('90s',1),
    ('00s',1),
    ('10s',1),
    ('Billboard_Hot_100',2),
    ('Rolling_stones',2),
    ('Forza_horizon',3)
    ;
INSERT INTO documents(
    name, format, size, hash, parent_katalog_id
    )
    VALUES 
    ('Blade_Runner', 'txt', 676688, '59147331',4),
    ('Raiders_of_the_Lost_Ark', 'txt', 878714, '14396977',4),
    ('Scarface', 'txt', 880529, '90129101',4),
    ('The_Shawshank_Redemption', 'txt', 608850, '2042647',5),
    ('Schindlers_List ', 'txt', 640493, '54973792',5),
    ('Toy_Story', 'txt', 680998, '57602299',5),
    ('Inglourious_Basterds', 'txt', 518581, '15200368',6),
    ('No_Country_for_Old_Men', 'txt', 864529, '7147076',6),
    ('Once_Upon_a_Time_in_Hollywood', 'txt', 995981, '48987209',7),
    ('Billboard_Hot_100_WEEK_OF_JUNE_1, 2024', 'txt', 79221, '67759989',8),
    ('The_500_Greatest_Songs_of_All_Time', 'txt', 849543, '95051009',9),
    ('Arctic_Monkeys_R_U_Mine', 'mp4', 905174, '8706123',10),
    ('The_Black_Keys_Lonely_Boy', 'mp4', 539329, '13692888',10)
    ;
