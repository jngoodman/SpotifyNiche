SELECT term, artist_name, MIN(popularity)
FROM top_artist_popularities
GROUP BY term;
