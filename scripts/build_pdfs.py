#!/usr/bin/env python3
"""
build_pdfs.py — compile every .tex file in the repo to PDF.

Usage:
    python scripts/build_pdfs.py              # compile all
    python scripts/build_pdfs.py --dry-run   # show what would be compiled
    python scripts/build_pdfs.py --one 00-foundations/iam/iam_core.tex

Requires a TeX Live installation with pdflatex and latexmk.
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def find_tex_files(root: Path):
    return sorted(root.rglob("*.tex"))


def compile_one(tex_path: Path, dry_run: bool = False) -> bool:
    """Compile a single .tex to .pdf using latexmk."""
    tex_abs = tex_path.resolve()
    if not tex_abs.exists():
        print(f"SKIP (not found): {tex_abs}")
        return True

    dir_path = tex_abs.parent
    base = tex_abs.stem
    pdf_path = dir_path / f"{base}.pdf"

    print(f"=== {tex_abs.relative_to(Path.cwd())} ===")

    if dry_run:
        print(f"  [dry-run] would compile -> {pdf_path.name}")
        return True

    try:
        result = subprocess.run(
            ["latexmk", "-pdf", "-quiet", "-interaction=nonstopmode", str(tex_abs)],
            cwd=str(dir_path),
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode != 0:
            print(f"  FAIL (latexmk exit {result.returncode})")
            if result.stdout:
                print(f"  stdout: {result.stdout[-500:]}")
            if result.stderr:
                print(f"  stderr: {result.stderr[-500:]}")
            return False

        if pdf_path.exists():
            size_kb = pdf_path.stat().st_size / 1024
            print(f"  OK -> {pdf_path.name} ({size_kb:.1f} KB)")
            return True
        else:
            print(f"  WARN: pdflatex claimed success but {pdf_path.name} not found")
            return True
    except FileNotFoundError:
        print("  ERROR: latexmk not found — install TeX Live")
        return False
    except subprocess.TimeoutExpired:
        print("  ERROR: timed out after 120s")
        return False


def clean_aux(root: Path, dry_run: bool = False):
    """Remove auxiliary files (.aux, .log, .out, .toc, .fls, .fdb_latexmk)."""
    exts = {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".synctex.gz"}
    removed = 0
    for p in root.rglob("*"):
        if p.is_file() and p.suffix in exts:
            if dry_run:
                print(f"  [dry-run] would remove {p.relative_to(root)}")
            else:
                p.unlink()
                print(f"  removed {p.relative_to(root)}")
            removed += 1
    return removed


def main():
    parser = argparse.ArgumentParser(description="Compile all .tex files in the repo")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be compiled")
    parser.add_argument("--one", type=str, metavar="FILE", help="Compile only this .tex file")
    parser.add_argument("--clean", action="store_true", help="Remove auxiliary files")
    parser.add_argument("--clean-only", action="store_true", help="Clean aux files only, no compile")
    args = parser.parse_args()

    root = Path.cwd()

    if args.clean_only or (args.clean and not args.dry_run and not args.one):
        n = clean_aux(root, dry_run=args.dry_run)
        print(f"\nCleaned {n} auxiliary files")
        if args.clean_only:
            return 0

    if args.one:
        tex = Path(args.one)
        if not tex.exists():
            print(f"ERROR: {tex} not found")
            return 1
        ok = compile_one(tex, dry_run=args.dry_run)
        return 0 if ok else 1

    tex_files = find_tex_files(root)
    print(f"Found {len(tex_files)} .tex files\n")

    failed = 0
    for tex in tex_files:
        if not compile_one(tex, dry_run=args.dry_run):
            failed += 1

    print(f"\nDone: {len(tex_files) - failed}/{len(tex_files)} compiled successfully")
    if args.dry_run:
        print("(dry run — no files were written)")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
