#!/usr/bin/env python3
"""Build the site catalog from the in-repo raw sources.

Reads:   data/raw/cookware.raw.json, data/raw/radiators.raw.json   (copies of the
         pdf-extractor output — safe to hand-edit; the originals are never touched)
Writes:  data/cookware.json, data/radiators.json
Images:  already live under public/images/products/. If the pdf-extractor drive is
         mounted (IMG_SRC below), any newly-referenced webp is copied in; otherwise
         image copying is skipped silently.

Run:     python3 scripts/build_catalog.py   (from the pan_web repo root)

------------------------------------------------------------------------------------
EDIT HERE to fix cookware grouping. The catalog's back section (pages 21–28) groups by
product type/material rather than by branded collection, so those "series" values are
not real collections. We give them collection=None and a SPECIALTY label, and expose
the real browse axes: `collection` (sidebar) and `typeGroup` (filter chips).
"""
import json, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
DATA = ROOT / "data"
PUB = ROOT / "public" / "images" / "products"
IMG_SRC = {  # source webp dirs (optional — only used to copy not-yet-present images)
    "cookware": Path("/mnt/c/Users/kaira/workspace/pdf-extractor/output1_new"),
    "radiators": Path("/mnt/c/Users/kaira/workspace/pdf-extractor/output2"),
}

# --- cookware grouping config (edit freely) ----------------------------------------
# "Series" values that are really type/catch-all sections, not branded collections.
# Their products get collection = SPECIALTY_LABEL and are browsed via the Type axis.
TYPE_ONLY_SERIES = {
    "Wok", "Grill", "Multifunctional Grill", "Roaster",
    "Double Fry Pan", "Multi-functional",
}
SPECIALTY_LABEL = "Specialty & Grills"

# Raw product type -> (display name, type-filter bucket). Anything unmapped falls back
# to a title-cased display name and the "Other" bucket.
TYPE_MAP = {
    "FRY PAN": ("Fry Pan", "Fry Pan"),
    "DEEP FRY PAN": ("Deep Fry Pan", "Fry Pan"),
    "DOUBLE FRY PAN": ("Double Fry Pan", "Fry Pan"),
    "FAT-AWAY PAN": ("Fat-Away Pan", "Fry Pan"),
    "SAUCE PAN": ("Sauce Pan", "Sauce Pan"),
    "CASSEROLE": ("Casserole", "Casserole"),
    "SHALLOW CASSEROLE": ("Shallow Casserole", "Casserole"),
    "WOK": ("Wok", "Wok"),
    "GRILL PAN": ("Grill Pan", "Grill"),
    "GRILL TRAY": ("Grill Tray", "Grill"),
    "HALLOW BBQ GRILL TRAY": ("Hollow BBQ Grill Tray", "Grill"),
    "BBQ GRILL": ("BBQ Grill", "Grill"),
    "3 IN 1 GRILL PAN": ("3-in-1 Grill Pan", "Grill"),
    "4 IN 1 GRILL PAN": ("4-in-1 Grill Pan", "Grill"),
    "5 IN 1 GRILL PAN": ("5-in-1 Grill Pan", "Grill"),
    "SQUARE ROASTER": ("Square Roaster", "Roaster"),
    "ROASTER": ("Roaster", "Roaster"),
    "OVAL ROASTER": ("Oval Roaster", "Roaster"),
    "P-ROASTER": ("P-Roaster", "Roaster"),
    "EGG PAN": ("Egg Pan", "Egg & Crepe"),
    "CREPE PAN": ("Crepe Pan", "Egg & Crepe"),
    "CREP PAN": ("Crepe Pan", "Egg & Crepe"),
    "OVAL FISH PAN": ("Oval Fish Pan", "Specialty"),
}
# -----------------------------------------------------------------------------------


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").strip().lower()).strip("-")


def title(s):
    return " ".join(w.capitalize() for w in (s or "").split())


def uniq_id(base, seen):
    base = base or "item"
    cand, n = base, 2
    while cand in seen:
        cand, n = f"{base}-{n}", n + 1
    seen.add(cand)
    return cand


copied = {"cookware": set(), "radiators": set()}


def copy_img(thumb_rel, kind):
    name = Path(thumb_rel).name
    url_thumb = f"/images/products/{kind}/thumb/{name}"
    url_full = f"/images/products/{kind}/full/{name}"
    src_root = IMG_SRC[kind]
    for sub in ("thumb", "full"):
        dst = PUB / kind / sub / name
        if dst.exists():
            continue
        src = src_root / "effects" / "web" / sub / name
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
    copied[kind].add(name)
    return url_thumb, url_full


def type_info(raw_type):
    disp, bucket = TYPE_MAP.get(raw_type, (title(raw_type), "Other"))
    return disp, bucket


# ---------- COOKWARE ----------
cw_raw = json.loads((RAW / "cookware.raw.json").read_text(encoding="utf-8"))
merged, order = {}, []
for p in cw_raw:
    key = (p.get("series"), p.get("type"), p.get("art_no"), p.get("size"))
    if key not in merged:
        merged[key] = {**p, "photos": list(p.get("photos") or ([p["photo"]] if p.get("photo") else []))}
        order.append(key)
    else:
        for ph in (p.get("photos") or []):
            if ph not in merged[key]["photos"]:
                merged[key]["photos"].append(ph)

