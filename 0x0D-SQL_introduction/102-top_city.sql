-- Retrieve the top 3 cities with the highest temperatures during July and August
SELECT `city`, MAX(`value`) AS `max_temp`
FROM `temperatures`
WHERE `month` IN ('July', 'August')
GROUP BY `city`
ORDER BY `max_temp` DESC
LIMIT 3;

