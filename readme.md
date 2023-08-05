# Dog Breed Recognizer

 My project tells the user what the breed of a dog in an image is. 

![Image of what the ouput image with the breed of the dog on it looks like](https://i.imgur.com/5QbZLmw.png)

## The Algorithm

First, my code imports all the required libraries and functions, which are jetson_inference, jetson_utils, argparse, (the rest are from jetson_utils) videoOutput, cudaFont, and adaptFontSize. After that, when you run the code, the first thing it does is ask the user (through the input command) what the name of the file (image) they want to pass through the code is. After that, it defines all the variables it needs, which are as follows: img, output, net, and font. img is the file that you inputted earlier, output is used to get an output image, net is set to the network you want to use, and font is the font that gets overlayed onto the image in a later step, with the size of that font being adjusted for the width of the image. AFterwards, the model classifies the image, with the dog_breed_idx given the value of the what the image is classified as. Then, to make sure that the image provided is a dog, an if statement is used to check whether dog_breed_idx is between 152 and 277, inclusive. If it isn't, the text "This wasn't recognized as a dog!" will be overlayed over the image. Otherwise, dog_breed_idx is a numerical value, denoting where in the list of all the possible classifications the current classification is, so to change it to what the breed of the dog is in words the getClassDesc command is run on dog_breed_idx, with the variable dog_breed being set to the string resulting from that. Afterwards, dog_breed is overlayed onto the image to let the user know what the breed of the dog is. Lastly, the img is rendered to the output so that an image will be outputted, letting the user see the results of the Dog Breed Recognizer.

## Running this project

1. Download Visual Studio (VS) code onto your device
2. Using the command palete, connect to your Jetson Nano with SSH
3. Don't forget to make sure that python3 and the Jetson Inference library are installed
4. Copy the dog_breed_recognizer.py code from this github into a new file in VS code, preferably named dog_breed_recognizer.py
5. In VS code, press ctrl+shift+` to make a new terminal
6. Import the image of the dog you want to figure out the breed of into VS code using the command **wget (link to the image)** in the terminal (in VS code), or drag and drop the file into VS code if you downloaded it, just make sure that your image is a jpg
7. Use the command (don't type any of the text in the parentheses, that is simply there to help explain the command) **python3 dog_breed_recognizer.py (or whatever you named your file with the dog_breed_recognizer code in it) --network=resnet-18 (this part is optional as the network is defaulted to googlenet, but you can set it to the one of your choosing with that part) output.jpg (the output can be called whatever you want, as long as it ends in .jpg)** in the terminal
8. When the code is done running, you should see output.jpg (or whatever you named your output image) how up on the left side, in the Explorer (ctrl+shift+e to get in the explorer if you aren't already in it). Click on that, and you should see an image like the one above before the algorithm section, with the dog breed or "This wasn't recognized as a dog!" in the upper left corner

## View a video explanation here: [(video link)](https://youtu.be/lCsjooA60fg)
