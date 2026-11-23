# Sample artists and exhibitions

All people and shows here are **fictional sample content**, made to match the 12
sample artworks. Artist **Name** must match the product **Vendor** exactly, so each
profile can find its works.

Images: every artwork image is already in Shopify (Content → Files) from the product
import. Pick them with "Select existing" in the file picker; the file names start with
`ag-sample-`.

---

## Step 1 — Definitions (Settings → Custom data → Metaobjects → Add definition)

### Artist — type `artist`, turn on **Web pages / Storefronts**

| Field | Key | Type |
|---|---|---|
| Name | `name` | Single line text (set as display name) |
| Portrait | `portrait` | File → Image |
| Practice | `practice` | Single line text |
| Location | `location` | Single line text |
| Born | `born` | Single line text |
| Bio | `bio` | Multi-line text |
| Artworks | `artworks` | Product → List of products |

### Exhibition — type `exhibition`, turn on **Web pages / Storefronts**

| Field | Key | Type |
|---|---|---|
| Title | `title` | Single line text (set as display name) |
| Subtitle | `subtitle` | Single line text |
| Artist names | `artist_names` | Single line text |
| Artists | `artists` | Metaobject → Artist → List |
| Start date | `start_date` | Date |
| End date | `end_date` | Date |
| Location | `location` | Single line text |
| Opening | `opening` | Single line text |
| Cover | `cover` | File → Image |
| Summary | `summary` | Multi-line text |
| Description | `description` | Rich text |
| Installation views | `installation_views` | File → Image → List |
| Artworks | `artworks` | Product → List of products |

---

## Step 2 — Artists (Content → Metaobjects → Artist → Add entry)

### Ira Vadera
- Portrait: `ag-sample-01`
- Practice: Painting and drawing
- Location: Ahmedabad
- Born: 1986, Vadodara
- Bio: Ira Vadera paints slow, layered fields of colour that hold the feeling of weather and season. Trained in printmaking, she still builds each canvas in thin washes, one over another, until the surface seems to breathe. Her ink drawings follow the same rhythm in line instead of colour.
- Artworks: Monsoon Field, Tide Lines

### Kabir Solanki
- Portrait: `ag-sample-08`
- Practice: Painting
- Location: Bhuj
- Born: 1979, Mandvi
- Bio: Kabir Solanki grew up between the desert and the sea, and both appear in his work as simple, warm shapes. His paintings of dunes, doorways and courtyards strip places down to colour and light, leaving space for memory to fill in the rest.
- Artworks: Dusk over Kutch, Three Doorways

### Anaya Rathod
- Portrait: `ag-sample-03`
- Practice: Works on paper
- Location: Pune
- Born: 1991, Nashik
- Bio: Anaya Rathod works almost entirely on paper, with gouache, cut paper and collage. Her circles and garden forms come from daily studies of plants and light, repeated until they become something closer to pattern than picture.
- Artworks: Sun Rings, Garden Forms

### Rohan Ves
- Portrait: `ag-sample-10`
- Practice: Painting
- Location: Surat
- Born: 1983, Navsari
- Bio: Rohan Ves moves between strict geometry and open landscape. His grid paintings borrow from threshold drawings and textile patterns; his night paintings come from long trips to the salt flats, painted from memory back in the studio.
- Artworks: Kolam Grid, Night at Rann

### Meher Joshi
- Portrait: `ag-sample-05`
- Practice: Textile and print
- Location: Jaipur
- Born: 1988, Udaipur
- Bio: Meher Joshi weaves on a hand loom and prints by hand, using natural dyes wherever she can. Her pieces treat colour as something you can build thread by thread, and her limited-edition prints carry the same patience onto paper.
- Artworks: Loom Song, Seed Spiral

### Tara Bhatt
- Portrait: `ag-sample-12`
- Practice: Painting and ink
- Location: Mumbai
- Born: 1990, Rajkot
- Bio: Tara Bhatt works intuitively, without sketches, letting each layer suggest the next. Her large canvases explore the colours of dusk; her ink works gather thousands of small marks into slow, drifting fields.
- Artworks: Pollen Drift, Teal Evening

