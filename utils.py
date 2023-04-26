# # import streamlit as st
# # import numpy as np
# # import simpleaudio
# # import numpy
# # import random
# # import time
# #
# #
# # def play_note(note, octave=4):
# #     if octave >= 8:
# #         octave = 8
# #     frequency = note[1] * 2 ** (((octave*12)-48) / 12)
# #     fs = 44100  # 44100 samples per second
# #     seconds = 1 # Note duration - integer
# #
# #     # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
# #     t = numpy.linspace(0, seconds, seconds * fs, False)
# #
# #     # Generate a sine wave from the frequency
# #     note = numpy.sin(frequency * t * 2 * numpy.pi)
# #
# #     # Ensure that highest value is in 16-bit range
# #     audio = note * (2**15 - 1) / numpy.max(numpy.abs(note))
# #     # Convert to 16-bit data
# #     audio = audio.astype(numpy.int16)
# #
# #     # Start playback
# #     play_obj = simpleaudio.play_buffer(audio, 1, 2, fs)
# #
# # # Remove this after testing is done
# #
# # # sample_rate = 44100  # 44100 samples per second
# # # seconds = 2  # Note duration of 2 seconds
# # #
# # # frequency_la = 440  # Our played note will be 440 Hz
# # #
# # # # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
# # # t = np.linspace(0, seconds, seconds * sample_rate, False)
# # #
# # # # Generate a 440 Hz sine wave
# # # note_la = np.sin(frequency_la * t * 2 * np.pi)
# # # st.audio(note_la, sample_rate=sample_rate)
# #
# # # Note frequencies
# # notes = {
# #     1: ["A" ,0],
# #     2: ["A#",0],
# #     3: ["B" ,0],
# #     4: ["C" ,0],
# #     5: ["C#",0],
# #     6: ["D" ,0],
# #     7: ["D#",0],
# #     8: ["E" ,0],
# #     9: ["F" ,0],
# #     10:["F#",0],
# #     11:["G" ,0],
# #     12:["G#",0],
# # }
# #
# # # Generate note frequencies
# # for i,note in enumerate(notes.keys()):
# #     notes[note] = round(440 * 2 ** (i / 12), 1)
# #     print(notes[i])
# #
# # play_note(notes[1], octave = 4)
# # time.sleep(1)
#
# # from mingus.midi import fluidsynth
# # from mingus.containers import NoteContainer
# # from mingus.core import notes, chords
#
# # Define the notes and their durations
# # notes = NoteContainer(["C", "D", "E", "F", "G", "A", "B"])
# # durations = [4, 4, 4, 4, 4, 4, 4]
# #
# # # Create a sequence of notes using the defined notes and durations
# # sequence = []
# # for note, duration in zip(notes, durations):
# #     sequence.append((note, duration))
# #
# # # Play the sequence using a synthesizer
# # fluidsynth.init()
# # for note, duration in sequence:
# #     fluidsynth.play_Note(note, duration * 500)
# # fluidsynth.stop()
#

import subprocess
from pydub import AudioSegment
from music21 import *
import music21


def generate_midi_by_notes(notes, durations, midi_out_path):
    melody_stream = stream.Stream()

    for i in range(len(notes)):
        current_note = music21.note.Note(notes[i], duration=duration.Duration(durations[i]))
        melody_stream.append(current_note)

    midi_data = midi.translate.streamToMidiFile(melody_stream)

    midi_data.open(midi_out_path, 'wb')
    midi_data.write()
    midi_data.close()


def midi_to_wav(midi_path, wav_path, soundfont_file=r"Roland_SC-88.sf2", mp3=False):
    fluidsynth_cmd = [
        "fluidsynth",
        "-F", wav_path,
        "-ni", soundfont_file,
        midi_path
    ]

    subprocess.call(fluidsynth_cmd)
    if mp3:
        wav_audio = AudioSegment.from_wav(wav_path)
        mp3_path = wav_path.split('.')[0] + ".mp3"
        wav_audio.export(mp3_path, format="mp3")

        # (Optional) Set ID3 tags on the MP3 file
        mp3_audio_tags = {"title": "Melody", "artist": "Me", "album": "My Album"}
        mp3_audio = AudioSegment.from_mp3(mp3_path)
        mp3_audio.export(mp3_path, format="mp3", tags=mp3_audio_tags)