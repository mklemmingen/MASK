# MASK

In this repo, I document the development process and present M.A.S.K. (Machine-Learning Assisted Skeleton Kinect Tracking), an approach for threshold-based pose recognition in TouchDesigner using a KinectV2, MediaPipe, and their connection via data synchronization and a Kalman filter. The system utilizes machine learning to improve Kinect skeleton tracking and aims to enable precise pose recognition. The workflow integrates the TouchDesigner Kinect node with a MediaPipe pipeline for extracting and processing skeleton values. These values are visualized for troubleshooting and used to set thresholds for skeleton node relationships. These skeleton points are queried in parallel for pattern matching. This allows for the recognition of pose patterns via chaining of node relations. The system aims to show improvements in accuracy and responsiveness. 

It was developed primarily for servitude as a tool for applications in interactive media and performance art, but can be extended onto other projects that have a kinect at hand and want to improve their tracking. It was created as a technical component of a student project under the direction of the Filmakademie Ludwigsburg.

the .toe has been certified working on 2023.12120 since it was a requirement by the stakeholders. Compatibility is not assured, but a overall project structure and the python scripts should remain the same. Please check for correct and compatible calls via the op() method that suits your version, since the call has been outdated in newer versions.

# How to Use / Setup Step-By-Step
for mediapipe, this project uses another github projects mediapipe configuration for GPU Acceleration as external toxes. You need to download the last compatible release via:

https://github.com/torinmb/mediapipe-touchdesigner/archive/refs/tags/v0.5.0.zip

Extract it, and put the toxes folder in the root of this project, so that the .toe access the toxes folder from its location. It needs access to pose aswell as mediapipe.tox atleast.

For the next step, make sure that when opening the .toe, you have selected the right camera in the mediapipe node and are in frame. Relations will show -1 as a value in its constant nodes if the visibility of the node is under a certain rule based threshold. You might also need to make sure that in the kinect node, it is set to ON.

Using the elongated python script, you can add your own relations if needed. 
Otherwise, use the constant CHOPs to chain together Triggers as needed
