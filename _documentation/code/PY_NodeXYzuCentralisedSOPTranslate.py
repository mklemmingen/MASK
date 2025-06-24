# me - this DAT
# scriptOp - the OP which is cooking

# press 'Setup Parameters' in the OP to call this function to re-create the parameters.
def onSetupParameters(scriptOp):
	page = scriptOp.appendCustomPage('Custom')
	p = page.appendFloat('Valuea', label='Value A')
	p = page.appendFloat('Valueb', label='Value B')
	return

# called whenever custom pulse parameter is pushed
def onPulse(par):
	return

def onCook(scriptOp):
	rechte_hand = op('rechteHand') 

	# Get resolution reference from a TOP about the resolution of the output beamer
	res = op('constant1')  
	width = res['res1'][0]
	height = res['res2'][0] 

	# Get normalized x/y 
	x_norm = rechte_hand['x'][0]
	y_norm = rechte_hand['y'][0]
	
	# Convert to correct fraction offset
	x = x_norm * width/height - 1
	y = y_frac = 0.5 - y_norm

	# Output result
	scriptOp.clear()
	scriptOp.appendChan('x')[0] = x
	scriptOp.appendChan('y')[0] = y

	return
