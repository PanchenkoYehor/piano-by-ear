import utils
import streamlit as st

def test():
    utils.generate_midi_by_notes(['C4', 'D4', 'E4'], [2, 2, 2], 'sample.mid')
    utils.midi_to_wav('sample.mid', 'asmple.wav')


if __name__ == "__main__":
    data = "melody_roland.wav"
    st.audio(data, format="audio/wav")