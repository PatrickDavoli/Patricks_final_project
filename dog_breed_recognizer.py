import jetson_inference
import jetson_utils
import argparse
from jetson_utils import videoOutput, cudaFont, adaptFontSize


parser = argparse.ArgumentParser()
filename = input("what is the name of the image you'd like to load? ")
parser.add_argument("--network", type=str, default="googlenet")
parser.add_argument("output", type=str, default="", nargs='?')
args = parser.parse_args()


img = jetson_utils.loadImage(filename)
output = videoOutput(args.output)
net = jetson_inference.imageNet(args.network)
font = cudaFont(size=adaptFontSize(img.width))
dog_breed_idx, confidence = net.Classify(img)


if (dog_breed_idx in range(152, 278)):
    dog_breed = net.GetClassDesc(dog_breed_idx)
    font.OverlayText(img, text=f"{dog_breed}",  
                 width = 5, height = 5,
                 x=5, y=0,
                 color=font.Black, background=font.White)
else:
    font.OverlayText(img, text=f"This wasn't recognized as a dog!",
                 width = 5, height = 5,
                 x=5, y=0,
                 color=font.Black, background=font.White)

output.Render(img)