badge-photo-maker is a tool to automate creation of ID / employee badges.
Export can be made automaticly in bulk or manually seperatly.

There are many options like:
Monochrome
Face Detection
Defining cropped face desired resolution
Background removal with ability to define number of times it iterates that remove function

It uses rembg library under MIT license with u2net.onnx model to remove background, 
opencv-python under MIT license to make the photo in greyscale,
for face detection uses haarcascade_frontalface_default.xml,
and GUI is made using tkinter

Usage:
In upper left corner there is a menu. Click the option you desire (input images, or all images from folder). Then an image will appearn on the left side. In the right side of the main window are options. Select the ones that suit you and click "Submit" to see preview, or click "Save" to save the images.

Result:
<p style="display: flex;align-items: center;justify-content: center;">
  <img alt="example photo-1" src="https://github.com/GinaHanaMi/badge-photo-maker/blob/main/examples/StockSnap_DULMKZVVDC.jpg" width="100" />
  <img alt="example photo-2" src="https://github.com/GinaHanaMi/badge-photo-maker/blob/main/examples/StockSnap_FIP1AN4O4U.jpg" width="100" />
  <img alt="example photo-3" src="https://github.com/GinaHanaMi/badge-photo-maker/blob/main/examples/StockSnap_G4YYZSAXAT.jpg" width="100" />
  <img alt="example photo-4" src="https://github.com/GinaHanaMi/badge-photo-maker/blob/main/examples/StockSnap_H1DONX4WW2.jpg" width="100" />
  <img alt="example photo-5" src="https://github.com/GinaHanaMi/badge-photo-maker/blob/main/examples/StockSnap_LHZMZE0JL0.jpg" width="100" />
  <img alt="example photo-6" src="https://github.com/GinaHanaMi/badge-photo-maker/blob/main/examples/StockSnap_NCT0MAJ5LE.jpg" width="100" />
  <img alt="example photo-7" src="https://github.com/GinaHanaMi/badge-photo-maker/blob/main/examples/StockSnap_OLJZKBI4DD.jpg" width="100" />
  <img alt="example photo-8" src="https://github.com/GinaHanaMi/badge-photo-maker/blob/main/examples/StockSnap_QLQKAOHIUJ.jpg" width="100" />
  <img alt="example photo-9" src="https://github.com/GinaHanaMi/badge-photo-maker/blob/main/examples/StockSnap_QOA4RON0B0.jpg" width="100" />
</p>

GUI:
<p style="display: flex;align-items: center;justify-content: center;">
  <img alt="example photo-1" src="https://github.com/GinaHanaMi/badge-photo-maker/blob/main/examples/GUI.JPG" width="800" />
</p>

Thanks to https://stocksnap.io/ for photos to process that are on CC0 license.
