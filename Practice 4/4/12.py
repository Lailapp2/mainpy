import json

MISSING = object()

def to_compact_json(value):
    # <missing> печатаем как есть (без кавычек)
    if value is MISSING:
        return "<missing>"
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)

def deep_diff(a, b, prefix=""):
    diffs = []

    # Оба должны быть объектами (dict) по условию
    keys = set(a.keys()) | set(b.keys())

    for key in keys:
        path = f"{prefix}.{key}" if prefix else key

        va = a.get(key, MISSING)
        vb = b.get(key, MISSING)

        # Если оба есть и оба dict — идём глубже
        if isinstance(va, dict) and isinstance(vb, dict):
            diffs.extend(deep_diff(va, vb, path))
        else:
            # Если разные (включая случаи missing)
            if va is MISSING or vb is MISSING or va != vb:
                diffs.append((path, va, vb))

    return diffs

obj1 = json.loads(input())
obj2 = json.loads(input())

diffs = deep_diff(obj1, obj2)

if not diffs:
    print("No differences")
else:
    for path, old, new in sorted(diffs, key=lambda x: x[0]):
        print(f"{path} : {to_compact_json(old)} -> {to_compact_json(new)}")