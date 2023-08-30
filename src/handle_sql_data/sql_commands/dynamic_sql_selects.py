extraction_intro = "SELECT * FROM top_artist_popularities WHERE"

extraction_keys = {
        'short_term': "term IS 'short_term'",
        'medium_term': "term IS 'medium_term'",
        'long_term': "term IS 'long_term'"
    }

extraction_outro = "ORDER BY popularity;"