# Build one variant per raw row, then GROUP size-variants that share a photo into a
# single product with a `configs` list — the catalog shows one photo per product with a
# spec table of sizes, not one card per size.
def config_specs(size, wall, bottom, art):
    out = []
    nums = re.findall(r"[\d.]+", size or "")
    if len(nums) >= 3:  # rectangular L×W×H (roasters, grill trays, fish/oval pans)
        out.append({"label": "dimensions", "value": f"{nums[0]} × {nums[1]} × {nums[2]} cm"})
    elif len(nums) == 2:  # round Ø diameter × height
        out.append({"label": "diameter", "value": f"{nums[0]} cm"})
        out.append({"label": "height", "value": f"{nums[1]} cm"})
    elif size:
        out.append({"label": "size", "value": size})
    if wall:
        out.append({"label": "wallThickness", "value": f"{wall} mm"})
    if bottom:
        out.append({"label": "bottomThickness", "value": f"{bottom} mm"})
    return out  # Collection/Type/Article No are shown as badges, not spec rows


groups, gorder = {}, []
for key in order:
    p = merged[key]
    series = p.get("series", "")
    type_disp, type_group = type_info(p.get("type", ""))
    collection = None if series in TYPE_ONLY_SERIES else series
    size = (p.get("size") or "").replace("Φ", "Ø")
    art = p.get("art_no", "")
    photos = [x for x in p.get("photos", []) if x]
    images = []
    for ph in photos:
        t, f = copy_img(ph, "cookware")
        if {"thumb": t, "full": f} not in images:
            images.append({"thumb": t, "full": f})
    cfg = {"artNo": art, "size": size, "wall": p.get("wall"),
           "bottom": p.get("bottom"), "specs": config_specs(size, p.get("wall"), p.get("bottom"), art)}

    # group key: same section + type = one product offered in several sizes (matches
    # review.html, which groups one card per series+type and collects every photo into a
    # gallery — primary image first, the rest as secondary/alternate views).
    gkey = (series, type_disp)
    if gkey not in groups:
        groups[gkey] = {
            "series": series, "type_disp": type_disp, "type_group": type_group,
            "collection": collection, "collection_label": collection or SPECIALTY_LABEL,
            "page": p.get("page"), "images": list(images), "configs": [cfg],
        }
        gorder.append(gkey)
    else:
        g = groups[gkey]
        g["configs"].append(cfg)
        for img in images:
            if img not in g["images"]:
                g["images"].append(img)

cookware, seen_ids = [], set()
for gkey in gorder:
    g = groups[gkey]
    type_disp, collection = g["type_disp"], g["collection"]
    name = type_disp if collection is None else f"{g['series']} {type_disp}"
    pid = uniq_id(slug(g["configs"][0]["artNo"]) or slug(f"{g['series']}-{type_disp}"), seen_ids)
    images = g["images"]
    cookware.append({
        "id": pid, "name": name,
        "section": g["series"], "page": g["page"],
        "collection": collection, "collectionLabel": g["collection_label"],
        "type": type_disp, "typeGroup": g["type_group"],
        "image": images[0]["thumb"] if images else None,
        "full": images[0]["full"] if images else None,
        "images": images,
        "commonSpecs": [],
        "configs": g["configs"],
    })

# Order into catalog reading order: sections sorted by their first page, products keep
# their original order within a section (stable sort makes each section contiguous).
_sec_page, _sec_first = {}, {}
for i, c in enumerate(cookware):
    s = c["section"]
    pg = c["page"] if isinstance(c["page"], int) else 999
    if s not in _sec_page or pg < _sec_page[s]:
        _sec_page[s] = pg
    _sec_first.setdefault(s, i)
cookware.sort(key=lambda c: (_sec_page[c["section"]], _sec_first[c["section"]]))

# ---------- RADIATORS ----------
rd_raw = json.loads((RAW / "radiators.raw.json").read_text(encoding="utf-8"))
radiators, seen_ids = [], set()
for p in rd_raw:
    cat = p.get("category", "")
    model = (p.get("model") or "").strip()
    name = model or f"{title(cat)} Radiator"
    pid = uniq_id(slug(model) or slug(f"{cat}-{p.get('page')}"), seen_ids)
    stem = Path(p.get("photo") or p.get("image") or "").stem
    images = []
    if stem:
        t, f = copy_img(f"effects/web/thumb/{stem}.webp", "radiators")
        images.append({"thumb": t, "full": f})
    specs = []  # Model + Category are shown as badges, not spec rows
    for k, label, unit in [
        ("dimension_LWH_mm", "dimensions", "mm"),
        ("central_distance_mm", "centralDistance", "mm"),
        ("thermal_output_w", "thermalOutput", "W"),
        ("weight_kg", "weight", "kg"),
        ("water_capacity_L", "waterCapacity", "L"),
        ("working_pressure_mpa", "workingPressure", "MPa"),
        ("wall_thickness_mm", "wallThickness", "mm"),
        ("connecting_size", "connectingSize", ""),
    ]:
        v = p.get(k)
        if v not in ("", None):
            specs.append({"label": label, "value": f"{v} {unit}".strip()})
    radiators.append({
        "id": pid, "name": name, "category": cat, "model": model,
        "image": images[0]["thumb"] if images else None,
        "full": images[0]["full"] if images else None,
        "images": images, "specs": specs,
    })

(DATA / "cookware.json").write_text(json.dumps(cookware, ensure_ascii=False, indent=2), encoding="utf-8")
(DATA / "radiators.json").write_text(json.dumps(radiators, ensure_ascii=False, indent=2), encoding="utf-8")

collections = sorted({c["collectionLabel"] for c in cookware})
groups = sorted({c["typeGroup"] for c in cookware})
print(f"cookware: {len(cookware)} products | {len(collections)} collections | type groups: {groups}")
print(f"specialty (type-only) items: {sum(1 for c in cookware if c['collection'] is None)}")
print(f"radiators: {len(radiators)} products")
print(f"images touched: cookware={len(copied['cookware'])} radiators={len(copied['radiators'])}")
