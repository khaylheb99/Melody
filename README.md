# Melody AI

Melody AI is a Python-based tool that generates genre-specific melodies using the `music21` library. It supports genres like Afrobeat, Fuji, and Jazz, and creates MIDI files that can be played back or further processed.

## Features

- Melody generation based on predefined musical patterns and scales
- Support for multiple genres: Afrobeat, Fuji, Jazz
- Rhythmic variations using syncopation
- Basic percussion (kick and snare simulation)
- Outputs MIDI files
- Streamlit-compatible for web deployment

## Installation

1. Clone the repository:

```bash
git clone https://github.com/khaylheb99/Melody.git
cd Melody
```
2. Install required packages:

```bash

pip install -r requirements.txt
```

## Usage

```python

from melody_generator import generate_melody

# Generate a 30-second Fuji-style melody
generate_melody(genre="Fuji", duration_sec=30, output_file="fuji.mid")
```

In Streamlit
If you have a Streamlit app (app.py), run:

```bash

streamlit run app.py
```

## Genres Supported
Afrobeat: C Minor scale, 120 BPM

Fuji: F Mixolydian scale, 140 BPM

Jazz: G Major scale, 100 BPM

## Project Structure
```bash

Melody/
│
├── app.py                   # Streamlit frontend (optional)
├── melody_generator.py      # Main logic for melody generation
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```
