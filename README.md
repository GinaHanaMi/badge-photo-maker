badge-photo-maker is a tool to automate creation of ID / employee badges in bulk without human intervention

It uses rembg library under MIT license with u2net.onnx model to remove background, opencv-python under MIT license to make the photo in greyscale, and for face detection using haarcascade_frontalface_default.xml.
There is no GUI, usage below.

Usage:
Place images into inputImg folder, run the main.py file and wait for images to appear in outputimg folder.

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

Thanks to https://stocksnap.io/ for photos to process. These are CC0 license.

I am very sorry if I missed someone, or something. This is actually my first repo, first commit, and first introduction to bigger world of programming than previously as a self-taught programmer.
Opinions, advices, commits are welcome here.
