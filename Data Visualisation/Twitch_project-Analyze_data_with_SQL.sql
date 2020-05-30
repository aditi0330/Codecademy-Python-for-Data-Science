SELECT *
FROM stream
LIMIT 20;
SELECT *
FROM chat
LIMIT 20;
SELECT DISTINCT game
FROM stream;
SELECT game, COUNT(*)
FROM stream
GROUP BY game
ORDER BY COUNT(*) DESC;
SELECT country, COUNT(*)
FROM stream
WHERE game == 'League of Legends'
GROUP BY country
ORDER BY 2 DESC;
SELECT player, COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 2 DESC;
SELECT game,
 CASE
  WHEN game = 'Dota 2'
      THEN 'MOBA'
  WHEN game = 'League of Legends' 
      THEN 'MOBA'
  WHEN game = 'Heroes of the Storm'
      THEN 'MOBA'
    WHEN game = 'Counter-Strike: Global Offensive'
      THEN 'FPS'
    WHEN game = 'DayZ'
      THEN 'Survival'
    WHEN game = 'ARK: Survival Evolved'
      THEN 'Survival'
  ELSE 'Other'
  END AS 'genre',
  COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 3 DESC;
SELECT time
FROM stream
LIMIT 10;
SELECT time,
   strftime('%S', time)
FROM stream
GROUP BY 1
LIMIT 20;
SELECT strftime('%H', time), COUNT(*)
FROM stream
WHERE country == 'US'
GROUP BY 1;
SELECT *
FROM stream
JOIN chat
  ON stream.device_id = chat.device_id;