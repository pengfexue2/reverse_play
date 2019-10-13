#!/usr/bin/env python
# encoding: utf-8
# @Time : 2019-10-12 00:03

__author__ = 'Ted'


from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("love.mp3")
backwards = song.reverse()
backwards.export("result.mp3",format="mp3")
play(backwards)