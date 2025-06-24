# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

import math
import numpy as np
from collections import defaultdict

def onOffToOn(channel, sampleIndex, val, prev):
	return

def whileOn(channel, sampleIndex, val, prev):
	return

# Maintain velocity history for blobs
if 'blob_velocities' not in globals():
	blob_velocities = defaultdict(lambda: [0.0, 0.0])  # Indexed by blob index

# Helper function to assign a value to a CHOP parameter (typically "value0")
def assignToNode(node_name, value):
	node = op(node_name)
	if node is None:
		print(f"Error: Node {node_name} not found.")
		return  # Node not found, skip assignment
	if hasattr(node.par, 'value0'):
		node.par.value0 = value
	else:
		print(f"Warning: {node_name} does not have a 'value0' parameter.")
	
def whileOn(channel, sampleIndex, val, prev):
	
	# DATA CALLS ------------------
	
	# Extract data from Select DATs (MEDIAPIPE) "MediaPipe landmark positions" (in 3D MediaPipe coordinate space)
	# x
	# y
	# z
	# confidence
	mediapipe_positions = {}
	joint_list = [
	'nose', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow', 'left_wrist',
	'right_wrist', 'left_index', 'right_index', 'left_hip', 'right_hip', 'left_knee',
	'right_knee', 'left_ankle', 'right_ankle', 'left_foot_index', 'right_foot_index',
	'left_eye_inner', 'left_eye', 'left_eye_outer', 'right_eye_inner', 'right_eye',
	'right_eye_outer', 'left_ear', 'right_ear', 'mouth_left', 'mouth_right',
	'left_pinky', 'right_pinky', 'left_thumb', 'right_thumb', 'left_heel', 'right_heel'
	]

	for joint in joint_list:
		dat = op(joint)
		if dat is None:
			continue
		try:
			x = float(dat[0, 0])
			y = float(dat[0, 1])
			z = float(dat[0, 2])
			conf = float(dat[0, 3]) if dat.numCols > 3 else 1.0
		except Exception as e:
			x = y = z = 0.0
			conf = 0.0
		mediapipe_positions[joint] = (x, y, z, conf)

	# Use MediaPipe data as the unified skeleton (Kinect data and fusion are removed)
	skeleton_positions = mediapipe_positions.copy()

	# Calculate 2D SpineBase as average of left_hip and right_hip
	if 'left_hip' in mediapipe_positions and 'right_hip' in mediapipe_positions:
		lx, ly, lz, lc = mediapipe_positions['left_hip']
		rx, ry, r, rc = mediapipe_positions['right_hip']
		spine_x = (lx + rx) / 2.0
		spine_y = (ly + ry) / 2.0
	else:
		print("Fallback to spine 0.5 x y")
		spine_x = spine_y = 0.5  # fallback center

	# (We assume MediaPipe origin at hip center; this provides a "SpineBase" similar to Kinect for distance calculations.)

	# DISTANCE ------------------ WITHOUT STANDARDIZE BY SHOULDER DISTANCE
	
	# Calculate distances and angles using MediaPipe-only data
	def calc_distance(j1, j2):
		if j1 not in skeleton_positions or j2 not in skeleton_positions:
			return 0.0
		x1, y1, z1, _ = skeleton_positions[j1]
		x2, y2, z2, _ = skeleton_positions[j2]
		dx, dy, dz = x1 - x2, y1 - y2, z1 - z2
		return math.sqrt(dx*dx + dy*dy + dz*dz)
		
	# ANGLE --------------------------------------

	def calc_angle(j1, j2, j3):
		# Angle at j2 formed by segments j2->j1 and j2->j3
		if j1 not in skeleton_positions or j2 not in skeleton_positions or j3 not in skeleton_positions:
			return 0.0
		x1, y1, z1, _ = skeleton_positions[j1]
		x2, y2, z2, _ = skeleton_positions[j2]
		x3, y3, z3, _ = skeleton_positions[j3]
		# Vector from j2 to j1 and j2 to j3
		v1 = (x1 - x2, y1 - y2, z1 - z2)
		v2 = (x3 - x2, y3 - y2, z3 - z2)
		# Compute angle via dot product
		dot = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
		mag1 = math.sqrt(v1[0]**2 + v1[1]**2 + v1[2]**2)
		mag2 = math.sqrt(v2[0]**2 + v2[1]**2 + v2[2]**2)
		if mag1 < 1e-6 or mag2 < 1e-6:
			return 0.0
		cosang = dot / (mag1 * mag2)
		# Clamp cosang to valid range [-1,1] to avoid math domain errors
		cosang = max(-1.0, min(1.0, cosang))
		angle_deg = math.degrees(math.acos(cosang))
		return angle_deg
		
	# SCRIPT CALLS FOR RELATIONS ----------------------------

	# Distances
	assignToNode('distance_shoulders', calc_distance('left_shoulder', 'right_shoulder'))
	assignToNode('distance_elbows', calc_distance('left_elbow', 'right_elbow'))
	assignToNode('distance_wrists', calc_distance('left_wrist', 'right_wrist'))
	assignToNode('distance_knees', calc_distance('left_knee', 'right_knee'))
	assignToNode('distance_ankles', calc_distance('left_ankle', 'right_ankle'))
	assignToNode('distance_nose_left_shoulder', calc_distance('nose', 'left_shoulder'))
	assignToNode('distance_nose_right_shoulder', calc_distance('nose', 'right_shoulder'))
	assignToNode('distance_left_shoulder_left_hip', calc_distance('left_shoulder', 'left_hip'))
	assignToNode('distance_left_hip_left_knee', calc_distance('left_hip', 'left_knee'))
	assignToNode('distance_right_hip_right_knee', calc_distance('right_hip', 'right_knee'))
	assignToNode('distance_left_knee_left_ankle', calc_distance('left_knee', 'left_ankle'))
	assignToNode('distance_right_knee_right_ankle', calc_distance('right_knee', 'right_ankle'))
	
	# Angles
	assignToNode('angle_left_shoulder', calc_angle('left_hip', 'left_shoulder', 'left_elbow'))
	assignToNode('angle_right_shoulder', calc_angle('right_hip', 'right_shoulder', 'right_elbow'))

	assignToNode('angle_left_elbow', calc_angle('left_shoulder', 'left_elbow', 'left_wrist'))
	assignToNode('angle_right_elbow', calc_angle('right_shoulder', 'right_elbow', 'right_wrist'))

	assignToNode('angle_left_hip', calc_angle('left_shoulder', 'left_hip', 'left_knee'))
	assignToNode('angle_right_hip', calc_angle('right_shoulder', 'right_hip', 'right_knee'))

	assignToNode('angle_left_knee', calc_angle('left_hip', 'left_knee', 'left_ankle'))
	assignToNode('angle_right_knee', calc_angle('right_hip', 'right_knee', 'right_ankle'))

	assignToNode('angle_left_hip_left_wrist', calc_angle('left_shoulder', 'left_hip', 'left_wrist'))
	assignToNode('angle_right_hip_right_wrist', calc_angle('right_shoulder', 'right_hip', 'right_wrist'))
	
	assignToNode('angle_right_shoulder_right_hand', calc_angle('right_shoulder', 'right_hip', 'right_wrist'))
	assignToNode('angle_left_shoulder_left_hand', calc_angle('left_shoulder', 'left_hip', 'left_wrist'))
	assignToNode('angle_left_hip_left_foot', calc_angle('left_hip', 'left_foot_index', 'left_shoulder'))
	assignToNode('angle_right_hip_right_foot', calc_angle('right_hip', 'right_foot_index', 'right_shoulder'))
	
	return


def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	return
	