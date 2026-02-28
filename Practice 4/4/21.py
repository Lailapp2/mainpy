import importlib
for _ in range(int(input())):
    m,a=input().split()
    try:
        mod=importlib.import_module(m)
        print("ATTRIBUTE_NOT_FOUND" if not hasattr(mod,a)
              else "CALLABLE" if callable(getattr(mod,a))
              else "VALUE")
    except ModuleNotFoundError:
        print("MODULE_NOT_FOUND")