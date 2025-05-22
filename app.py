import streamlit as st
from music21 import stream, note, scale, tempo
import numpy as np
from tempfile import NamedTemporaryFile
import base64

def generate_melody(genre="Afrobeat", duration_sec=30):
    s = stream.Stream()

    templates = {
        "Afrobeat": {
            "scale": scale.MinorScale('C4'),
            "tempo": 120,
            "pattern": [1,3,5,6,5,3,1,2,3,5]
        },
        "Fuji": {
            "scale": scale.MixolydianScale('F4'),
            "tempo": 140,
            "pattern": [1,2,3,5,3,2,1,5,4,2]
        },
        "Jazz": {
            "scale": scale.MajorScale('G4'),
            "tempo": 100,
            "pattern": [2,3,5,6,9,7,5,3]
        }
    }

    params = templates.get(genre, templates["Afrobeat"])
    s.append(tempo.MetronomeMark(number=params["tempo"]))

    notes = []
    for i in range(int(duration_sec * 2)):
        degree = params["pattern"][i % len(params["pattern"])]
        pitch = params["scale"].pitchFromDegree(degree)
        dur = 0.5 if i % 4 < 2 else 0.25
        notes.append(note.Note(pitch, quarterLength=dur))

    drum_part = stream.Part()
    for i in range(int(duration_sec * 2)):
        if i % 4 == 0:
            drum_part.append(note.Note("C2", quarterLength=0.5))
        elif i % 4 == 2:
            drum_part.append(note.Note("D2", quarterLength=0.5))

    s.append(notes)
    s.append(drum_part)

    with NamedTemporaryFile(delete=False, suffix=".mid") as tmp:
        s.write('midi', fp=tmp.name)
        return tmp.name

st.title("🎵 Genre-Based Melody Generator")
genre = st.selectbox("Choose Genre", ["Afrobeat", "Fuji", "Jazz"])
duration = st.slider("Duration (seconds)", 5, 60, 30)

if st.button("Generate Melody"):
    midi_path = generate_melody(genre, duration)
    with open(midi_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        href = f'<a href="data:audio/midi;base64,{b64}" download="{genre}.mid">🎧 Download {genre} MIDI</a>'
        st.markdown(href, unsafe_allow_html=True)
