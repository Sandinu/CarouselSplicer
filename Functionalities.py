from PIL import Image
import os
from reportlab.pdfgen import canvas

def image_slice(path, output, generate_pdf):
    img = Image.open(path)
    file_name = os.path.splitext(os.path.basename(path))[0]

    width, height = img.size
    Slices = width //1080

    pdf_path = f"{output}/{file_name}.pdf"

    canvaS = canvas.Canvas(pdf_path, pagesize=(1080, height))

    if generate_pdf:
        for i in range(Slices):
            left = i*1080
            upper = 0
            right = min((i+1)*1080, width)
            lower = height

            slice_img = img.crop((left, upper, right, lower))
            slice_height = slice_img.size[1]
            slice_img.save(f"{output}/{file_name}_{i+1}.png")

            canvaS.drawImage(f"{output}/{file_name}_{i+1}.png", 0, 0, width=1080, height=slice_height)
            if i < Slices-1:
                canvaS.showPage()

        canvaS.save()
    else:
        for i in range(Slices):
            left = i * 1080
            upper = 0
            right = min((i + 1) * 1080, width)
            lower = height

            slice_img = img.crop((left, upper, right, lower))
            slice_img.save(f"{output}/{file_name}_{i + 1}.png")
