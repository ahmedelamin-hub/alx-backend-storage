-- 3-glam_rock.sql
-- This script lists all bands with Glam rock as their main style
-- The results are ordered by their longevity (in years until 2022)

SELECT 
    band_name,
    IFNULL(
        CASE 
            WHEN split IS NULL THEN 2022 - formed
            ELSE split - formed
        END, 0) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
