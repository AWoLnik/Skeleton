#Skeleton#
##For the Ivanti challenge at YHack 2018##

Skeleton aims to improve remote GUI performance by simplifying frames to their "skeletons" that are relevant for IT professionals, avoiding the need for video or bitmap streaming. The tool accomplishes this by using a deep convolutional neural network to identify UI features in frames, and optical character recognition to pull text from frames. These essential features are then transmitted in a small JSON array, and reconstructed into a minimal GUI on the remote agent's desktop.

The project could certainly benefit from further training on a better data set, and implementation of interactivity in the agent GUI.

The GitHub repo does not contain the trained model, and cannot be run without it. 
The model is too large to share in this formats, but we can provide it upon request. 
Once the model is in the root directory of the project, simply run ./skeleton.sh [image.file] to process the image and render the minimal GUI based on it.
