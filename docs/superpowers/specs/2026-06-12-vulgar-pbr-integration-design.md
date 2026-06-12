# v4.0 低俗/色情识别规则 PBR 整合设计文档

## 基本信息
- **版本**: v1.0
- **日期**: 2026-06-12
- **作者**: TikTok Shop EU 运营团队
- **状态**: 待评审
- **关联文档**: 
  - [EMEA] [Listing] Shoptab Product Main Image Quality Vulgar Unified PBR
  - judgment_criteria.md v4.0
  - juror_system_prompt_v4.0.txt

## 背景与目标

### 背景
当前 v4.0 系统的 vulgar (泛低俗)、ansa (成人内容)、child_sexualization (儿童性化) 判定规则较为笼统，缺乏量化标准和细分类目，导致误判率较高。官方 PBR (Policy, Business, Rule) 文档提供了详细的判定标准和案例，需要整合到现有规则体系中。

### 目标
1. 将 PBR 文档的完整规则整合到 v4.0 系统中
2. 提供量化判定阈值，减少模糊地带
3. 降低 vulgar/ansa 相关的误判率和漏判率
4. 保持与官方 PBR 标准 100% 对齐

## 设计方案

### 总体架构
保持现有 19 类型体系不变，仅增强以下三个相关类型的判定标准：
- **Type 3: vulgar** (泛低俗) - 整合 PBR Rule 1-4 大部分内容
- **Type 6: ansa** (成人内容) - 整合 PBR 中涉及直接裸露的内容
- **Type 16: child_sexualization** (儿童性化) - 整合 PBR Rule 4 儿童安全内容

### 规则映射表

| PBR 规则编号 | PBR 规则名称 | 映射到 v4.0 类型 | 判定要点 |
|-------------|-------------|-----------------|---------|
| **Rule 1.1.1** | Breast exposure in lingerie | vulgar | 胸部暴露 > 1/2 或性暗示 |
| **Rule 1.1.2** | Zoomed-in breast imagery | vulgar | 胸部占画面 ≥ 50% |
| **Rule 1.1.3** | Protruding nipples | vulgar | 乳头透过衣物凸起 |
| **Rule 1.1.4** | Sticky bras & nipple covers | vulgar | 模特佩戴乳贴/隐形文胸 |
| **Rule 1.2.1** | Naked buttocks/uncovered buttcrack | ansa | 臀部全裸 + 臀沟全露 |
| **Rule 1.2.2** | Thongs and minimal coverage underwear | vulgar | 丁字裤导致臀部大部分暴露 |
| **Rule 1.2.3** | Full buttcrack through mesh clothing | vulgar | 透视装露出完整臀沟 |
| **Rule 1.2.4** | Upper butt crack | vulgar | 露出上臀沟 |
| **Rule 1.3.1** | Minimal garment coverage | vulgar | 微丁字裤仅覆盖极小部分 |
| **Rule 1.3.2** | Crotchless garments | vulgar | 开裆内衣穿在模特/假人身上 |
| **Rule 1.4** | Back Exposure | vulgar | 上半身背部全裸 |
| **Rule 2.1** | Bending over | vulgar | 性暗示方式弯腰 |
| **Rule 2.2** | Posing on all fours | vulgar | 性暗示方式四肢着地 |
| **Rule 2.3** | Posing on knees | vulgar | 性暗示方式跪姿 |
| **Rule 2.4** | Posing with spread legs | vulgar | 性暗示方式分腿 |
| **Rule 2.5** | Posing suggestively while laying down | vulgar | 性暗示方式躺卧 |
| **Rule 2.6** | Stripping/states of undress | vulgar | 脱衣动作或半脱状态 |
| **Rule 2.7** | Sexual facial expressions | vulgar | 性高潮表情、翻白眼等 |
| **Rule 2.8** | Kissing | vulgar | 两人接吻（无论是否穿衣） |
| **Rule 2.9** | Groping | vulgar | 抚摸胸部/阴部/臀部 |
| **Rule 2.10** | Suggestive camera angles or close-ups | vulgar | 暗示性拍摄角度或特写 |
| **Rule 3.1** | Underpants with faces/phallic symbols | vulgar | 内裤印有人脸或阳具符号 |
| **Rule 3.2** | Sexual roleplay uniforms and costumes | vulgar | 性角色扮演制服（护士、女仆、警察、学生等） |
| **Rule 3.3** | Sheer or mesh tops | vulgar | 透视上衣经 PS 去除乳头 |
| **Rule 3.4** | Products that resemble genitalia | vulgar | 商品造型类似生殖器（阴茎、睾丸、乳房、阴道等） |
| **Rule 3.5** | Silhouette/Cartoon/stick figure sexual poses | vulgar | 剪影/卡通/简笔画的性姿势 |
| **Rule 3.6** | Barry Wood Products | vulgar | Barry Wood 相关商品 |
| **Rule 3.7** | Wall flags/banners with models | vulgar | 旗帜上印有比基尼/少衣模特 |
| **Rule 3.8** | Scantily clothed models on posters/clothing/albums | vulgar | 海报/服装/专辑上印有少衣模特 |
| **Rule 3.9** | Sexual Anime Stickers and Decals | vulgar | 性感动漫贴纸（夸张胸部、性暗示姿势） |
| **Rule 3.10** | Sexual References or Innuendo to Genitalia | vulgar | 对生殖器的性暗示或隐喻（黄瓜、茄子等） |
| **Rule 3.11** | Prohibited Products - ANSA and Adult Products | ansa / prohibited | ANSA 和成人用品（人审专用规则，AI 参考） |
| **Rule 4.1** | Intimate Body Jewellery | vulgar | 私密部位珠宝（乳环、阴环、身体链等） |
| **Rule 4.2** | Erotic Body Harnesses & Accessories | vulgar | 情色束身带（笼式胸罩、开杯束带等） |
| **Rule 4.3** | Fetish & BDSM Accessories | vulgar | BDSM/恋物配饰（O 形环项圈、牵引绳、束缚手铐等） |
| **Rule 4 (Child)** | Sexualized Cartoon Characters | child_sexualization | 性化卡通人物 |

