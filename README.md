**DESCRIPTION:**

This program will make an API request to a Spotify App (that the user must currently generate) to obtain the user's top artists and their popularities over three distinct time ranges.

The program will file this information into a relational database.

The program will then prompt the user to input requested time ranges 's, m or l' for short, medium or long.

The program will then produce a graph containing the artist's names and their popularities for the requested time ranges, to tell the user whether or not they have become more niche in their music taste.


NOTE: If the database already exists, i.e., the program has been run before, then the user will be prompted as to whether they would like to use the local database or update it using the API.

Example outputs are included in the example_graphs folder.




**INTRUCTIONS:**

1) Make a Spotify App using your own spotify account to get a Client ID and Client Secret.

2) Replace 'string' in the corresponding entries in the example.env in a new .env file with the obtained Client ID and Client Secret.
  
3) Run main.py




**UPCOMING CHANGES:**

(1) Unit tests.

(2) New authorisation flow so user does not need to make Spotify App.

(3) Django interface.




**EXAMPLE IMAGE:**
![ExampleAllTerms](https://github.com/jngoodman/SpotifyNiche/assets/140734696/ecc3a0a4-74eb-4602-a5b0-7fad9b8d6afd)
