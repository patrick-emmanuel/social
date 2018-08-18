

# Delete all the previously generated images before creating a new one.
def recreate_image(image, image_file):
    image.delete_all_created_images()
    image.delete(False)
    image = image_file
    image.save()
    return image
