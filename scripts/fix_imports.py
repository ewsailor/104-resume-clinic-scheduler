#!/usr/bin/env python3
"""自定義腳本。

將函式內部的 import 語句移到檔案頂部
"""

# ===== 標準函式庫 =====
import ast
from pathlib import Path
import sys


def extract_imports_from_functions(file_path: str) -> tuple[list[str], list[str]]:
    """從檔案中提取函式內部的 import 語句。

    Args:
        file_path: 檔案路徑

    Returns:
        tuple[list[str], list[str]]: (頂部 imports, 函式內部 imports)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 解析 AST
    try:
        tree = ast.parse(content)
    except SyntaxError:
        print(f"警告：{file_path} 有語法錯誤，跳過處理")
        return [], []

    function_imports = []
    top_level_imports = []

    # 收集頂層的 import 語句
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            if hasattr(node, 'lineno'):
                # 檢查是否在函式內部
                in_function = False
                for parent in ast.walk(tree):
                    if isinstance(parent, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        if (
                            hasattr(parent, 'lineno')
                            and hasattr(parent, 'end_lineno')
                            and parent.lineno <= node.lineno <= parent.end_lineno
                        ):
                            in_function = True
                            break

                if in_function:
                    # 提取 import 語句的原始文字
                    lines = content.split('\n')
                    if node.lineno - 1 < len(lines):
                        import_line = lines[node.lineno - 1].strip()
                        if import_line.startswith(('import ', 'from ')):
                            # 處理包含多個語句的行（如 import pdb; pdb.set_trace()）
                            if ';' in import_line:
                                # 分割多個語句
                                statements = [s.strip() for s in import_line.split(';')]
                                for stmt in statements:
                                    if stmt.startswith(('import ', 'from ')):
                                        function_imports.append(stmt)
                                # 記錄需要移除的原始行
                                function_imports.append(import_line)
                            else:
                                function_imports.append(import_line)
                else:
                    # 提取頂層 import 語句
                    lines = content.split('\n')
                    if node.lineno - 1 < len(lines):
                        import_line = lines[node.lineno - 1].strip()
                        if import_line.startswith(('import ', 'from ')):
                            top_level_imports.append(import_line)

    return top_level_imports, function_imports


def fix_imports_in_file(file_path: str) -> bool:
    """修復檔案中的 import 語句。

    Args:
        file_path: 檔案路徑

    Returns:
        bool: 是否有修改
    """
    print(f"處理檔案：{file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    top_level_imports, function_imports = extract_imports_from_functions(file_path)

    if not function_imports:
        print(f"  - 沒有發現函式內部的 import 語句")
        return False

    print(f"  - 發現 {len(function_imports)} 個函式內部的 import 語句")

    # 移除函式內部的 import 語句
    lines = content.split('\n')
    new_lines = []

    for i, line in enumerate(lines):
        stripped = line.strip()

        # 跳過函式內部的 import 語句
        if stripped in function_imports:
            print(f"    - 移除：{stripped}")
            continue

        # 跳過空行（如果前面是 import 語句）
        if stripped == '' and i > 0 and lines[i - 1].strip() in function_imports:
            continue

        new_lines.append(line)

    # 在檔案頂部添加 import 語句
    if function_imports:
        # 找到第一個非 import 語句的位置，但要跳過 docstring
        insert_pos = 0
        in_docstring = False
        docstring_started = False

        for i, line in enumerate(new_lines):
            stripped = line.strip()

            # 檢查是否進入 docstring
            if stripped.startswith('"""') or stripped.startswith("'''"):
                if not docstring_started:
                    docstring_started = True
                    in_docstring = True
                else:
                    in_docstring = False
                    docstring_started = False
                continue

            # 如果在 docstring 內，跳過
            if in_docstring:
                continue

            # 找到第一個非 import 語句的位置
            if (
                stripped
                and not stripped.startswith(('import ', 'from ', '#', '"""', "'''"))
                and not stripped.startswith('__')
            ):
                insert_pos = i
                break

        # 插入新的 import 語句
        new_imports = []
        for imp in function_imports:
            if imp not in top_level_imports:  # 避免重複
                new_imports.append(imp)

        if new_imports:
            # 在適當位置插入 import 語句
            if insert_pos > 0:
                new_lines.insert(insert_pos, '')
                insert_pos += 1

            for imp in new_imports:
                new_lines.insert(insert_pos, imp)
                insert_pos += 1

            if insert_pos < len(new_lines):
                new_lines.insert(insert_pos, '')

    # 寫回檔案
    new_content = '\n'.join(new_lines)
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  - 已修復 {len(function_imports)} 個 import 語句")
        return True

    return False


def main():
    """主函式。"""
    if len(sys.argv) < 2:
        print("用法：python fix_imports.py <檔案路徑>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not Path(file_path).exists():
        print(f"錯誤：檔案 {file_path} 不存在")
        sys.exit(1)

    if fix_imports_in_file(file_path):
        print("修復完成！")
    else:
        print("沒有需要修復的內容")


if __name__ == "__main__":
    main()
