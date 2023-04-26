import utils
import index
import streamlit as st
import streamlit.components.v1 as components


def test():
    utils.generate_midi_by_notes(['C4', 'D4', 'E4'], [2, 2, 2], 'sample.mid')
    utils.midi_to_wav('sample.mid', 'asmple.wav')


def local_css(file_name):
    with open(file_name) as f:
        # print(f.read())
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


if __name__ == "__main__":
    # local_css("style.css")
    # st.markdown(f'<link rel="stylesheet" href="style.css">', unsafe_allow_html=True)
    # remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

    data = "melody_roland.wav"
    st.audio(data, format="audio/wav")
    only_white_keys = st.checkbox('only white keys')

    components.html(index.html_front, height=600)