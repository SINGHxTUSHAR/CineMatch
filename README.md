[![GitHub license](https://img.shields.io/github/license/SINGHxTUSHAR/CineMatch.svg)](https://github.com/SINGHxTUSHAR/CineMatch/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/SINGHxTUSHAR/CineMatch.svg)](https://GitHub.com/SINGHxTUSHAR/CineMatch/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/SINGHxTUSHAR/CineMatch.svg)](https://GitHub.com/SINGHxTUSHAR/CineMatch/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/SINGHxTUSHAR/CineMatch.svg)](https://GitHub.com/SINGHxTUSHAR/CineMatch/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)


[![GitHub watchers](https://img.shields.io/github/watchers/SINGHxTUSHAR/CineMatch.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/SINGHxTUSHAR/CineMatch/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/SINGHxTUSHAR/CineMatch.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/SINGHxTUSHAR/CineMatch/network/)
[![GitHub stars](https://img.shields.io/github/stars/SINGHxTUSHAR/CineMatch.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/SINGHxTUSHAR/CineMatch/stargazers/)

[![Open in Visual Studio Code](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://open.vscode.dev/SINGHxTUSHAR/CineMatch)

# CineMatch 🎥:
![img_1](https://github.com/SINGHxTUSHAR/CineMatch/assets/113624520/40d66ecc-1189-4d14-b767-aa6ae37f2a32)

Imagine a system that suggests movies you'd love, like magic. This movie recommendation system uses a combination of clever math and language understanding. First,
it gathers details about movies, like descriptions, genres, and ratings. Then, it employs Natural Language Processing (NLP) techniques to clean up the descriptions,
focusing on the important words that truly describe the movie's content. NLP also helps the system understand synonyms and different ways of expressing the same idea.

Next, the system gets to know you. It might ask for your movie ratings or preferences for genres or actors.
This information is also converted into a special code, much like the movie descriptions. Here's where the magic happens – a mathematical concept called cosine similarity helps
the system compare your code with the movie codes. The closer the match, the more similar the movie's content is to your taste. Finally, the system recommends movies with the closest matches,
ensuring you have a fantastic cinematic experience tailored just for you.

## Work-Flow ⚔️:

#### `Data Preparation:`

* Movie Data Collection:  The system gathers information about movies, including titles, descriptions, cast, crew, genres, and ratings.

* NLP Preprocessing: NLP techniques come into play here. Text descriptions might undergo cleaning, stemming (reducing words to their root form), and removing stop words (common words like "the" or "a").

* Vectorization:  Each movie is converted into a mathematical vector using techniques like TF-IDF (Term Frequency-Inverse Document Frequency). This vector represents the movie's content based on the importance of each word in the description.

#### `Cosine Similarity for Recommendation:`

* User Interaction:  The user might provide ratings for movies they've seen or express preferences for genres or actors. This user data is also converted into a vector.

* Similarity Calculation:  Cosine similarity is applied between the user's vector and the movie vectors. This calculates how similar each movie's content is to the user's preferences.

* Recommendation Generation:  Movies with the highest cosine similarity scores are considered the most similar to the user's taste and are recommended.

Overall, this system leverages cosine similarity to find movies with content most relevant to a user's preferences, informed by the power of NLP to analyze movie descriptions and user input.


## Requirements💻 :

Ensure you have the following dependencies installed:

- Python (version 3.12.x)
- IDE: VS-CODE or collab
- Virtual-environment
- Other dependencies (refer to the requirement.txt)

You can install the required Python packages using:

```bash
pip install -r requirements.txt
```

## Setup 💿:

- Clone the repository:
```bash
git clone https://github.com/SINGHxTUSHAR/CineMatch.git
cd CineMatch
```
- Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```
- Activate the virtual environment:
  - On Windows:
   ```bash
   venv\Scripts\activate
   ```
  - On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```


## Contributing 📌:
If you'd like to contribute to this project, please follow the standard GitHub fork and pull request process. Contributions, issues, and feature requests are welcome!

## Suggestion 🚀: 
If you have any suggestions for me related to this project, feel free to contact me at tusharsinghrawat.delhi@gmail.com or <a href="https://www.linkedin.com/in/singhxtushar/">LinkedIn</a>.

## License 📝:
This project is licensed under the <a href="https://github.com/SINGHxTUSHAR/CineMatch/blob/main/LICENSE">MIT License</a> - see the LICENSE file for details.
