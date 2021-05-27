from django.db import models
import matplotlib.pyplot as plt 
# Create your models here.
class ocr_model(models.Model):
    image = models.ImageField(upload_to='images/')
    # print(type(image))
    # plt.imshow(image)
    # plt.show()
   