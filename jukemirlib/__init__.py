from .constants import *
from .setup_models import *
from .lib import *

# Ensure DEVICE is properly initialized on import
import torch
if DEVICE == "cuda" and torch.cuda.is_available():
    torch.cuda.init()
