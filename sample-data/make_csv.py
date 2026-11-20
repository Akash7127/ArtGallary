"""Build Shopify product import CSVs for the ArtGallary sample artworks.

All artists, titles and descriptions are fictional sample content.
Run:  python sample-data/make_csv.py
Writes sample-data/sample-artworks.csv (with artwork detail fields) and
sample-data/sample-artworks-basic.csv (without them).
"""
import csv
from pathlib import Path

IMAGE_BASE = 'https://artgallary-store.myshopify.com/cdn/shop/t/3/assets/'
HERE = Path(__file__).parent

PRINTS = [('Print A2 (42 x 59 cm)', 6500), ('Print A3 (30 x 42 cm)', 3800)]

ARTWORKS = [
    # handle, title, artist, medium, size, year, price, edition, framing, prints?, sold?, tags, description
    ('monsoon-field', 'Monsoon Field', 'Ira Vadera', 'Acrylic on canvas', '120 x 150 cm', '2026', 185000, '', 'Unframed, stretched and ready to hang', False, False,
     'Abstract, Colour field, Red, Large',
     'Three soft bands of earth, rust and saffron, painted in thin layers over many weeks. Vadera thinks of it as the moment before the first rain, when the light turns heavy and warm.'),
    ('dusk-over-kutch', 'Dusk over Kutch', 'Kabir Solanki', 'Oil on canvas', '150 x 120 cm', '2025', 240000, '', 'Framed in natural teak', True, False,
     'Landscape, Desert, Orange, Large',
     'Rolling dunes in deepening browns under a single red sun. Solanki reduces the landscape to its quietest shapes, leaving room for the heat and stillness of evening.'),
    ('sun-rings', 'Sun Rings', 'Anaya Rathod', 'Gouache on paper', '60 x 60 cm', '2026', 68000, '', 'Framed in white oak with museum glass', False, False,
     'Abstract, Circles, Yellow, Works on paper',
     'Uneven rings of ochre, vermilion and slate, each laid down by hand with a broad brush. The slight wobble of every ring is deliberate: a record of breath and movement.'),
    ('kolam-grid', 'Kolam Grid', 'Rohan Ves', 'Acrylic on board', '80 x 100 cm', '2024', 92000, '', 'Unframed, ready to hang', False, False,
     'Geometric, Pattern, Blue, Medium',
     'A grid of split squares inspired by threshold drawings made each morning outside homes. Ves lets chance decide each diagonal, so no two rows repeat.'),
    ('loom-song', 'Loom Song', 'Meher Joshi', 'Hand-woven cotton and silk', '90 x 112 cm', '2025', 135000, '', 'Mounted on a linen-covered panel', False, False,
     'Textile, Stripes, Multicolour, Medium',
     'Woven on a hand loom over three months, with warp and weft dyed in madder, turmeric and indigo. Up close it reads as pure colour; from across the room, as light through a window.'),
    ('pollen-drift', 'Pollen Drift', 'Tara Bhatt', 'Ink on paper', '100 x 80 cm', '2026', 54000, '', 'Unframed, shipped flat', True, False,
     'Abstract, Dots, Green, Works on paper',
     'Thousands of small ink dots gathered into slow waves of teal, gold and coral. Bhatt works without sketches, letting each layer suggest where the next should drift.'),
    ('tide-lines', 'Tide Lines', 'Ira Vadera', 'Pen and ink on paper', '48 x 60 cm', '2025', 38000, '', 'Framed in black ash', False, True,
     'Drawing, Lines, Black and white, Small, Works on paper',
     'Seventy hand-drawn lines rise and fall like water seen from a height. A meditative drawing that took a single long sitting to complete.'),
    ('three-doorways', 'Three Doorways', 'Kabir Solanki', 'Acrylic on canvas', '90 x 112 cm', '2026', 120000, '', 'Unframed, stretched and ready to hang', True, False,
     'Architecture, Arches, Teal, Medium',
     'Three arched forms in terracotta, teal and turmeric, each pierced by a small round window. A study of old courtyard houses, simplified to colour and shape.'),
    ('garden-forms', 'Garden Forms', 'Anaya Rathod', 'Mixed media on paper', '70 x 70 cm', '2025', 72000, '', 'Framed in white oak with museum glass', False, False,
     'Abstract, Organic, Earth tones, Works on paper',
     'Overlapping leaf-like shapes cut, painted and layered by hand. Made from studies of the same small garden across a whole year.'),
    ('night-at-rann', 'Night at Rann', 'Rohan Ves', 'Oil on linen', '125 x 100 cm', '2024', 165000, '', 'Framed in dark walnut', False, False,
     'Landscape, Night, Blue, Large',
     'A pale moon over the salt flats, with the sky crowded by stars. Ves painted it from memory after a winter night spent out on the white desert.'),
    ('seed-spiral', 'Seed Spiral', 'Meher Joshi', 'Screen print on cotton rag paper', '50 x 50 cm', '2026', 18000, 'Edition of 25, signed and numbered', 'Unframed, shipped flat', False, False,
     'Print, Spiral, Multicolour, Small',
     'A spiral of seed-like marks that grow as they turn outward, printed in four colours by hand. Signed and numbered by the artist.'),
    ('teal-evening', 'Teal Evening', 'Tara Bhatt', 'Acrylic on canvas', '120 x 150 cm', '2026', 210000, '', 'Unframed, stretched and ready to hang', False, False,
     'Abstract, Colour field, Teal, Large',
     'Cool teal and sand give way to a warm band of rust at the base. Bhatt calls it a painting of the hour after sunset, when colours seem to glow from within.'),
]

