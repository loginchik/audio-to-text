# Audiofile to text with Whisper by OpenAI\

Whisper docs: [project homepage on Github](https://github.com/openai/whisper)

Project uses whisper-openai to transcribe audio files. 
Most of the code is just a decoration for model work process. 

Supported audio formats are the same as whisper support at the moment of project creation:
mp3, m4a, webm, mp4, mpga, wav, mpeg. By default, "base" version of whisper model is used. 
Other model can be set while the program runs. Models are saved into auto-created `models` directory.

## How to run 

### Setup

Create and activate virtual environment. More: [python venv docs](https://docs.python.org/3/library/venv.html)

Install the requirements from `requirements.txt` file:

```python
pip install -r requirements.txt 
```

### Run 

Code runs in terminal. Entering point is in `cli.py`. Run the file:

```python
python cli.py
```