# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

def onOffToOn(channel, sampleIndex, val, prev):
	return

def whileOn(channel, sampleIndex, val, prev):
	
	# CHOP NULLs for MediaPipe coordinates
	lefthand = op('x_y_left_hand') 
	righthand = op('x_y_right_hand')
	head = op('x_y_head')
	leftfoot = op('x_y_left_foot')
	rightfoot = op('x_y_right_foot')
	spinebase = op('x_y_spine_base')

	# TRANSFORM TOPs for each marker
	trans_lefthand = op('trans_lefthand')
	trans_righthand = op('trans_righthand')
	trans_head = op('trans_head')
	trans_leftfoot = op('trans_leftfoot')
	trans_rightfoot = op('trans_rightfoot')
	trans_spinebase = op('trans_spinebase')

	# Reference TOP for resolution for clamping (camera stream)
	camera_top = op('camera_width_height')
	width_clamp = camera_top.width
	height_clamp = camera_top.height
	
	# Resolution of null2 (visuals)
	base_top = op('null2')
	width = base_top.width
	height = base_top.height
	widthSlashHeight = width/height

	# Debug toggle
	debug_value = op('debugValue')[0]
	
	def set_output_resolution(trans, base_top):
		trans.par.outputresolution = 'custom'
		trans.par.resolutionw = base_top.width
		trans.par.resolutionh = base_top.height
		
	set_output_resolution(trans_lefthand, base_top)
	set_output_resolution(trans_righthand, base_top)
	set_output_resolution(trans_head, base_top)
	set_output_resolution(trans_leftfoot, base_top)
	set_output_resolution(trans_rightfoot, base_top)
	set_output_resolution(trans_spinebase, base_top)
	set_output_resolution(op('circle2'), base_top)

	def get_pixel_coords(chop):
		x_norm = chop['x'].eval()
		y_norm = chop['y'].eval()
		x_px = x_norm * width - width/2 
		y_px = -(y_norm * height - height / 2)
		return x_px, y_px

	def update_layout(trs_top, chop): 
		x, y = get_pixel_coords(chop)
		trs_top.par.tx = x
		trs_top.par.ty = y
		trs_top.par.sx = 1
		trs_top.par.sy = 1

	if debug_value > 0:
		update_layout(trans_lefthand, lefthand)
		update_layout(trans_righthand, righthand)
		update_layout(trans_head, head)
		update_layout(trans_leftfoot, leftfoot)
		update_layout(trans_rightfoot, rightfoot)
		update_layout(trans_spinebase, spinebase)
	else:
		for layout in [trans_lefthand, trans_righthand, trans_head, trans_leftfoot, trans_rightfoot, trans_spinebase]:
			layout.par.sx = 0
			layout.par.sy = 0

	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	return
	