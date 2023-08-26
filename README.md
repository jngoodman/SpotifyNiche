**DESCRIPTION:**

This program will either use a local database.db, or request data from Spotify to obtain the user's top artists and their popularities over three distinct time ranges.

The program will prompt the user to input requested time ranges 's, m or l' for short, medium or long. 

The program will then produce a graph containing the artist's names and their popularities for the requested time ranges, to tell the user whether or not they have become more niche in their music taste.

Example outputs are included in the example_graphs folder.




**INTRUCTIONS:**

1) Install Python3 (https://www.python.org/) and Pipenv (https://pipenv.pypa.io/en/latest/) to your computer.

2) Make a Spotify App using your own spotify account to get a Client ID and Client Secret.

3) Replace 'string' in the corresponding entries in the example.env in a new .env file with the obtained Client ID and Client Secret. Ensure REDIRECT_URI in the .env is equal to the REDIRECT.URI in your Spotify App.
  
4) In your command prompt, navigate to the SpotifyNiche folder, and then type 'pipenv shell'.

5) Type 'py main.py'.




**EXAMPLE IMAGE:**
![ExampleAllTerms](https://github.com/jngoodman/SpotifyNiche/assets/140734696/ecc3a0a4-74eb-4602-a5b0-7fad9b8d6afd)




**MAKING A SPOTIFY APP**

To make a Spotify App, navigate to https://developer.spotify.com/dashboard/, sign in, and click 'Create App'.

Once you've made the App, you need to recover the Client ID, Client Secret and Redirect URI. This is since you need to enter these in to their corresponding fields in a file named '.env' (see example.env). 

To find these, click 'Settings' in the top right of your app, and under Basic Information you'll have something similar to the image below. You can find the Client ID, Client Secret and Redirect URIs at the positions marked with red arrows.

NOTE: you will need to enter the Redirect URI yourself first. The program will not run unless the same Redirect URI is in both your .env file and saved in your web-based Spotify App.

![image](https://github.com/jngoodman/SpotifyNiche/assets/140734696/0c9bc23b-0cf9-4661-99c0-9df3990358cd)
