import os
import glob

script_dir = os.path.dirname(os.path.abspath(__file__))
benchmarks_dir = os.path.join(script_dir, "benchmarks")

bril_files = glob.glob(os.path.join(benchmarks_dir, "**", "*.bril"), recursive=True)

bril_dict = {}

for bril_file in bril_files:
    with open(bril_file, "r") as f:
        content = f.read()

    filename = os.path.splitext(os.path.basename(bril_file))[0]
    bril_dict[filename] = content
