bad apple on linux terminal
----------------------------------

1) if you want any other video to be converted just cut it with frames via ffmpeg.
best way to do this is to run following command in terminal

    `ffmpeg -i yourvideo.mp4 img%04d.jpeg`

2) ...Then copy those frames into ``` badAppleFrames``` folder (feel free to modify code)

3) Next, empty ```converted``` folder and run ``` frames-to-ascii.py``` 

####Finally, the tricky part
open your terminal and change size  (its up to you how you change, but increase cell spacing by 2x)

REMEMBER: modify  `runner.py:4`. Faster your pc, bigger the number.

--------------------------------------
####COPYRIGHT FREE
please support my work and at least share it with friends.
have fun :)

------------------------------------
SEE VIDEO https://www.youtube.com/watch?v=Rk9t-RjtDYI

P.S if there will be demand I will upload tutorial of everything