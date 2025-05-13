import json
from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Traits.json"

with open(json_path, "r", encoding="utf-8") as f:
    traits = json.load(f)

# İlk turda tüm trait'leri insert edip id'lerini url üzerinden yakalayacağız
with engine.begin() as conn:
    # Tabloyu sıfırla
    conn.execute(text("TRUNCATE TABLE traits RESTART IDENTITY CASCADE"))

    # İlk adım: name, description, url eklenir, geri kalanı sonra update edilir
    for trait in traits:
        name = trait.get("name")
        url = trait.get("url")
        desc = trait.get("desc")
        if isinstance(desc, list):
            description = "\n\n".join(desc)
        else:
            description = desc

        conn.execute(text("""
            INSERT INTO traits (name, description, url)
            VALUES (:name, :description, :url)
        """), {
            "name": name,
            "description": description,
            "url": url
        })

    # Şimdi tüm traits veritabanında mevcut. Update işlemleri yapabiliriz
    for trait in traits:
        url = trait.get("url")

        # Trait ID'yi bul
        result = conn.execute(text("SELECT id FROM traits WHERE url = :url"), {"url": url})
        trait_id = result.scalar()
        if not trait_id:
            continue

        # subrace_id
        subrace_id = None
        subraces = trait.get("subraces", [])
        if subraces:
            sub_url = subraces[0].get("url") if isinstance(subraces[0], dict) else None
            if sub_url:
                res = conn.execute(text("SELECT id FROM subraces WHERE url = :url"), {"url": sub_url})
                subrace_id = res.scalar()

        # parent
        parent_id = None
        parent = trait.get("parent")
        if isinstance(parent, dict):
            parent_url = parent.get("url")
            if parent_url:
                res = conn.execute(text("SELECT id FROM traits WHERE url = :url"), {"url": parent_url})
                parent_id = res.scalar()

        # proficiencies varsa → kendi trait_id’sini yaz
        prof_self = trait_id if trait.get("proficiencies") else None

        # races varsa → kendi trait_id’sini yaz
        race_self = trait_id if trait.get("races") else None

        # trait_proficiency_id varsa
        has_proficiency = "proficiency_choices" in trait or "trait_specific" in trait
        trait_proficiency_id = trait_id if has_proficiency else None

        # extra_language sadece 1 trait'e yazılır (dil seçenekli)
        extra_language = 1 if "language_options" in trait else None

        # Güncelleme
        conn.execute(text("""
            UPDATE traits
            SET subrace_id = :subrace_id,
                parent = :parent,
                proficiencies = :proficiencies,
                races = :races,
                extra_language = :extra_language,
                trait_proficiency_id = :trait_proficiency_id
            WHERE id = :trait_id
        """), {
            "subrace_id": subrace_id,
            "parent": parent_id,
            "proficiencies": prof_self,
            "races": race_self,
            "extra_language": extra_language,
            "trait_proficiency_id": trait_proficiency_id,
            "trait_id": trait_id
        })

print("✅ traits tablosu başarıyla yüklendi ve güncellendi.")
