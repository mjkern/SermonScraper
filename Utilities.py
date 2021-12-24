def sanitize_filename(filename):
    # taken from https://stackoverflow.com/questions/7406102/create-sane-safe-filename-from-any-unsafe-string
    return "".join([c for c in filename if c.isalpha() or c.isdigit() or c==' ']).rstrip()