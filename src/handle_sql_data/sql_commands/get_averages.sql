SELECT term, AVG(popularity)
FROM top_artist_popularities
GROUP BY term;
