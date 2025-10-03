#!/usr/bin/env python3
"""清除 Python 快取文件的腳本。

這個腳本會清除專案中的所有 Python 快取文件，包括：
- __pycache__ 目錄
- .pyc 文件
- .pyo 文件

使用方法:
    python scripts/clear_cache.py [--include-venv] [--quiet]

選項:
    --include-venv    同時清除虛擬環境中的快取文件
    --quiet          減少輸出訊息
"""

# ===== 標準函式庫 =====
import argparse  # 解析命令行參數
from pathlib import Path
import shutil  # 刪除目錄和文件
import sys  # 退出腳本


def clear_python_cache(include_venv=False, quiet=False):
    """清除 Python 快取文件。"""
    if not quiet:
        print("🧹 開始清除 Python 快取文件...")

    # 獲取專案根目錄
    project_root = Path(__file__).parent.parent
    if not quiet:
        print(f"📁 專案根目錄: {project_root}")

    # 定義要排除的目錄（這些目錄通常很大且不需要清除快取）
    exclude_dirs = {
        '.git',
        '.svn',
        '.hg',  # 版本控制目錄
        'node_modules',  # Node.js 模組
        'dist',
        'build',  # 建置目錄
        '.pytest_cache',  # pytest 快取
        'htmlcov',  # 測試覆蓋率報告
        'logs',  # 日誌目錄
        'alembic/versions',  # 資料庫遷移版本
    }

    # 如果不包含虛擬環境，則排除虛擬環境目錄
    if not include_venv:
        exclude_dirs.update(
            {
                '.venv',
                'venv',
                'env',  # 虛擬環境
            }
        )

    # 定義要優先檢查的 Python 目錄
    priority_dirs = ['app', 'tests', 'scripts', 'alembic']
    if include_venv:
        priority_dirs.append('.venv')

    # 統計清除的文件數量
    removed_dirs = 0
    removed_files = 0
    skipped_items = 0
    failed_items = []

    if not quiet:
        print("🔍 搜尋並清除快取文件...")

    # 首先檢查優先目錄（這些目錄最可能有快取文件）
    for priority_dir in priority_dirs:
        priority_path = project_root / priority_dir
        if priority_path.exists():
            if not quiet:
                print(f"  📂 檢查 {priority_dir} 目錄...")

            # 搜尋並刪除 __pycache__ 目錄
            for pycache_dir in priority_path.rglob("__pycache__"):
                if not any(exclude in str(pycache_dir) for exclude in exclude_dirs):
                    if pycache_dir.exists():
                        try:
                            shutil.rmtree(pycache_dir)
                            removed_dirs += 1
                            if not quiet:
                                print(f"    ✅ 已刪除目錄: {pycache_dir}")
                        except FileNotFoundError:
                            skipped_items += 1
                        except PermissionError as e:
                            error_msg = f"權限不足: {e}"
                            if not quiet:
                                print(f"    ❌ 刪除失敗 {pycache_dir}: {error_msg}")
                            failed_items.append(('dir', pycache_dir, error_msg))
                        except Exception as e:
                            error_msg = f"未知錯誤: {e}"
                            if not quiet:
                                print(f"    ❌ 刪除失敗 {pycache_dir}: {error_msg}")
                            failed_items.append(('dir', pycache_dir, error_msg))

            # 搜尋並刪除 .pyc 和 .pyo 文件
            for pyc_file in priority_path.rglob("*.pyc"):
                if not any(exclude in str(pyc_file) for exclude in exclude_dirs):
                    if pyc_file.exists():
                        try:
                            pyc_file.unlink()
                            removed_files += 1
                            if not quiet:
                                print(f"    ✅ 已刪除文件: {pyc_file}")
                        except FileNotFoundError:
                            skipped_items += 1
                        except PermissionError as e:
                            error_msg = f"權限不足: {e}"
                            if not quiet:
                                print(f"    ❌ 刪除失敗 {pyc_file}: {error_msg}")
                            failed_items.append(('file', pyc_file, error_msg))
                        except Exception as e:
                            error_msg = f"未知錯誤: {e}"
                            if not quiet:
                                print(f"    ❌ 刪除失敗 {pyc_file}: {error_msg}")
                            failed_items.append(('file', pyc_file, error_msg))

            for pyo_file in priority_path.rglob("*.pyo"):
                if not any(exclude in str(pyo_file) for exclude in exclude_dirs):
                    if pyo_file.exists():
                        try:
                            pyo_file.unlink()
                            removed_files += 1
                            if not quiet:
                                print(f"    ✅ 已刪除文件: {pyo_file}")
                        except FileNotFoundError:
                            skipped_items += 1
                        except PermissionError as e:
                            error_msg = f"權限不足: {e}"
                            if not quiet:
                                print(f"    ❌ 刪除失敗 {pyo_file}: {error_msg}")
                            failed_items.append(('file', pyo_file, error_msg))
                        except Exception as e:
                            error_msg = f"未知錯誤: {e}"
                            if not quiet:
                                print(f"    ❌ 刪除失敗 {pyo_file}: {error_msg}")
                            failed_items.append(('file', pyo_file, error_msg))

    # 然後檢查其他目錄（但跳過已知的大型目錄）
    if not quiet:
        print("  📂 檢查其他目錄...")
    for item in project_root.iterdir():
        if (
            item.is_dir()
            and item.name not in exclude_dirs
            and item.name not in priority_dirs
        ):
            # 只檢查第一層的 __pycache__ 目錄
            pycache_dir = item / "__pycache__"
            if pycache_dir.exists():
                try:
                    shutil.rmtree(pycache_dir)
                    removed_dirs += 1
                    if not quiet:
                        print(f"    ✅ 已刪除目錄: {pycache_dir}")
                except FileNotFoundError:
                    skipped_items += 1
                except PermissionError as e:
                    error_msg = f"權限不足: {e}"
                    if not quiet:
                        print(f"    ❌ 刪除失敗 {pycache_dir}: {error_msg}")
                    failed_items.append(('dir', pycache_dir, error_msg))
                except Exception as e:
                    error_msg = f"未知錯誤: {e}"
                    if not quiet:
                        print(f"    ❌ 刪除失敗 {pycache_dir}: {error_msg}")
                    failed_items.append(('dir', pycache_dir, error_msg))

            # 檢查 .pyc 和 .pyo 文件
            for pyc_file in item.glob("*.pyc"):
                if pyc_file.exists():
                    try:
                        pyc_file.unlink()
                        removed_files += 1
                        if not quiet:
                            print(f"    ✅ 已刪除文件: {pyc_file}")
                    except FileNotFoundError:
                        skipped_items += 1
                    except PermissionError as e:
                        error_msg = f"權限不足: {e}"
                        if not quiet:
                            print(f"    ❌ 刪除失敗 {pyc_file}: {error_msg}")
                        failed_items.append(('file', pyc_file, error_msg))
                    except Exception as e:
                        error_msg = f"未知錯誤: {e}"
                        if not quiet:
                            print(f"    ❌ 刪除失敗 {pyc_file}: {error_msg}")
                        failed_items.append(('file', pyc_file, error_msg))

            for pyo_file in item.glob("*.pyo"):
                if pyo_file.exists():
                    try:
                        pyo_file.unlink()
                        removed_files += 1
                        if not quiet:
                            print(f"    ✅ 已刪除文件: {pyo_file}")
                    except FileNotFoundError:
                        skipped_items += 1
                    except PermissionError as e:
                        error_msg = f"權限不足: {e}"
                        if not quiet:
                            print(f"    ❌ 刪除失敗 {pyo_file}: {error_msg}")
                        failed_items.append(('file', pyo_file, error_msg))
                    except Exception as e:
                        error_msg = f"未知錯誤: {e}"
                        if not quiet:
                            print(f"    ❌ 刪除失敗 {pyo_file}: {error_msg}")
                        failed_items.append(('file', pyo_file, error_msg))

    # 顯示統計結果
    removed_dirs + removed_files + skipped_items

    if not quiet:
        print(f"\n✅ 清除完成！")
        print("📊 統計結果:")
        print(f"   - 成功刪除目錄: {removed_dirs} 個")
        print(f"   - 成功刪除文件: {removed_files} 個")
        if skipped_items > 0:
            print(f"   - 跳過已不存在的項目: {skipped_items} 個")
    else:
        print(f"✅ 清除完成！刪除 {removed_dirs} 個目錄，{removed_files} 個文件")

    if failed_items:
        if not quiet:
            print(f"   - 失敗項目: {len(failed_items)} 個")
            print("\n❌ 失敗項目詳情:")
            for item_type, item_path, error in failed_items:
                print(f"     {item_type}: {item_path} - {error}")
        else:
            print(f"⚠️  有 {len(failed_items)} 個項目刪除失敗")

    # 快速驗證（只檢查主要目錄）
    if not quiet:
        print("\n🔍 快速驗證...")
    remaining_count = 0

    for priority_dir in priority_dirs:
        priority_path = project_root / priority_dir
        if priority_path.exists():
            remaining = list(priority_path.rglob("__pycache__"))
            remaining_count += len(remaining)

    if remaining_count > 0:
        if not quiet:
            print(f"⚠️  警告: 仍有 {remaining_count} 個快取目錄可能存在")
            print("💡 建議: 可能需要管理員權限或檢查文件鎖定狀態")
        else:
            print(f"⚠️  仍有 {remaining_count} 個快取目錄存在")
    else:
        if not quiet:
            print("🎉 所有快取文件已完全清除！")
        else:
            print("🎉 快取清除完成！")


def main():
    """主函數，處理命令行參數。"""
    parser = argparse.ArgumentParser(
        description="清除 Python 快取文件",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
範例:
  python scripts/clear_cache.py              # 清除專案快取文件
  python scripts/clear_cache.py --include-venv  # 同時清除虛擬環境快取文件
  python scripts/clear_cache.py --quiet      # 減少輸出訊息
        """,
    )

    parser.add_argument(
        '--include-venv', action='store_true', help='同時清除虛擬環境中的快取文件'
    )
    parser.add_argument('--quiet', action='store_true', help='減少輸出訊息')

    args = parser.parse_args()

    try:
        clear_python_cache(include_venv=args.include_venv, quiet=args.quiet)
    except KeyboardInterrupt:
        print("\n⏹️  操作已取消")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 發生錯誤: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
