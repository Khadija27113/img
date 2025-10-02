from ColorPaletteGeneration import ColorPaletteGeneration


if __name__ == "__main__":
    image_path = r"C:\Users\khadi\Documents\CPU\Image_Recolorization\assets\pexels-souvenirpixels-417074.jpg"
    palette_gen = ColorPaletteGeneration(image_path)
    palette_gen.fittingData()
    palette_gen.plotAndSaveColors()