import math
from filterpy.kalman import KalmanFilter
import numpy as np

kalman_filters = {}

def apply_kalman_filter(kf, landmark, kinect_z):
		kf.predict()
		kf.update(np.array(landmark))
		# Fuse the z data from landmarks and Kinect
		fused_z = (kf.x[2] + kinect_z) / 2  # Simple averaging, can be replaced with weighted averaging
		kf.x[2] = fused_z
		return kf.x

def onCook(scriptOp):
	global kalman_filters
	
	scriptOp.clear()
	
	# DATA CALLS ------------------
	
	# Extract data from Select DATs (MEDIAPIPE)
	# x
	# y
	# z
	# visibility
	landmarks = {

		# used by the kinect aswell
		'nose': [float(op('nose')[0, 0]), float(op('nose')[0, 1]), float(op('nose')[0, 2]), float(op('nose')[0, 3])],
		'left_shoulder': [float(op('left_shoulder')[0, 0]), float(op('left_shoulder')[0, 1]), float(op('left_shoulder')[0, 2]), float(op('left_shoulder')[0, 3])],
		'right_shoulder': [float(op('right_shoulder')[0, 0]), float(op('right_shoulder')[0, 1]), float(op('right_shoulder')[0, 2]), float(op('right_shoulder')[0, 3])],
		'left_elbow': [float(op('left_elbow')[0, 0]), float(op('left_elbow')[0, 1]), float(op('left_elbow')[0, 2]), float(op('left_elbow')[0, 3])],
		'right_elbow': [float(op('right_elbow')[0, 0]), float(op('right_elbow')[0, 1]), float(op('right_elbow')[0, 2]), float(op('right_elbow')[0, 3])],
		'left_wrist': [float(op('left_wrist')[0, 0]), float(op('left_wrist')[0, 1]), float(op('left_wrist')[0, 2]), float(op('left_wrist')[0, 3])],
		'right_wrist': [float(op('right_wrist')[0, 0]), float(op('right_wrist')[0, 1]), float(op('right_wrist')[0, 2]), float(op('right_wrist')[0, 3])],
		'left_index': [float(op('left_index')[0, 0]), float(op('left_index')[0, 1]), float(op('left_index')[0, 2]), float(op('left_index')[0, 3])],
		'right_index': [float(op('right_index')[0, 0]), float(op('right_index')[0, 1]), float(op('right_index')[0, 2]), float(op('right_index')[0, 3])],
		'left_hip': [float(op('left_hip')[0, 0]), float(op('left_hip')[0, 1]), float(op('left_hip')[0, 2]), float(op('left_hip')[0, 3])],
		'right_hip': [float(op('right_hip')[0, 0]), float(op('right_hip')[0, 1]), float(op('right_hip')[0, 2]), float(op('right_hip')[0, 3])],
		'left_knee': [float(op('left_knee')[0, 0]), float(op('left_knee')[0, 1]), float(op('left_knee')[0, 2]), float(op('left_knee')[0, 3])],
		'right_knee': [float(op('right_knee')[0, 0]), float(op('right_knee')[0, 1]), float(op('right_knee')[0, 2]), float(op('right_knee')[0, 3])],
		'left_ankle': [float(op('left_ankle')[0, 0]), float(op('left_ankle')[0, 1]), float(op('left_ankle')[0, 2]), float(op('left_ankle')[0, 3])],
		'right_ankle': [float(op('right_ankle')[0, 0]), float(op('right_ankle')[0, 1]), float(op('right_ankle')[0, 2]), float(op('right_ankle')[0, 3])],
		'left_foot_index': [float(op('left_foot_index')[0, 0]), float(op('left_foot_index')[0, 1]), float(op('left_foot_index')[0, 2]), float(op('left_foot_index')[0, 3])],
		'right_foot_index': [float(op('right_foot_index')[0, 0]), float(op('right_foot_index')[0, 1]), float(op('right_foot_index')[0, 2]), float(op('right_foot_index')[0, 3])],
		
		# not used
		'left_eye_inner': [float(op('left_eye_inner')[0, 0]), float(op('left_eye_inner')[0, 1]), float(op('left_eye_inner')[0, 2]), float(op('left_eye_inner')[0, 3])],
		'left_eye': [float(op('left_eye')[0, 0]), float(op('left_eye')[0, 1]), float(op('left_eye')[0, 2]), float(op('left_eye')[0, 3])],
		'left_eye_outer': [float(op('left_eye_outer')[0, 0]), float(op('left_eye_outer')[0, 1]), float(op('left_eye_outer')[0, 2]), float(op('left_eye_outer')[0, 3])],
		'right_eye_inner': [float(op('right_eye_inner')[0, 0]), float(op('right_eye_inner')[0, 1]), float(op('right_eye_inner')[0, 2]), float(op('right_eye_inner')[0, 3])],
		'right_eye': [float(op('right_eye')[0, 0]), float(op('right_eye')[0, 1]), float(op('right_eye')[0, 2]), float(op('right_eye')[0, 3])],
		'right_eye_outer': [float(op('right_eye_outer')[0, 0]), float(op('right_eye_outer')[0, 1]), float(op('right_eye_outer')[0, 2]), float(op('right_eye_outer')[0, 3])],
		'left_ear': [float(op('left_ear')[0, 0]), float(op('left_ear')[0, 1]), float(op('left_ear')[0, 2]), float(op('left_ear')[0, 3])],
		'right_ear': [float(op('right_ear')[0, 0]), float(op('right_ear')[0, 1]), float(op('right_ear')[0, 2]), float(op('right_ear')[0, 3])],
		'mouth_left': [float(op('mouth_left')[0, 0]), float(op('mouth_left')[0, 1]), float(op('mouth_left')[0, 2]), float(op('mouth_left')[0, 3])],
		'mouth_right': [float(op('mouth_right')[0, 0]), float(op('mouth_right')[0, 1]), float(op('mouth_right')[0, 2]), float(op('mouth_right')[0, 3])],
		'left_pinky': [float(op('left_pinky')[0, 0]), float(op('left_pinky')[0, 1]), float(op('left_pinky')[0, 2]), float(op('left_pinky')[0, 3])],
		'right_pinky': [float(op('right_pinky')[0, 0]), float(op('right_pinky')[0, 1]), float(op('right_pinky')[0, 2]), float(op('right_pinky')[0, 3])],
		'left_thumb': [float(op('left_thumb')[0, 0]), float(op('left_thumb')[0, 1]), float(op('left_thumb')[0, 2]), float(op('left_thumb')[0, 3])],
		'right_thumb': [float(op('right_thumb')[0, 0]), float(op('right_thumb')[0, 1]), float(op('right_thumb')[0, 2]), float(op('right_thumb')[0, 3])],
		'left_heel': [float(op('left_heel')[0, 0]), float(op('left_heel')[0, 1]), float(op('left_heel')[0, 2]), float(op('left_heel')[0, 3])],
		'right_heel': [float(op('right_heel')[0, 0]), float(op('right_heel')[0, 1]), float(op('right_heel')[0, 2]), float(op('right_heel')[0, 3])]
	}
	
	array_of_not_shared = [
	'left_eye_inner',
    'left_eye',
    'left_eye_outer',
    'right_eye_inner',
    'right_eye',
    'right_eye_outer',
    'left_ear',
    'right_ear',
    'mouth_left',
    'mouth_right',
    'left_pinky',
    'right_pinky',
    'left_thumb',
    'right_thumb',
    'left_heel',
    'right_heel'
	]
	
	# EXTRACT FROM SELECT CHOPS (KINECT)
	# 0 tx
	# 1 ty
	# 2 tz
	# 3 u
	# 4 v
	# 5 depthu
	# 6 depthv
	kinect_nodes = {
		# head is kalman filtered with nose from landmarks
		'nose': [float(op('head')['tx']), float(op('head')['ty']), float(op('head')['tz']), float(op('head')['u']), float(op('head')['v']), float(op('head')['depthu']), float(op('head')['depthv'])],
		# l_shoulder is kalman filtered with left_shoulder from landmarks
		'left_shoulder': [float(op('l_shoulder')['tx']), float(op('l_shoulder')['ty']), float(op('l_shoulder')['tz']), float(op('l_shoulder')['u']), float(op('l_shoulder')['v']), float(op('l_shoulder')['depthu']), float(op('l_shoulder')['depthv'])],
		# r_shoulder is kalman filtered with right_shoulder from landmarks
		'right_shoulder': [float(op('r_shoulder')['tx']), float(op('r_shoulder')['ty']), float(op('r_shoulder')['tz']), float(op('r_shoulder')['u']), float(op('r_shoulder')['v']), float(op('r_shoulder')['depthu']), float(op('r_shoulder')['depthv'])],
		# l_elbow is kalman filtered with right_elbow from landmarks
		'left_elbow': [float(op('l_elbow')['tx']), float(op('l_elbow')['ty']), float(op('l_elbow')['tz']), float(op('l_elbow')['u']), float(op('l_elbow')['v']), float(op('l_elbow')['depthu']), float(op('l_elbow')['depthv'])],
		# r_elbow is kalman filtered with right_elbow from landmarks
		'right_elbow': [float(op('r_elbow')['tx']), float(op('r_elbow')['ty']), float(op('r_elbow')['tz']), float(op('r_elbow')['u']), float(op('r_elbow')['v']), float(op('r_elbow')['depthu']), float(op('r_elbow')['depthv'])],
		# l_wrist is kalman filtered with left_wrist from landmarks
		'left_wrist': [float(op('l_wrist')['tx']), float(op('l_wrist')['ty']), float(op('l_wrist')['tz']), float(op('l_wrist')['u']), float(op('l_wrist')['v']), float(op('l_wrist')['depthu']), float(op('l_wrist')['depthv'])],
		# r_wrist is kalman filtered with right_wrist from landmarks
		'right_wrist': [float(op('r_wrist')['tx']), float(op('r_wrist')['ty']), float(op('r_wrist')['tz']), float(op('r_wrist')['u']), float(op('r_wrist')['v']), float(op('r_wrist')['depthu']), float(op('r_wrist')['depthv'])],
		# l_handtip is kalman filtered with left_index from landmarks
		'left_index': [float(op('l_handtip')['tx']), float(op('l_handtip')['ty']), float(op('l_handtip')['tz']), float(op('l_handtip')['u']), float(op('l_handtip')['v']), float(op('l_handtip')['depthu']), float(op('l_handtip')['depthv'])],
		# r_handtip is kalman filtered with right_index from landmarks
		'right_index': [float(op('r_handtip')['tx']), float(op('r_handtip')['ty']), float(op('r_handtip')['tz']), float(op('r_handtip')['u']), float(op('r_handtip')['v']), float(op('r_handtip')['depthu']), float(op('r_handtip')['depthv'])],
		# l_hip is kalman filtered with left_hip from landmarks
		'left_hip': [float(op('l_hip')['tx']), float(op('l_hip')['ty']), float(op('l_hip')['tz']), float(op('l_hip')['u']), float(op('l_hip')['v']), float(op('l_hip')['depthu']), float(op('l_hip')['depthv'])],
		# r_hip is kalman filtered with right_hip from landmarks
		'right_hip': [float(op('r_hip')['tx']), float(op('r_hip')['ty']), float(op('r_hip')['tz']), float(op('r_hip')['u']), float(op('r_hip')['v']), float(op('r_hip')['depthu']), float(op('r_hip')['depthv'])],
		# l_knee is kalman filtered with left_knee from landmarks
		'left_knee': [float(op('l_knee')['tx']), float(op('l_knee')['ty']), float(op('l_knee')['tz']), float(op('l_knee')['u']), float(op('l_knee')['v']), float(op('l_knee')['depthu']), float(op('l_knee')['depthv'])],
		# r_knee is kalman filtered with left_knee from landmarks
		'right_knee': [float(op('r_knee')['tx']), float(op('r_knee')['ty']), float(op('r_knee')['tz']), float(op('r_knee')['u']), float(op('r_knee')['v']), float(op('r_knee')['depthu']), float(op('r_knee')['depthv'])],
		# left_ankle is kalman filtered with left_ankle from landmarks
		'left_ankle': [float(op('l_ankle')['tx']), float(op('l_ankle')['ty']), float(op('l_ankle')['tz']), float(op('l_ankle')['u']), float(op('l_ankle')['v']), float(op('l_ankle')['depthu']), float(op('l_ankle')['depthv'])],
		# right_ankle is kalman filtered with right_ankle from landmarks
		'right_ankle': [float(op('r_ankle')['tx']), float(op('r_ankle')['ty']), float(op('r_ankle')['tz']), float(op('r_ankle')['u']), float(op('r_ankle')['v']), float(op('r_ankle')['depthu']), float(op('r_ankle')['depthv'])],
		# l_foot is kalman filtered with left_foot_index from landmarks
		'left_foot_index': [float(op('l_foot')['tx']), float(op('l_foot')['ty']), float(op('l_foot')['tz']), float(op('l_foot')['u']), float(op('l_foot')['v']), float(op('l_foot')['depthu']), float(op('l_foot')['depthv'])],
		# r_foot' is kalman filtered with right_foot_index from landmarks
		'right_foot_index': [float(op('r_foot')['tx']), float(op('r_foot')['ty']), float(op('r_foot')['tz']), float(op('r_foot')['u']), float(op('r_foot')['v']), float(op('r_foot')['depthu']), float(op('r_foot')['depthv'])]
	}


	# KALMAN FILTER ------------

	def initialize_kalman_filter():
		kf = KalmanFilter(dim_x=4, dim_z=4)
		kf.x = np.array([0., 0., 0., 0.])  # Initial state (x, y, z, visibility)
		kf.F = np.array([[1., 0., 0., 0.],
						[0., 1., 0., 0.],
						[0., 0., 1., 0.],
						[0., 0., 0., 1.]])  # State transition matrix
		kf.H = np.array([[1., 0., 0., 0.],
						[0., 1., 0., 0.],
						[0., 0., 1., 0.],
						[0., 0., 0., 1.]])  # Measurement matrix
		kf.P *= 1000.  # Covariance matrix
		kf.R = np.array([[1., 0., 0., 0.],
						[0., 1., 0., 0.],
						[0., 0., 1., 0.],
						[0., 0., 0., 1.]])  # Measurement noise
		kf.Q = np.array([[0.1, 0., 0., 0.],
						[0., 0.1, 0., 0.],
						[0., 0., 0.1, 0.],
						[0., 0., 0., 0.1]])  # Process noise
		return kf
		
	# Initialize Kalman filters if not already done
	for key in landmarks.keys():
		if key not in kalman_filters:
			kalman_filters[key] = initialize_kalman_filter()

	
	# Apply Kalman Filter to each landmark and fuse z data with Kinect nodes
	for key, value in landmarks.items():
		if key not in array_of_not_shared:
			kinect_z = kinect_nodes[key][2]  # Extract z data from Kinect nodes
			smoothed_value = apply_kalman_filter(kalman_filters[key], value, kinect_z)
			landmarks[key] = smoothed_value.tolist()


	# DISTANCE ------------------ WITH STANDARDIZE BY SHOULDER DISTANCE
	
	# Function to calculate distance between two points in 3D space non_standardised
	def calculate_distance_nonStandardised(point1, point2):
		x1, y1, z1, _ = point1
		x2, y2, z2, _ = point2
		return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
	
	CONSTANT_SHOULDER_VALUE = op('shoulder_distance')['chan1']
	
	left_shoulder = [float(op('left_shoulder')[0, 0]), float(op('left_shoulder')[0, 1]), float(op('left_shoulder')[0, 2]), float(op('left_shoulder')[0, 3])]
	right_shoulder = [float(op('right_shoulder')[0, 0]), float(op('right_shoulder')[0, 1]), float(op('right_shoulder')[0, 2]), float(op('right_shoulder')[0, 3])]
	
	MeasuredShoulderValue = calculate_distance_nonStandardised(left_shoulder, right_shoulder)
	
	# Triangle Similiarity Method: Function using a measured shoulder distance as a pre-known and the measured shoulder distance of the live measure
	def standardisedByShoulders(value):
		return value * CONSTANT_SHOULDER_VALUE/MeasuredShoulderValue

	# Function to calculate distance between two points in 3D space
	def calculate_distance(point1, point2):
		if not checkIfVisible(point1) or not checkIfVisible(point2):
			return -1
		x1, y1, z1, _ = point1
		x2, y2, z2, _ = point2
		result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
		return standardisedByShoulders(result)

		
	# ANGLE --------------------------------------

	# Function to calculate angle between three points
	def calculate_angle(point1, point2, point3):
		if not checkIfVisible(point1) or not checkIfVisible(point2) or not checkIfVisible(point3):
			return -1
		x1, y1, z1, _ = point1
		x2, y2, z2, _ = point2
		x3, y3, z3, _ = point3
		vector1 = [x1 - x2, y1 - y2, z1 - z2]
		vector2 = [x3 - x2, y3 - y2, z3 - z2]
		dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
		magnitude1 = math.sqrt(sum(v**2 for v in vector1))
		magnitude2 = math.sqrt(sum(v**2 for v in vector2))
		cos_theta = dot_product / (magnitude1 * magnitude2)
		angle = math.acos(cos_theta) * (180 / math.pi)  # Convert to degrees
		return angle
		
	# HELPER -------------------------------------

		
	# Check if a point is visible
	def checkIfVisible(point):
		_, _, _, visibility = point
		return visibility >= 0.1

		
	# Function to help with good assigning
	def assignToNode(nodeNameWithoutOp, value):
		# state node
		chop = op(nodeNameWithoutOp)
		# append new value
		chop.par.value0 = value
		
		
	# SCRIPT CALLS FOR RELATIONS ----------------------------

	# Distances
	assignToNode('distance_shoulders', calculate_distance(landmarks['left_shoulder'], landmarks['right_shoulder']))
	assignToNode('distance_hips', calculate_distance(landmarks['left_hip'], landmarks['right_hip']))
	assignToNode('distance_elbows', calculate_distance(landmarks['left_elbow'], landmarks['right_elbow']))
	assignToNode('distance_wrists', calculate_distance(landmarks['left_wrist'], landmarks['right_wrist']))
	assignToNode('distance_knees', calculate_distance(landmarks['left_knee'], landmarks['right_knee']))
	assignToNode('distance_ankles', calculate_distance(landmarks['left_ankle'], landmarks['right_ankle']))
	assignToNode('distance_feet', calculate_distance(landmarks['left_foot_index'], landmarks['right_foot_index']))
	assignToNode('distance_nose_left_shoulder', calculate_distance(landmarks['nose'], landmarks['left_shoulder']))
	assignToNode('distance_nose_right_shoulder', calculate_distance(landmarks['nose'], landmarks['right_shoulder']))
	assignToNode('distance_left_shoulder_left_hip', calculate_distance(landmarks['left_shoulder'], landmarks['left_hip']))
	assignToNode('distance_right_shoulder_right_hip', calculate_distance(landmarks['right_shoulder'], landmarks['right_hip']))
	assignToNode('distance_left_hip_left_knee', calculate_distance(landmarks['left_hip'], landmarks['left_knee']))
	assignToNode('distance_right_hip_right_knee', calculate_distance(landmarks['right_hip'], landmarks['right_knee']))
	assignToNode('distance_left_knee_left_ankle', calculate_distance(landmarks['left_knee'], landmarks['left_ankle']))
	assignToNode('distance_right_knee_right_ankle', calculate_distance(landmarks['right_knee'], landmarks['right_ankle']))
	
	# Angles
	assignToNode('angle_left_shoulder', calculate_angle(landmarks['left_hip'], landmarks['left_shoulder'], landmarks['left_elbow']))
	assignToNode('angle_right_shoulder', calculate_angle(landmarks['right_hip'], landmarks['right_shoulder'], landmarks['right_elbow']))

	assignToNode('angle_left_elbow', calculate_angle(landmarks['left_shoulder'], landmarks['left_elbow'], landmarks['left_wrist']))
	assignToNode('angle_right_elbow', calculate_angle(landmarks['right_shoulder'], landmarks['right_elbow'], landmarks['right_wrist']))

	assignToNode('angle_left_hip', calculate_angle(landmarks['left_shoulder'], landmarks['left_hip'], landmarks['left_knee']))
	assignToNode('angle_right_hip', calculate_angle(landmarks['right_shoulder'], landmarks['right_hip'], landmarks['right_knee']))

	assignToNode('angle_left_knee', calculate_angle(landmarks['left_hip'], landmarks['left_knee'], landmarks['left_ankle']))
	assignToNode('angle_right_knee', calculate_angle(landmarks['right_hip'], landmarks['right_knee'], landmarks['right_ankle']))

	assignToNode('angle_left_hip_left_wrist', calculate_angle(landmarks['left_shoulder'], landmarks['left_hip'], landmarks['left_wrist']))
	assignToNode('angle_right_hip_right_wrist', calculate_angle(landmarks['right_shoulder'], landmarks['right_hip'], landmarks['right_wrist']))

	
	return