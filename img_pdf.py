import pdf2image
from PIL import Image
img_list = ['Aclonica.png','Amatic sc.png','Arial.png','Calibri.png','Courier.png','Helvetica neue.png','Jua.png','Lobster.png','pattaya.png','Times New Roman.png']
list1 = ['Aclonica','Amatic sc','Arial','Calibri','Courier','Helvetica neue','Jua','Lobster','pattaya','Times New Roman']
i = 0
while i < len(img_list):
    image = Image.open(r'/home/jija/Desktop/files/OCR imgtotxt/images/'+img_list[i])
    img = image.convert('RGB')
    img.save(r'/home/jija/Desktop/files/OCR imgtotxt/pdf_folder/'+list1[i]+'.pdf')
    i+=1

def image_conversion(inpath,image_path):
  print("converting to image")
  OUTPUT_FOLDER = None
  FIRST_PAGE = None
  LAST_PAGE = None
  FORMAT = 'jpg'
  USERPWD = None
  USE_CROPBOX = False
  STRICT = False

  pil_images = pdf2image.convert_from_path(inpath,
                                          output_folder = OUTPUT_FOLDER,
                                          first_page = FIRST_PAGE,
                                          last_page = LAST_PAGE,
                                          fmt = FORMAT,
                                          userpw = USERPWD,
                                          use_cropbox= USE_CROPBOX,
                                          strict = STRICT )
  for image in pil_images :
    image.save(image_path+"image_converted.jpg")
inpath = ("/home/jija/Desktop/files/OCR imgtotxt/pdf_folder/Arial.pdf")
image_path = ("/home/jija/Desktop/files/OCR imgtotxt/pdf2image/")
image_conversion(inpath , image_path)