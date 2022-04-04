# RallyeChambre

Webcam needed

Quick code to make a fun escape game activity. You need to have mediapipe and opencv dependencies for python.
If you don't you can type in your commande prompt (if you have python in PATH) :
pip install mediapipe
pip install opencv-python

Just run the code (py test-rallye.py) on a command prompt, it will connect to your webcam and show strings of bits. I used a dual screen, pressed alt + enter to fullscreen the command prompt and a youtube video of a waving flag on the second screen. The arrow icon was hidden by the full screen video.

If more than 4 people are on the camera at the same time it will interrupt the strings of bits and ask for a password.
You can change the threshold of that detection to have more people on the camera if you want. 

My camera had a cache on during the escape game so that people couldn't be detected ahead of time. 