BASE_COLUMNS = [
    'Handle', 'Title', 'Body (HTML)', 'Vendor', 'Product Category', 'Type', 'Tags', 'Published',
    'Option1 Name', 'Option1 Value', 'Variant SKU', 'Variant Grams', 'Variant Inventory Tracker',
    'Variant Inventory Qty', 'Variant Inventory Policy', 'Variant Fulfillment Service', 'Variant Price',
    'Variant Compare At Price', 'Variant Requires Shipping', 'Variant Taxable', 'Image Src',
    'Image Position', 'Image Alt Text', 'Gift Card', 'SEO Title', 'SEO Description',
    'Variant Weight Unit', 'Status',
]
META_COLUMNS = {
    'year': 'Year (product.metafields.custom.year)',
    'medium': 'Medium (product.metafields.custom.medium)',
    'dimensions': 'Dimensions (product.metafields.custom.dimensions)',
    'edition': 'Edition (product.metafields.custom.edition)',
    'framing': 'Framing (product.metafields.custom.framing)',
}


def rows(with_meta):
    out = []
    for n, (handle, title, artist, medium, size, year, price, edition, framing, prints, sold, tags, desc) in enumerate(ARTWORKS, 1):
        image = f'{IMAGE_BASE}ag-sample-{n:02d}.jpg'
        alt = f'{title} by {artist}, {medium.lower()}'
        variants = [('Original', price, 0 if sold else 1, 6000)]
        if prints:
            variants += [(name, p, 25, 600) for name, p in PRINTS]
        for i, (option, vprice, qty, grams) in enumerate(variants):
            first = i == 0
            row = {c: '' for c in BASE_COLUMNS}
            row.update({
                'Handle': handle,
                'Option1 Value': option,
                'Variant SKU': f'AG-{n:02d}-{"ORIG" if first else ("A2" if "A2" in option else "A3")}',
                'Variant Grams': grams,
                'Variant Inventory Tracker': 'shopify',
                'Variant Inventory Qty': qty,
                'Variant Inventory Policy': 'deny',
                'Variant Fulfillment Service': 'manual',
                'Variant Price': f'{vprice:.2f}',
                'Variant Requires Shipping': 'TRUE',
                'Variant Taxable': 'TRUE',
                'Variant Weight Unit': 'kg',
            })
            if first:
                row.update({
                    'Title': title,
                    'Body (HTML)': f'<p>{desc}</p><p><em>Sample artwork by a fictional artist, for testing the store.</em></p>',
                    'Vendor': artist,
                    'Type': medium,
                    'Tags': f'{tags}, Sample',
                    'Published': 'TRUE',
                    'Option1 Name': 'Format',
                    'Image Src': image,
                    'Image Position': 1,
                    'Image Alt Text': alt,
                    'Gift Card': 'FALSE',
                    'SEO Title': f'{title} by {artist}',
                    'SEO Description': desc[:155],
                    'Status': 'active',
                })
                if with_meta:
                    row.update({
                        META_COLUMNS['year']: year,
                        META_COLUMNS['medium']: medium,
                        META_COLUMNS['dimensions']: size,
                        META_COLUMNS['edition']: edition or ('Original, one of a kind' if not prints else 'Original; open-edition prints available'),
                        META_COLUMNS['framing']: framing,
                    })
            elif with_meta:
                row.update({c: '' for c in META_COLUMNS.values()})
            out.append(row)
    return out


def write(path, with_meta):
    columns = BASE_COLUMNS + (list(META_COLUMNS.values()) if with_meta else [])
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows(with_meta))
    print('wrote', path.name, len(rows(with_meta)), 'rows')


write(HERE / 'sample-artworks.csv', True)
write(HERE / 'sample-artworks-basic.csv', False)
