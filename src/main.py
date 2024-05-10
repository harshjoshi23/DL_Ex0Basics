import matplotlib.pyplot as plt
from pattern import Checker, Circle, Spectrum
# from src.pattern import Checker, Circle, Spectrum

from generator import ImageGenerator
# from src.generator import ImageGenerator

def main():
    # Demonstrate the pattern generation
    checker = Checker(250, 25)
    checker.draw()
    checker.show()

    circle = Circle(200, 50, (100, 100))
    circle.draw()
    circle.show()

    spectrum = Spectrum(256)
    spectrum.draw()
    spectrum.show()

    # Assuming the ImageGenerator is correctly implemented and ready to use
    # Create an instance of the ImageGenerator
    generator = ImageGenerator(
        file_path='data/exercise_data',
        label_path='data/Labels.json',
        batch_size=10,
        image_size=[100, 100, 1],  # Example dimensions, adjust as needed
        rotation=True,
        mirroring=True,
        shuffle=True
    )
    
    # Generate and display one batch of images
    images, labels = generator.next()
    show_images(images, labels)

def show_images(images, labels):
    fig, axes = plt.subplots(1, len(images), figsize=(20, 4))
    for img, label, ax in zip(images, labels, axes):
        ax.imshow(img.squeeze(), cmap='gray')  # Adjust viewing options as necessary
        ax.title.set_text(f'Label: {label}')
    plt.show()

if __name__ == "__main__":
    main()
