import os

model="CSWM"
encoders=["small", "medium", "large"]

cmap="Blues"
#cmap="Sets"

for run in range(1,4):
    for encoder in encoders:
        if encoder is "small":
            bs = 1024
            time = 24
        elif encoder is "medium":
            bs = 512
            time = 48
        else:
            bs = 256
            time = 72
        for i in [3,5]:
             os.system(f"sbatch --gres=gpu:1 --mem=16G --account=rrg-bengioy-ad --time={time}:0:0 run.sh  {i} {model} {encoder} {bs} {cmap} {run}")