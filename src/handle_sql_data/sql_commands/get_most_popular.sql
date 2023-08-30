SELECT term, artist_name, MAX(popularity)
FROM top_artist_popularities
GROUP BY term;
