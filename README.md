**DESCRIPTION:**

This program will either use a local database.db, or request data from Spotify to obtain the user's top artists and their popularities over three distinct time ranges.

The program will prompt the user to input requested time ranges 's, m or l' for short, medium or long. 

The program will then produce a graph containing the artist's names and their popularities for the requested time ranges, to tell the user whether or not they have become more niche in their music taste.

Example outputs are included in the example_graphs folder.




**INTRUCTIONS:**

1) Make a Spotify App using your own spotify account to get a Client ID and Client Secret.

2) Replace 'string' in the corresponding entries in the example.env in a new .env file with the obtained Client ID and Client Secret. Ensure REDIRECT_URI in the .env is equal to the REDIRECT.URI in your Spotify App.
  
3) Run main.py




**EXAMPLE IMAGE:**
![ExampleAllTerms](https://github.com/jngoodman/SpotifyNiche/assets/140734696/ecc3a0a4-74eb-4602-a5b0-7fad9b8d6afd)
