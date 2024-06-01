from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Sélectionner une image')
    METHOD_CHOICES = [
        ('canny', 'Segmentation par Contour (Canny)'),
        ('sobel', 'Segmentation par Contour (Sobel)'),
        ('threshold_fixe', 'Seuillage Global (Fixe)'),
        ('threshold_adaptatif', 'Seuillage Adaptatif')
    ]
    method = forms.ChoiceField(choices=METHOD_CHOICES, label='Méthode de Segmentation')

