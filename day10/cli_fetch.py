from __future__ import annotations
import argparse
from pathlib import Path
from typing import Dict, Any

from api_basics import http_get_json, save_json, DATA_DIR

VALID_RESOURCES = {"posts", "users", "comments", "todos", "albums", "photos"}

def parse_params(pairs: list[str]) -> Dict[str, Any]:
    """
    Преобразует ["userId=1", "q=test"] -> {"userId": "1", "q": "test"}
    """
    out: Dict[str, Any] = {}
    for raw in pairs or []:
        if "=" not in raw:
            raise ValueError(f"Неверный формат параметра: {raw!r}, нужно key=value")
        k, v = raw.split("=", 1)
        out[k] = v
    return out

def main():
    parser = argparse.ArgumentParser(description="Fetch JSONPlaceholder resource via GET")
    parser.add_argument("resource", help=f"Ресурс: {', '.join(sorted(VALID_RESOURCES))}")
    parser.add_argument("--id", type=int, help="ID конкретного ресурса (например, /posts/1)")
    parser.add_argument("--param", action="append", help="Query-параметр key=value (можно несколько)")
    parser.add_argument("--timeout", type=float, default=5.0, help="Таймаут запроса в секундах")
    args = parser.parse_args()

    resource = args.resource.strip().lower()
    if resource not in VALID_RESOURCES:
        raise SystemExit(f"Неизвестный ресурс: {resource}. Допустимо: {', '.join(sorted(VALID_RESOURCES))}")

    params = parse_params(args.param)
    path = f"/{resource}"
    fname = resource

    if args.id is not None:
        path += f"/{args.id}"
        fname += f"_{args.id}"
    elif params:
        # Имя файла с параметрами (коротко)
        param_tag = "_".join(f"{k}-{v}" for k, v in sorted(params.items()))
        fname += f"_{param_tag}"

    data = http_get_json(path, params=params or None, timeout=args.timeout)

    out_path = DATA_DIR / f"{fname}.json"
    save_json(data, out_path)
    if isinstance(data, list):
        print(f"✅ Получен список из {len(data)} элементов → {out_path}")
    else:
        print(f"✅ Получен объект → {out_path}")

if __name__ == "__main__":
    main()
