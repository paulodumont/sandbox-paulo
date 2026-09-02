# Product Sets & Bundles

Working prototype: open `index.html` in any browser (self-contained, images embedded).
Source photos in `img/`.

## Selling model

- A **set** is a parent product that references its pieces; each piece remains a sellable SKU.
- The set page opens with **all pieces pre-selected**; the buyer can deselect and keep a single piece.
- An optional **set advantage** (percentage) applies only when all pieces are selected.
- Stock is tracked per piece; the set is offered while every piece is in stock.

## Data model

```json
{
  "sku": "SET-AME-001",
  "type": "set",
  "name": "Amethyst Parure",
  "currency": "USD",
  "setAdvantagePct": 10,
  "images": { "still": "img/set-still.jpg", "worn": "img/set-worn.jpg" },
  "pieces": [
    { "sku": "EAR-AME-001", "name": "Drop Earrings",    "price": 1900 },
    { "sku": "PEN-AME-001", "name": "Pendant Necklace", "price": 1450 },
    { "sku": "RIN-AME-001", "name": "Cocktail Ring",    "price": 1650 }
  ]
}
```

## Catalogue rules

- The set card carries a `PARURE · N PIECES` badge and the complete-set price.
- Each piece card carries a `FROM THE PARURE` badge linking back to the set page.
- Every set is photographed twice: one still, one worn.

All prices, SKUs and the advantage percentage above are sample values.
