-- 2-fans.sql
-- This script ranks country origins of bands by the number of fans
-- The results are ordered by the number of (non-unique) fans in descending order

SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
