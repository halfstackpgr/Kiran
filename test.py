from kiran.errors import KiranUnkownError


def main() -> None:
    raise KiranUnkownError("test", None)

try: 
    main()
except KiranUnkownError as e:
    e.bug_drop()