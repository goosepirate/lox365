from com.sun.star.awt import Size

def IMAGE(doc, out_cell, url):
    drawpages = doc.DrawPages[int(out_cell.RangeAddress.Sheet)]
    existing_images = []

    def get_existing_images_at_position():
        for item in drawpages:
            if out_cell.Position != item.Position: continue
            existing_images.append(item)
    def remove_existing_images_at_position():
        [item.dispose() for item in existing_images]

    get_existing_images_at_position()

    # Parse URL.
    if url == '':
        remove_existing_images_at_position()
        return ''
    elif (
        not url.startswith('file://')
        and not url.startswith('http://')
        and not url.startswith('https://')
    ):  # Assume relative file path.
        current_dir = doc.URL.split('/')[:-1]
        url = '/'.join(current_dir) + '/' + url

    image = doc.createInstance('com.sun.star.drawing.GraphicObjectShape')
    image.Position = out_cell.Position
    image.GraphicURL = url
    image.Name = f'Generated image'
    try:
        drawpages.add(image)
    except:
        image.dispose()
        return ''
    size = Size()
    multiplier = 2540 * 15 / 1440
    size.Width, size.Height = (
        image.Graphic.Size.Width  * multiplier,
        image.Graphic.Size.Height * multiplier,
    )
    image.setSize(size)
    remove_existing_images_at_position()
    return ''
