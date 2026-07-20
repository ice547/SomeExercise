#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
organize_media.py

功能:
    掃描指定「根資料夾」底下的所有子資料夾(可控制掃描深度),
    找出其中的 .gif 與 .mp4 檔案,
    並將每個檔案各自搬到「與檔案同目錄、以檔名命名(不含副檔名)」的新資料夾中。

範例:
    整理前:
        root/
            folderA/
                cat.gif
                dog.mp4
            folderB/
                movie.mp4

    整理後:
        root/
            folderA/
                cat/
                    cat.gif
                dog/
                    dog.mp4
            folderB/
                movie/
                    movie.mp4

用法:
    # 先預覽,不會真的搬檔案
    python organize_media.py "C:/path/to/root" --dry-run

    # 確認沒問題後,真的執行搬移
    python organize_media.py "C:/path/to/root"

    # 若同時要處理更多副檔名
    python organize_media.py "C:/path/to/root" --ext gif mp4 png

    # 如果檔名相同的資料夾已存在,想要覆蓋/合併(預設是跳過並提示)
    python organize_media.py "C:/path/to/root" --skip-existing
"""

import argparse
import shutil
import sys
from pathlib import Path


def collect_target_files(root: Path, extensions: set[str]) -> list[Path]:
    """遞迴收集 root 底下所有符合副檔名的檔案(不含 root 本身這一層,只找子資料夾內的檔案)"""
    targets = []
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower().lstrip(".") in extensions:
            # 排除直接放在 root 底下(不在任何子資料夾內)的檔案,
            # 若也想處理 root 底下的檔案,把下面這個 if 拿掉即可
            if path.parent != root:
                targets.append(path)
    return targets


def organize(root: Path, extensions: set[str], dry_run: bool, skip_existing: bool) -> None:
    files = collect_target_files(root, extensions)

    if not files:
        print(f"在 {root} 底下的子資料夾中,找不到符合條件的檔案 ({', '.join(sorted(extensions))})")
        return

    print(f"共找到 {len(files)} 個檔案,開始{'預覽' if dry_run else '搬移'}...\n")

    moved, skipped = 0, 0

    for file_path in files:
        target_dir = file_path.parent / file_path.stem
        target_path = target_dir / file_path.name

        if target_path.exists():
            print(f"[跳過] 目標已存在: {target_path}")
            skipped += 1
            continue

        if dry_run:
            print(f"[預覽] {file_path}  ->  {target_path}")
        else:
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file_path), str(target_path))
            print(f"[完成] {file_path}  ->  {target_path}")

        moved += 1

    print(f"\n{'預覽' if dry_run else '搬移'}結束: 共 {moved} 個檔案, 跳過 {skipped} 個")


def main():
    parser = argparse.ArgumentParser(
        description="把子資料夾內的 gif/mp4 檔案各自搬到以檔名命名的資料夾中"
    )
    parser.add_argument("root", type=str, help="要處理的根資料夾路徑")
    parser.add_argument(
        "--ext",
        nargs="+",
        default=["gif", "mp4"],
        help="要處理的副檔名清單(不需加點),預設為 gif mp4",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只預覽會執行的動作,不會真的搬移檔案",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="若目標資料夾/檔案已存在則跳過(預設行為即為跳過並提示)",
    )

    args = parser.parse_args()
    root = Path(args.root).expanduser().resolve()

    if not root.exists() or not root.is_dir():
        print(f"錯誤: 找不到資料夾 {root}")
        sys.exit(1)

    extensions = {e.lower().lstrip(".") for e in args.ext}
    organize(root, extensions, dry_run=args.dry_run, skip_existing=args.skip_existing)


if __name__ == "__main__":
    main()