# GeoMap Lite

[![Version](https://img.shields.io/badge/version-v2.18.1-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

这是 GeoMap Lite 的稳定入口仓库。自 v2.18.1 起，Full 与 Lite 不再保存两套业务源码：实际应用统一由 [`Geomap-app`](https://github.com/Superhedgehoger/Geomap-app) 构建，本仓库的 GitHub Pages 只将访问者转到 `Geomap-app/?variant=lite`。

- 在线入口：<https://superhedgehoger.github.io/Geomap-app-lite/>
- 实际 Lite 应用：<https://superhedgehoger.github.io/Geomap-app/?variant=lite>
- 唯一业务源码：<https://github.com/Superhedgehoger/Geomap-app>

Lite 模式保留地图绘制、图层管理、时间轴、框选、范围圈和数据导入导出，并关闭事件追踪器及其事件徽章、Popup 摘要与编辑入口。

## 本地检查

```bash
python3 -m unittest discover -s tests -v
python3 server.py
```

本仓库仅维护入口页、部署配置和入口回归测试。功能修改和问题修复请提交到 Full 仓库。

## License

MIT，详见 [LICENSE](LICENSE)。
