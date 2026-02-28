import json

def patch(source, patch_obj):
    for key, value in patch_obj.items():
        if value is None:
            source.pop(key, None)
        elif key in source and isinstance(source[key], dict) and isinstance(value, dict):
            patch(source[key], value)
        else:
            source[key] = value
    return source


source = json.loads(input())
patch_obj = json.loads(input())

result = patch(source, patch_obj)

print(json.dumps(result, separators=(',', ':'), sort_keys=True))