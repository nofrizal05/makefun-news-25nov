"""make.fun entry: news-image-20261125 — "The World in One Day — 25 November 2026".

The entry is a finished newspaper front page (1024x1024 PNG) that sums up
Wednesday 25 November 2026's world news in a single image. The front page
is built around six lead stories, all real news first reported on 24–25
November 2026 (see news-research-20261125.md for sources):

  * Lead: Houthi drone strike on Riyadh's tallest tower — 11 wounded,
    the second hit on the PIF headquarters in under a week.
  * Zelenskyy confirms Ukraine's drone strike on the Russian cargo ship
    Sparta II in the Gulf of Finland.
  * Nvidia's Jensen Huang returns as CEO; shares jump 31.5% in a day.
  * Huawei convicted in the US of stealing trade secrets, cleared of
    racketeering.
  * Shanghai party chief Chen Jining placed under a corruption probe.
  * Record king tides flood California's coast ahead of Thanksgiving.

A footer strip carries eight smaller headlines of the day, and a
"The Day in Numbers" box collects the day's figures (11 wounded,
385 m tower, +31.5%, 8.23 ft tide).

The image was drawn locally and is shipped with this entry as entry.png.
This program does the only thing the grading sandbox needs: it copies that
shipped image into the output directory make.fun provides, so the run is
fully deterministic. Standard library only — no third-party packages,
because the sandbox runs Python 3.13 with nothing installed.
"""

import os
import shutil
from pathlib import Path

# The finished front page, shipped next to this file.
SHIPPED_IMAGE = Path(__file__).resolve().parent / "entry.png"

# make.fun hands the output directory to the entry through this variable;
# /output is the documented fallback.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    """Copy the shipped front page to the output directory."""
    if not SHIPPED_IMAGE.is_file():
        raise FileNotFoundError(f"shipped image missing: {SHIPPED_IMAGE}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    destination = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SHIPPED_IMAGE, destination)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
