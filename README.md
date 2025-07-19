
# Image Processing Web App with Django

This project is a simple web application built with **Django** that allows users to **upload, process, and view images**. It provides an easy-to-use interface to apply various **image processing algorithms**, such as filtering and segmentation, directly through the browser.

## Technologies Used

- **Backend**: Python (Django)
- **Frontend**: HTML, CSS
- **Database**: SQLite
- **Image Processing**: Pillow or OpenCV
- **Optional**: Bootstrap for styling

## Features

-  Upload images from your device
-  View original and processed images
- **Filtering operations**:
  - Gaussian blur
  - Median filter
  - Edge detection (Sobel, Canny, etc.)
-  **Segmentation techniques**:
  - Thresholding (binary, adaptive)
  - K-means clustering
  - Active contour models (optional, if implemented)
-  Save the results after processing

## Project Structure

```
├── django_db/           # Django project configuration
├── traitement_img/      # App for image processing logic
├── db.sqlite3           # Local database
└── manage.py            # Django project manager
```

##  To run the project locally:

```bash
git clone https://github.com/khabbaoui/traitement_image.git
cd traitement_image
python manage.py migrate
python manage.py runserver
```

