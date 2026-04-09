# -*- coding: utf-8 -*-
"""
===================================
WebUI 启动脚本
===================================

用于启动 Web 服务界面。
直接运行 `python webui.py` 将启动 Web 后端服务。

等效命令：
    python main.py --webui-only

Usage:
  python webui.py
  API_HOST=0.0.0.0 API_PORT=8000 python webui.py
"""

from __future__ import annotations

import os
import logging

logger = logging.getLogger(__name__)


def main() -> int:
    """
    启动 Web 服务
    """
    # API_HOST/API_PORT 为正式变量名，WEBUI_* 为旧版兼容
    host = os.getenv("API_HOST", os.getenv("WEBUI_HOST", "127.0.0.1"))
    port = int(os.getenv("API_PORT", os.getenv("WEBUI_PORT", "8000")))

    print(f"正在启动 Web 服务: http://{host}:{port}")
    print(f"API 文档: http://{host}:{port}/docs")
    print()

    try:
        import uvicorn
        from src.config import setup_env
        from src.logging_config import setup_logging

        setup_env()
        setup_logging(log_prefix="web_server")

        uvicorn.run(
            "api.app:app",
            host=host,
            port=port,
            log_level="info",
        )
    except KeyboardInterrupt:
        pass

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