### 豁免规则整合

| 豁免编号 | 豁免内容 | 适用规则 |
|---------|---------|---------|
| **Exemption 1** | 书籍封面接吻 | Rule 2.8 Kissing |
| **Exemption 2** | 非性化提衣动作 | Rule 2.6 Stripping |
| **Exemption 3** | 时尚珠宝（非情色用途） | Rule 4 全部 |
| **Exemption 4** | 服饰/文化/宗教饰品（非 BDSM 营销） | Rule 4 全部 |
| **现有豁免** | 经典艺术作品（断臂维纳斯、大卫雕像） | ansa |
| **现有豁免** | 医学/教育用途 | ansa / uncomfortable |
| **现有豁免** | 正常泳装展示（无挑逗姿势） | vulgar |
| **现有豁免** | 正常内衣展示（无裸露特写） | vulgar |
| **现有豁免** | 人体模特服装展示（无挑逗角度） | vulgar |
| **现有豁免** | 平铺内衣展示（无人体穿着） | vulgar |

### 量化阈值

| 判定项 | 阈值 | 说明 |
|-------|------|------|
| 胸部暴露 | > 1/2 乳房 | 超过一半乳房暴露即违规 |
| 胸部特写 | ≥ 50% 画面 | 胸部占画面 50% 以上即违规 |
| 臀部暴露 | 大部分暴露 | 丁字裤等导致大部分臀部暴露 |
| 臀部全裸 | 全裸 + 臀沟全露 | 归为 ANSA |
| 微丁字裤 | 仅覆盖极小部分 | 归为 vulgar |

### 优先级调整

现有优先级保持不变：
1. **最高**: child_sexualization
2. **安全类**: ansa, politically_sensitive
3. **合规类**: prohibited, ipr, vulgar
4. **内容质量类**: low_quality, uncomfortable, novelty
5. **展示规范类**: black_white_edge, video_screenshot, watermark
6. **其他**: new_issue_supplement, other

### 置信度阈值

