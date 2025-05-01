# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 

import math
from td import absTime

# ───── persistent animation state ─────
animating        = False
anim_start_time  = 0.0
anim_start_value = 0.0
anim_target      = 0
anim_value       = 0.0
last_logic       = 0

# ───── external CHOPs ─────
blend_param_op = op('blend_param')  # ← Constant CHOP with 'chan1'
switch_op      = op('switch1')      # Switch TOP

def whileOn(channel, sampleIndex, val, prev):
	global animating, anim_start_time, anim_start_value, anim_target, anim_value, last_logic

	# ───── determine current logic state ─────
	spine  = op('spinebase')
	hand_l = op('handleft')
	hand_r = op('handright')

	sy = spine['y'][0]
	ly = hand_l['y'][0]
	ry = hand_r['y'][0]

	logic = 1 if (ly < sy or ry < sy) else 0

	# ───── detect transition (0→1 or 1→0) ─────
	if logic != last_logic:
		anim_start_time  = absTime.seconds
		anim_start_value = anim_value
		anim_target      = logic
		animating        = True
		last_logic       = logic

	# ───── fetch blend duration from Null CHOP ─────
	blend_time = blend_param_op['chan1'][0]
	blend_time = max(0.001, float(blend_time))  # avoid divide-by-zero | safety clam

	# ───── update animation if in progress ─────
	if animating:
		t = (absTime.seconds - anim_start_time) / blend_time
		if t >= 1.0:
			t = 1.0
			animating = False  # finished
		anim_value = anim_start_value + (anim_target - anim_start_value) * t
	else:
		anim_value = float(anim_target)

	# ───── write interpolated value to switch ─────
	switch_op.par.index = anim_value

	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	return
	