---

## Step 3 — Exhibitions (Content → Metaobjects → Exhibition → Add entry)

### Earth and Ember  *(now showing)*
- Subtitle: A group exhibition with
- Artist names: Ira Vadera, Kabir Solanki and Tara Bhatt
- Artists: Ira Vadera, Kabir Solanki, Tara Bhatt
- Start date: 2026-11-06 · End date: 2027-01-10
- Location: Main gallery
- Opening: Friday 6 November, 6–9 pm
- Cover: `ag-sample-02`
- Summary: Three painters, one warm palette. Earth and Ember brings together new canvases and drawings that look at heat, dusk and the colours of dry land.
- Description: The works in this exhibition were made over the past year in three very different places: a studio in Ahmedabad, a courtyard in Bhuj and a small flat in Mumbai. What joins them is colour. Rust, ochre, saffron and deep brown run through every room, along with the cooler teal of evening. Together they make a quiet, glowing show about land and light.
- Installation views: `ag-sample-01`, `ag-sample-12`
- Artworks: Monsoon Field, Dusk over Kutch, Teal Evening, Tide Lines

### Salt and Stars  *(coming soon)*
- Subtitle: A solo exhibition by
- Artist names: Rohan Ves
- Artists: Rohan Ves
- Start date: 2026-12-05 · End date: 2027-01-31
- Location: Online viewing room
- Cover: `ag-sample-10`
- Summary: New paintings from the white desert, where the ground is salt and the sky never seems to end.
- Description: Rohan Ves has returned to the salt flats every winter for a decade. This online exhibition shows his newest night paintings alongside the strict grid works that he makes in between trips, two sides of the same search for order and space.
- Artworks: Night at Rann, Kolam Grid

### Thread and Ground  *(coming soon)*
- Subtitle: Textile, paper and print by
- Artist names: Meher Joshi and Anaya Rathod
- Artists: Meher Joshi, Anaya Rathod
- Start date: 2027-01-22 · End date: 2027-03-08
- Location: Project room
- Opening: Friday 22 January, 6–8 pm
- Cover: `ag-sample-05`
- Summary: Two artists who build images slowly, by hand: one with thread, the other with cut and painted paper.
- Description: Thread and Ground pairs Meher Joshi's hand-woven textiles and prints with Anaya Rathod's gouaches and collages. Both work through repetition and patience, and both draw on plants, gardens and natural colour.
- Artworks: Loom Song, Seed Spiral, Sun Rings, Garden Forms

### Paper Weather  *(past)*
- Subtitle: Works on paper by
- Artist names: Tara Bhatt, Anaya Rathod and Ira Vadera
- Artists: Tara Bhatt, Anaya Rathod, Ira Vadera
- Start date: 2026-09-04 · End date: 2026-10-18
- Location: Main gallery
- Cover: `ag-sample-06`
- Summary: Ink, gouache and pen on paper: small, intimate works that respond to rain, wind and changing light.
- Description: Paper Weather brought together small works on paper by Tara Bhatt, Anaya Rathod and Ira Vadera. Drifting ink dots, hand-painted rings and long pen lines hung side by side, three very different ways of recording rain, wind and the changing light of a single season.
- Artworks: Pollen Drift, Sun Rings, Tide Lines

### First Light  *(past)*
- Subtitle: A solo exhibition by
- Artist names: Kabir Solanki
- Artists: Kabir Solanki
- Start date: 2025-02-10 · End date: 2025-03-30
- Location: Main gallery
- Cover: `ag-sample-08`
- Summary: Kabir Solanki's first solo show with the gallery: doorways, courtyards and the early-morning light of Kutch.
- Description: First Light was Kabir Solanki's first solo exhibition with the gallery. The paintings came from early-morning walks through the old towns of Kutch, where doorways, arches and courtyards glow before the heat of the day. Each work strips a familiar place down to a few warm shapes and a single quiet colour.
- Artworks: Three Doorways, Dusk over Kutch
