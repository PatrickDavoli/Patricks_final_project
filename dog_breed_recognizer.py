#Code does everything besides loading the new image with the overlayed text

import jetson_inference
import jetson_utils
from jetson_utils import cudaFont

import argparse

parser = argparse.ArgumentParser()
filename = input("what is the name of the image you'd like to load? ")
parser.add_argument("--network", type=str, default="googlenet")
args = parser.parse_args()
font = cudaFont()

img = jetson_utils.loadImage(filename)
net = jetson_inference.imageNet(args.network)
dog_breed_idx = net.Classify(img)

if (dog_breed_idx in range(152, 278)):
    dog_breed = net.GetClassDesc(dog_breed_idx)
    dog_breed_label = net.GetClassLabel(dog_breed)
    print(f"imagenet: breed #{dog_breed} ({dog_breed_label})")
    font.OverlayText(img, text=f"{dog_breed_label}",
                 x=5, y=5 * (font.GetSize() + 5),
                 color=font.Black, background=font.White)
else:
    font.OverlayText(img, text=f"This wasn't recognized as an image of a dog, or the species isn't in the dataset!",
                 x=5, y=5 * (font.GetSize() + 5),
                 color=font.Black, background=font.White)
