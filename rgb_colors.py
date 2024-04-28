from PIL import Image, ImageDraw



def color_converter(image):
    # Convert the image to RGB mode (if it's not already in RGB)
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Get the RGB values as a list of tuples
    rgb_values = list(image.getdata())

    # If you want to get the width and height of the image
    width, height = image.size

    # Close the image (not necessary, but good practice)
    image.close()

    # Now, rgb_values contains a list of (R, G, B) tuples for each pixel in the image
    # You can access the RGB values like this:

    # Collect all the RGB values
    all_rgb_values = []

    for pixel in rgb_values:
        r, g, b = pixel
        all_rgb_values.append((r, g, b))

    
    # Calculate the average RGB values
    average_r = sum([rgb[0] for rgb in all_rgb_values]) // len(all_rgb_values)
    average_g = sum([rgb[1] for rgb in all_rgb_values]) // len(all_rgb_values)
    average_b = sum([rgb[2] for rgb in all_rgb_values]) // len(all_rgb_values)

    # Print the average RGB values
    print(f"Average RGB value: ({average_r}, {average_g}, {average_b})\n")

    # Create a new image with the same size as the original image
    new_image = Image.new("RGB", (width, height), (average_r, average_g, average_b))

    # Save or display the new image
    #new_image.show()
    # new_image.save("output_image.jpg")  # Uncomment this line to save the image to a file
    
    
    # Open the image

for i in range(1,13):
    num = 'H' + str(i)
    print(f"The RGB value for {num} is")

    image = Image.open(f"Color_{num}.jpg")  # Replace with your image file path
    
    color_converter(image)
