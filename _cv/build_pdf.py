#!/usr/bin/env python3
"""Build files/cv.pdf from _cv/cv_source.html and _includes/cv-body.html."""
import pathlib
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

template = (ROOT / "_cv" / "cv_source.html").read_text(encoding="utf-8")
body = (ROOT / "_includes" / "cv-body.html").read_text(encoding="utf-8")
assert template.count("<!-- CV_BODY -->") == 1

with tempfile.TemporaryDirectory() as tmp:
    page = pathlib.Path(tmp) / "cv.html"
    page.write_text(template.replace("<!-- CV_BODY -->", body), encoding="utf-8")
    subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={ROOT / 'files' / 'cv.pdf'}", page.as_uri()],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
print("wrote", ROOT / "files" / "cv.pdf")
