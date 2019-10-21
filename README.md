# Song-Lyrics-search-engine #
## Domain Specific Information Retrieval System ##

* The task is to build a search engine which will cater to the needs of a particular domain.
* The dataset contains musixmatch track id of each song and the corresponding term frequency of each of top 5000 terms that constitute roughly 92% of all lyrics.
* The dataset is already in bag of words model and hence the same preprocessing technique as implemented in the dataset has been used for user queries as well.
* Vector space model using TF-IDF scores as corresponding vector components and ISC similarity measure has been used to rank the songs in order of relevance to the user query.
* Once this is done, the user will give a query as an input.
* Top 10 relevant documents as returned as the output.

## File Structure ##
* -data folder -dataset used to build the model. It contains two files:
  * data folder/music.txt -the dataset of 27143 songs used for training the retrieval system.
  * data folder/words.txt -the track id-song name mappings are stored here.
* -files/document vectors.py- Used for creating and storing document vectors with tf-idf scores.
* -files/isc_calculation.py-Used for query handling, similarity calculation and retrieval.

## Usage ##
* -Download/clone this repository.
* -Change working directory to where the repository is stored.
* -Install dependencies:
* Python(version 3.7)
* Pandas(version 0.24.2)
* CSV(version 0.0.11)
* NumPy(version 1.16.4)
* -Compile and run.

### Link to actual dataset:
http://millionsongdataset.com/musixmatch/

### Github link for normalization algorithm used to create the bag of words:
https://github.com/tbertinmahieux/MSongsDB/blob/master/Tasks_Demos/Lyrics/lyrics_to_bow.py
