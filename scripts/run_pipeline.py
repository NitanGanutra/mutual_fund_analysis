"""
Bluestock Mutual Fund Analytics

Master Pipeline Script

Purpose:
Run all project scripts in sequence.

Author: Nitan Sharma
"""

import subprocess
import os
import sys

# Project root = parent folder of scripts/
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

scripts = [
    "data_ingestion.py",
    "live_nav_fetch.py",
    os.path.join("scripts", "day2_cleaning.py"),
    os.path.join("scripts", "load_to_sqlite.py"),
    os.path.join("scripts", "recommender.py")
]

for script in scripts:
    script_path = os.path.join(project_root, script)

    if os.path.exists(script_path):
        print(f"\nRunning {script}...")
        subprocess.run([sys.executable, script_path])
    else:
        print(f"Skipped: {script} (File not found)")

print("\nPipeline Completed Successfully!")