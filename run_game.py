#!/usr/bin/env python3
"""Run the Space Lander game locally."""
import asyncio
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from main import main
asyncio.run(main())
