import os
import sys

# Inject vendored directory into system path.
v_path = os.path.sep.join([os.path.dirname(os.path.realpath(__file__)), 'vendor'])
sys.path.append(v_path)
