Basic Website for my little brother to keep his music on.


Uses Flask to keep track of the music files
To use download the folder cd to the location, probably make a virutal enviroment if you want
usually:
	python -m venv env
	.\env\Scripts\activate

Then intall the requiments
	pip install -r requirements.txt

Run test server with:
	python app.py




Make a folder for each person you want to have music for in /static/music
then place the mp3 files there.

Program will automatiicaly detect each folder and make a list of all of them using their names as the artist name, then will make a site for each of those artist and list out each song in the folder, again auto detecting them.

I included some of my music to show how it works