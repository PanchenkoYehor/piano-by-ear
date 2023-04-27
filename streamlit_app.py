import utils
import index
import streamlit as st
import streamlit.components.v1 as components
from frontend import component_zero
from datetime import datetime

if 'counter' not in st.session_state:
    st.session_state.counter = 0


def test():
    utils.generate_midi_by_notes(['C4', 'D4', 'E4'], [2, 2, 2], 'sample.mid')
    utils.midi_to_wav('sample.mid', 'asmple.wav')


def run_component(props):
    value = component_zero(key='zero', **props)
    return value


def handle_event(value):
    st.header('Streamlit')
    st.write('Received from component: ', value)


if __name__ == "__main__":
    range_begin, range_end = st.select_slider(
        'Melody range',
        options=utils.piano_notes,
        value=(utils.piano_notes[0], utils.piano_notes[-1]))
    # st.write(f'Desired range is {range_begin}-{range_end}')

    only_white_keys = st.checkbox('only white keys')

    if st.button('Generate next melody'):
        utils.wav_out = utils.generate_melody(range_begin, range_end, only_white_keys)
        st.audio(utils.wav_out, format="audio/wav")
    else:
        st.audio(utils.wav_out, format="audio/wav")

    if st.button('Show ground melody'):
        st.write(f'here is ground melody: {utils.melody_notes}')

    # components.html(index.html_front, height=400, width=800)
    st.session_state.counter = st.session_state.counter + 1
    props = {
        'initial_state': {'message': ''},
        'counter': st.session_state.counter,
        'datetime': str(datetime.now().strftime("%H:%M:%S, %d %b %Y"))
    }

    handle_event(run_component(props))
