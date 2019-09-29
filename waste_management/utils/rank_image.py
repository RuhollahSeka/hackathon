# Imports the Google Cloud client library
from google.cloud import vision

# We put a litter cap to 200g, so that based on the litter label, 100% equals to 200g of trash
LITTER_CAP = 200


def trash_to_gas(amount):
    # 2.87 metric tons CO2 equivalent/ton
    # of waste recycled instead of landfilled

    # conversion grams to TON
    tons = amount * 0.000001

    # conversion tons of co2 to kg of co2
    co2kg = 2.87 * tons * 1000

    return co2kg


# Get the weight of the waste depending on the percentage of recognized
# litter in the image

def getLabelsWaste(labels):
    print('Labels:')
    litterpercentage = 0
    for label in labels:
        print(label.description)
        if label.description.lower() == "litter":
            litterpercentage = label.score
    waste = litterpercentage * LITTER_CAP
    return waste


def getObjectsWaste(objects):
    waste = 0
    print('Waste detect:')
    for object_ in objects:
        if "waste" in object_.name.lower() or "plastic" in object_.name.lower() or "package" in object_.name.lower():
            waste += 32
            print("Found waste in the picture")
            print("Vertices: ")
            for vertex in object_.bounding_poly.normalized_vertices:
                print(' - ({}, {})'.format(vertex.x, vertex.y))
    return waste


def printObjects(objects):
    print('Number of objects found: {}'.format(len(objects)))
    print('List of objects:')
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))


def analyze_image(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    response = client.label_detection(image=image)
    labels = response.label_annotations

    printObjects(objects)

    labelswaste = getLabelsWaste(labels)

    objectswaste = getObjectsWaste(objects)

    wasteamount = labelswaste + objectswaste
    print('Weight of trash from objects: ' + str(objectswaste) + ' g')
    print('Weight of trash from labels: ' + str(labelswaste) + ' g')
    print('Total weight of trash: ' + str(wasteamount) + ' g')
    print('Greenhouse Gas saved: ' + str(trash_to_gas(wasteamount)) + ' kg of CO2')
    return wasteamount
#
#
# if analyze_image("image.jpg"):
#     print("The image most likely contains trash!!")
# else:
#     print("The image most likely doesn't contain trash")
