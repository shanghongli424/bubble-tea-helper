# 2026-04-27

## Bubble Tea Helper 项目重要规则

### ⚠️ 文件名规则（必须遵守）
- GitHub Pages 默认入口是 `index.html`，不是 `bubble-tea.html`
- 以后所有代码修改必须直接改 `index.html`，不能再用 `bubble-tea.html`
- 如果仓库里同时存在两个文件，GitHub Pages 会忽略 `bubble-tea.html`
- 每次 commit 前确认修改的是 `index.html`

### GitHub 相关
- GitHub Pages 仓库: https://github.com/shanghongli424/bubble-tea-helper
- 远程仓库已配置 GitHub token 认证（credential helper store）
- 每次 push 前确保 `index.html` 是最新修改的文件
- 如果本地 `bubble-tea.html` 存在，需同步到 `index.html` 后再 commit

### 语音朗读功能
- Web Speech API (speechSynthesis)
- 大多数设备中文只有女声，男声选项因系统限制实际无效
- 已简化：点击🔊图标直接开关，无需弹窗
