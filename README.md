# uv Python Template

## Overview

このリポジトリは、`uv` を使ってすぐに Python 開発を始めるためのテンプレートです。

## Quick Start

1. `uv` をインストール
2. 仮想環境を作成
3. 依存関係を同期

```bash
uv venv
uv sync --no-install-project
```

## Check

```bash
PYTHONDONTWRITEBYTECODE=1 uv run python -c "import sys; print(sys.dont_write_bytecode)"
```

`__pycache__` を出したくないコマンドは、上記のように `PYTHONDONTWRITEBYTECODE=1` を付けて実行してください（この設定は付与したコマンド実行時のみ有効です）。
