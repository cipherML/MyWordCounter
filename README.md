<p align="center">
  <img src="https://user-images.githubusercontent.com/73163292/97105148-dc546000-16de-11eb-983c-85c144b1715d.png" width="154">
  <h1 align="center">My Word Counter</h1>
  <p align="center">The basic word counter where you can simply pass the text file or type paragraph or list of statement and word counter will read the text and find the total words, dict of words and how many word are repeated. </p>
  <p align="center">
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
    <a href="https://github.com/cipherML?tab=projects">
    	<img src="https://img.shields.io/badge/Author-Mayur%20Pawar-lightgrey" />
    </a>
  </p>
  
 
## Introduction
**What is Word Counter?**

Apart from counting words and characters, this program can help you to improve word choice and will tell you keyword density. To check word count, simply pass your text file or start typing if you want. You'll see the number of characters and words increase or decrease as you type, delete, and edit them. You can also copy and paste text from online.

**Demo**

__Input Text:__

Here, user need to type the text, paragraph, etc.. This feature will also help you to improve your typing skills.
<p align="center">
  <img src="https://user-images.githubusercontent.com/73163292/97105702-f5f7a680-16e2-11eb-8e8f-6f893eb76c4e.png" width="1600">
</p>

__Words Text file:__

Here, user need to pass a text file with words or paragraph.
<p align="center">
  <img src="https://user-images.githubusercontent.com/73163292/97105769-846c2800-16e3-11eb-8bf4-1f3b812081c8.png" width="1600">
</p>

## **Clone**
Run this in your terminal: 

__HTTPS:__
`https://github.com/cipherML/MyWordCounter.git`

__SSH:__
`git@github.com:cipherML/MyWordCounter.git`

__Important:__ 
**Python 3.6 or 3.7** is needed to run the toolbox.
- IDE `Pycharm`

### Features
- Total word count
- Keyword density (number of repeated words)

### Run
__NOTE:__ run following commands in `run.py`

If you want to improve your typing skills with word counting feature

```python
from WordCounter import input_texts_count

if __name__ == '__main__':
    print("<<<<< BASIC WORD COUNTER >>>>> \n")

    # For input texts
    input_texts_count()
```

Or, if you simply want to pass the text file.

```python
from WordCounter import read_text_file, word_count

if __name__ == '__main__':
    print("<<<<< BASIC WORD COUNTER >>>>>")

    # if there is a text file
    file_path = "sampleTEXT.txt"

    # read the text file
    file = read_text_file(path=file_path)
    print("Paragraph: \n", file)
    word_counts = word_count(string=file)
    print("Basic_word_counter: ", word_counts)
```