| 类型 | 最低置信度 | 说明 |
|-----|-----------|------|
| vulgar | ≥ 0.8 | 保持不变，需高置信度 |
| ansa | ≥ 0.5 | 保持不变 |
| child_sexualization | 任何置信度 | 零容忍，只要有嫌疑即标记人工审核 |

### 输出格式增强

保持现有 JSON 格式不变，`evidence` 字段增强要求：
- 必须引用具体违反的 PBR 规则编号（如 "违反 Rule 1.1.1 胸部过度暴露"）
- 必须描述具体的视觉元素（如 "模特穿着蕾丝内衣，约 2/3 乳房暴露"）
- 必须说明为何不符合豁免条件（如 "非书籍封面，不属于豁免范围"）

```json
{
  "has_problem": true,
  "problem_type": "vulgar",
  "confidence": 0.9,
  "is_new_type": false,
  "suggested_new_category": "",
  "reason": "模特穿着透视上衣，胸部大部分暴露，且拍摄角度为特写，符合 PBR Rule 1.1.1 和 Rule 2.10",
  "anomaly_score": 0.85,
  "evidence": {
    "image_elements": ["透视蕾丝上衣", "胸部暴露约 2/3", "特写拍摄角度"],
    "visual_issues": ["胸部过度暴露", "暗示性特写角度"],
    "context_analysis": ["违反 PBR Rule 1.1.1 胸部过度暴露", "违反 PBR Rule 2.10 暗示性拍摄角度", "不属于任何豁免规则"]
  }
}
```

## 实施计划

### 文件变更清单

1. **judgment_criteria.md**
   - 更新 Type 3 (vulgar) 判定标准，整合 PBR Rule 1-4 全部内容
   - 更新 Type 6 (ansa) 判定标准，补充 PBR 中直接裸露的内容
   - 更新 Type 16 (child_sexualization) 判定标准，补充性化卡通人物规则
   - 更新豁免规则部分，增加 PBR 的 4 项豁免
   - 更新常见误判案例，补充 PBR 中的正反案例
   - 更新版本历史

2. **juror_system_prompt_v4.0.txt**
   - 同步更新 Type 3、Type 6、Type 16 的判定标准
   - 同步更新豁免规则
   - 在输出要求中强调 PBR 规则编号引用

### 实施步骤

1. 更新 judgment_criteria.md 的 vulgar/ansa/child_sexualization 规则
2. 更新 juror_system_prompt_v4.0.txt 对应内容
3. 自检规则一致性
4. 提交到 GitHub
5. 验证工作流加载

## 风险与注意事项

### 风险
1. **Token 消耗增加**: 规则文本增加约 30%，可能导致推理成本上升
   - 缓解: 规则内容经过精简，保留核心判定要点
   
2. **规则冲突**: 现有规则与 PBR 规则可能存在不一致
   - 缓解: 以 PBR 规则为准，逐一比对整合

3. **JSON 人审文档缺失**: 用户提到的 JSON 人审文档未能定位
   - 缓解: 以 PBR 文档为主要依据，后续找到 JSON 文档后再补充

### 注意事项
1. vulgar 与 ansa 的区分必须严格：直接裸露→ansa，暗示/覆盖但暴露→vulgar
2. 豁免规则必须严格检查，避免误判正常商品
3. child_sexualization 保持零容忍政策，任何嫌疑都标记人工审核
4. 所有判定必须基于图片实际可见内容，禁止 AI 幻觉

## 验证标准

1. **规则完整性**: PBR 文档中所有规则均已整合到 v4.0 系统
2. **一致性**: judgment_criteria.md 与 juror_system_prompt_v4.0.txt 规则完全一致
3. **可追溯性**: 每条判定均可追溯到具体 PBR 规则编号
4. **量化性**: 所有可量化的判定标准均已明确阈值

## 版本历史

| 版本 | 日期 | 变更内容 | 作者 |
|------|------|---------|------|
| v1.0 | 2026-06-12 | 初始设计文档，完整 PBR 规则整合方案 | TikTok Shop EU 运营团队 |
