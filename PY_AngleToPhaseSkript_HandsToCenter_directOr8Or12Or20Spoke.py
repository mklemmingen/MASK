import math

# ---------- Angle → phase helper  ----------------------------------

# Continuous helper (kept for reference)
def angle_to_phase(angle_rad: float) -> float:
	"""atan2 → phase in [0‑1), 0 ≙ 45 ° clockwise (southeast)."""
	return ((2*math.pi - angle_rad + math.pi/4) / (2*math.pi)) % 1.0

# snap to the nearest of the eight spokes
def angle_to_phase_8(angle_rad: float) -> float:
	"""
	Map angle to one of eight 45‑degree steps.
	Phase indices run counter‑clockwise as required:
		0/8  = SE,   1/8 = E,   2/8 = NE, 3/8 = N,
		4/8  = NW,   5/8 = W,   6/8 = SW, 7/8 = S
	"""
	p = angle_to_phase(angle_rad)          # 0‑1 (continuous)
	idx = int(p * 8 + 0.5) % 8             # nearest 45 °
	return idx / 8.0                       # discrete phase (0‑1)
	
# snap to nearest of 12!
def angle_to_phase_12(angle_rad: float) -> float:
    """
    Map angle to one of twelve 30‑degree steps.
        0/12  = 45 °  (SE)      3/12 = 315 ° (NE)     6/12 = 225 ° (NW)
        1/12  = 15 °  (ESE)     4/12 = 285 ° (NNE)    7/12 = 195 ° (WNW)
        2/12  =   0 °  (E)       5/12 = 255 ° (N)      8/12 = 165 ° (W)
        9/12 = 135 ° (SW)      10/12 = 105 ° (SSW)   11/12 =  75 ° (S)
    """
    p   = angle_to_phase(angle_rad)      # continuous 0‑1
    idx = int(p * 12 + 0.5) % 12         # nearest 30 °
    return idx / 12.0                    # discrete phase in 12ths
    
# ───────── snap to 20 spokes (every 18 °) ────────────────────────────
def angle_to_phase_20(angle_rad: float) -> float:
    """
    Map angle to one of twenty 18‑degree steps.
    Indexing stays counter‑clockwise with 0/20 at 45 ° (SE), exactly
    like the 8‑ and 12‑step helpers:

        0/20  =  45 °  (SE)          5/20  =  -45 °  (E)
        1/20  =  27 °  (ESE)         6/20  =  -63 °  (ENE)
        2/20  =   9 °  (E‑by‑S)      7/20  =  -81 °  (NE)
        3/20  =  -9 °  (E)           8/20  = -99 °  (NNE)
        4/20  = -27 °  (E‑by‑N)      … and so on round the circle

    Return value is the discrete phase in 20ths of a turn (0‑1 range).
    """
    p   = angle_to_phase(angle_rad)      # continuous 0‑1
    idx = int(p * 20 + 0.5) % 20        # nearest 18 °
    return idx / 20.0
	
# ----------------------------------------------------------------------
# Per‑frame callback
# ----------------------------------------------------------------------

def whileOn(channel, sampleIndex, val, prev):
    # ───────── thresholds (screen‑fraction units) ─────────
    th_arm = op('distance_threshold_arm')[0].eval()
    th_leg = op('distance_threshold_leg')[0].eval()

    # ───────── screen size  (height = 1.0 after normalise) ─────────
    W = op('width')[0].eval()             # width in “height units”
    H = op('height')[0].eval()            # = 1.0 by definition
    aspect = W / H                       # same as W here

    # centre in wide‑coords so the circle stays round
    cx_wide = 0.5 * aspect               # e.g. 0.888 for 16:9
    cy      = 0.5

    # ───────── limb table ────────────────────────────────
    limbs = {
        'right_hand': {'coord': op('right_hand_xy'), 'ramp': op('Ramp_Hand_right'), 'th': th_arm},
        'left_hand':  {'coord': op('left_hand_xy'),  'ramp': op('Ramp_Hand_left'),  'th': th_arm},
        'right_foot': {'coord': op('right_foot_xy'), 'ramp': op('Ramp_foot_right'), 'th': th_leg},
        'left_foot':  {'coord': op('left_foot_xy'),  'ramp': op('Ramp_foot_left'),  'th': th_leg},
    }

    comp_target = op('comp15')            # TOP that receives the ramps

    for limb, cfg in limbs.items():
        xy   = cfg['coord']
        ramp = cfg['ramp']
        th   = cfg['th']

        # ----------- current position --------------------
        x_raw = xy[0].eval()              # 0‒1
        y     = xy[1].eval()              # 0‒1

        # stretch X so one screen‑unit = screen‑height
        x_wide = x_raw * aspect
        dx = x_wide - cx_wide
        dy = y - cy

        dist  = math.hypot(dx, dy)        # same units as th_*
        angle = math.atan2(dy, dx)
        ramp.par.phase = angle_to_phase_20(angle)

        # ----------- connection logic --------------------
        outside   = dist >= th            # TRUE when limb is beyond the ring
        connected = bool(ramp.outputs)    # ramp already patched?

        if outside and not connected:
            ramp.outputConnectors[0].connect(comp_target)
        elif (not outside) and connected:
            ramp.outputConnectors[0].disconnect()

        # ----------- debug (optional) --------------------
        # print(f"{limb}: dist={dist:.3f}  th={th:.3f}  outside={outside}")

    return


# ----------------------------------------------------------------------
# Unused callbacks ------------------------------------------------------
# ----------------------------------------------------------------------

def onOffToOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	return