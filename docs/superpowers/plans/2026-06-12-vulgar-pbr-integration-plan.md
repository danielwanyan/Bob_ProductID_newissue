# v4.0 低俗/色情识别规则 PBR 整合实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 整合 PBR 文档的完整低俗/色情判定规则到 v4.0 系统的 judgment_criteria.md 和 juror_system_prompt_v4.0.txt 中，实现与官方 PBR 标准 100% 对齐。

**Architecture:** 保持现有 19 类型体系不变，仅增强 vulgar (Type 3)、ansa (Type 6)、child_sexualization (Type 16) 三个类型的判定标准，补充 PBR 规则的量化阈值和豁免条款。

**Tech Stack:** Markdown (规则文档), GitHub (规则托管), Aicolate (工作流执行)

---

## 文件结构

| 文件 | 操作 | 说明 |
|------|------|------|
| `/Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md` | 修改 | 更新 Type 3、Type 6、Type 16 判定标准，补充 PBR 规则和豁免条款 |
| `/Users/bytedance/Bob_ProductID_newissue/juror_system_prompt_v4.0.txt` | 修改 | 同步更新对应类型的判定标准 |

---

## Task 1: 更新 judgment_criteria.md - Type 3 (vulgar) 判定标准

**Files:**
- Modify: `/Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md:44-68`

- [ ] **Step 1: 读取当前 Type 3 内容**

```bash
# 已读取，当前内容位于第 44-68 行
```

- [ ] **Step 2: 替换 Type 3 判定标准为 PBR 整合版本**

将原 Type 3 内容（第 44-68 行）替换为：

```markdown
### Type 3: vulgar 泛低俗 (Pan Vulgar)
**定义:** 主图包含性暗示、过度暴露或挑逗性内容（非直接裸露），符合 PBR (Policy, Business, Rule) 低俗判定标准

**判定标准 (满足任一即可):**

#### A. 身体暴露类 (PBR Rule 1)
1. **胸部过度暴露 (Rule 1.1.1)**: 内衣展示中超过 1/2 乳房暴露，或具有性暗示
2. **胸部特写 (Rule 1.1.2)**: 胸部占画面 ≥ 50% 的特写镜头
3. **乳头凸起 (Rule 1.1.3)**: 女性乳头透过衣物明显凸起
4. **乳贴/隐形文胸 (Rule 1.1.4)**: 模特佩戴粘性乳贴或乳头遮盖物
5. **丁字裤/极小内裤 (Rule 1.2.2)**: 丁字裤或极小内裤导致臀部大部分暴露
6. **透视装露臀沟 (Rule 1.2.3)**: 透视/蕾丝/网眼衣物露出完整臀沟
7. **上臀沟暴露 (Rule 1.2.4)**: 衣物露出臀沟顶部
8. **微丁字裤 (Rule 1.3.1)**: "微丁字裤"或其他极小覆盖度的内衣（男女均适用）
9. **开裆内衣 (Rule 1.3.2)**: 开裆内衣或下装穿在模特/假人身上，或下方有其他衣物
10. **背部全裸 (Rule 1.4)**: 从后方拍摄的上半身全裸（腰部以上无衣物）

#### B. 性暗示行为类 (PBR Rule 2)
1. **暗示性弯腰 (Rule 2.1)**: 以暗示或性化方式弯腰
2. **四肢着地 (Rule 2.2)**: 以暗示或性化方式四肢着地
3. **暗示性跪姿 (Rule 2.3)**: 以暗示或性化方式跪坐
4. **分腿姿势 (Rule 2.4)**: 以暗示或性化方式张开双腿
5. **暗示性躺卧 (Rule 2.5)**: 以性化或暗示方式躺卧
6. **脱衣/半脱状态 (Rule 2.6)**: 任何性暗示的脱衣动作或处于脱衣状态
7. **性表情 (Rule 2.7)**: 性化面部表情（高潮表情、翻白眼等）
8. **接吻 (Rule 2.8)**: 两人接吻（无论是否穿衣）
9. **抚摸 (Rule 2.9)**: 抚摸自己或他人的胸部、阴部或臀部
10. **暗示性拍摄角度 (Rule 2.10)**: 服装、场景和拍摄角度组合产生性暗示或恋物聚焦

#### C. 低俗商品类 (PBR Rule 3)
1. **人脸/阳具图案内裤 (Rule 3.1)**: 男士内裤印有人脸或阳具符号
2. **性角色扮演制服 (Rule 3.2)**: 性角色扮演制服（学校、女仆、警察、护士等）
3. **透视上衣 (Rule 3.3)**: 透视或网眼上衣经数字修改去除乳头，或乳头本应可见
4. **生殖器造型商品 (Rule 3.4)**: 商品造型类似生殖器（阴茎、睾丸、乳房、阴道、阴毛、肛门）
5. **剪影/卡通/简笔画性姿势 (Rule 3.5)**: 剪影、卡通或简笔画处于性姿势
6. **Barry Wood 商品 (Rule 3.6)**: Barry Wood 相关商品（裸体/极少衣物）
7. **旗帜模特 (Rule 3.7)**: 旗帜/横幅上印有比基尼或极少衣物的模特
8. **海报/服装/专辑少衣模特 (Rule 3.8)**: 海报、服装或专辑上印有比基尼、内衣、赤裸上身或少衣模特
9. **性感动漫贴纸 (Rule 3.9)**: 动漫/卡通人物处于性暗示姿势、过度性化、性暗示表情或夸张胸部/臀部
10. **生殖器性暗示/隐喻 (Rule 3.10)**: 对生殖器的性暗示或隐喻（包括阳具暗示，如黄瓜、茄子、蘑菇等）

#### D. 情色饰品类 (PBR Rule 4)
1. **私密部位珠宝 (Rule 4.1)**: 专为私密部位设计的珠宝（乳环、阴环、身体链等）
2. **情色束身带 (Rule 4.2)**: 情色美学的身体配饰（笼式胸罩、开杯束带、裸身束带等）
3. **BDSM/恋物配饰 (Rule 4.3)**: 明确用于 BDSM、恋物活动或性角色扮演的配饰（O 形环项圈、牵引绳、束缚手铐等）

**明确排除项 (NOT vulgar):**
- ❌ 正常泳装展示 (比基尼、泳衣) - 无刻意性挑逗姿势
- ❌ 正常内衣/家居服展示 - 无私密部位裸露特写，无 >1/2 乳房暴露
- ❌ 人体模特服装展示 - 无挑逗性角度或姿势
- ❌ 平铺内衣展示 - 无人体穿着
- ❌ 书籍封面接吻 - 浪漫小说等书籍封面的接吻场景 (Exemption 1)
- ❌ 非性化提衣动作 - 非实际脱衣的非性化提衣 (Exemption 2)
- ❌ 时尚珠宝 - 作为时尚配饰营销的身体链、腰链等，模特穿着适当，无性暗示 (Exemption 3)
- ❌ 服饰/文化/宗教饰品 - 万圣节、cosplay、戏剧、文化/宗教用途的饰品，无 BDSM 术语或恋物营销 (Exemption 4)

**关键区分点 (vulgar vs ansa):**
- ✅ vulgar: 暗示性内容、覆盖但过度暴露、性姿势、性化商品（无直接裸露）
- ❌ ansa: 私密部位直接裸露（乳头、生殖器、肛门）、露骨性动作、成人情趣用品露骨展示

**人审反馈案例:**
- "低俗: 模特穿着透视内衣，约 2/3 乳房暴露，违反 PBR Rule 1.1.1"
- "低俗: 模特以性暗示方式弯腰，违反 PBR Rule 2.1"
- "低俗: 内裤印有女性人脸图案，违反 PBR Rule 3.1"
- "没问题: 认为为正常泳装展示，未见明显性挑逗姿势或刻意凸显敏感部位。"
- "没问题: 图片为正常的人体模特对服装进行展示，虽然服装部分为蕾丝材质，但没有裸露私密部位，姿势和角度也未表现出明显的性挑逗"

**置信度要求:** ≥ 0.8 才判定
```

- [ ] **Step 3: 验证文件修改正确**

```bash
# 检查文件是否包含新的 PBR 规则编号
grep -n "Rule 1.1.1" /Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md
# Expected: 找到匹配行
```

- [ ] **Step 4: 提交更改**

```bash
cd /Users/bytedance/Bob_ProductID_newissue
git add judgment_criteria.md
git commit -m "feat: update vulgar (Type 3) criteria with full PBR Rule 1-4 integration"
```

---

## Task 2: 更新 judgment_criteria.md - Type 6 (ansa) 判定标准

**Files:**
- Modify: `/Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md:131-146`

- [ ] **Step 1: 读取当前 Type 6 内容**

```bash
# 已读取，当前内容位于第 131-146 行
```

- [ ] **Step 2: 替换 Type 6 判定标准为 PBR 整合版本**

将原 Type 6 内容（第 131-146 行）替换为：

```markdown
### Type 6: ansa 成人内容 (Adult Nudity and Sexual Activities)
**定义:** 露骨的成人色情内容 (区别于 vulgar 的暗示性内容)

**判定标准 (满足任一即可):**

#### A. 直接裸露 (PBR Rule 1 相关)
1. **全裸臀部+臀沟 (Rule 1.2.1)**: 同时展示全裸臀部和完整臀沟
2. **乳头直接裸露**: 女性乳头完全裸露（非透过衣物）
3. **生殖器直接裸露**: 男性或女性生殖器完全裸露
4. **肛门直接裸露**: 肛门完全裸露

#### B. 露骨性动作 (PBR Rule 3.11)
1. 露骨的性交动作展示
2. 露骨的自慰动作展示
3. 其他露骨性活动展示

#### C. 成人情趣用品露骨展示 (PBR Rule 3.11)
1. 成人情趣用品的露骨使用展示
2. 性玩具的露骨展示

**明确排除项 (NOT ansa):**
- ❌ 经典艺术作品（断臂维纳斯、大卫雕像等）
- ❌ 医学/教育用途（解剖图、临床影像）
- ❌ 非露骨的性暗示（归为 vulgar）
- ❌ 覆盖但过度暴露（归为 vulgar）

**关键:** 需结合语境判断 — 艺术/医学用途 vs 色情意图

**PBR 说明:** Rule 3.11 (Prohibited Products - ANSA and Adult Products) 主要针对人审，但 AI 模型可参考其判定标准识别露骨成人内容。
```

- [ ] **Step 3: 验证文件修改正确**

```bash
grep -n "全裸臀部+臀沟" /Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md
# Expected: 找到匹配行
```

- [ ] **Step 4: 提交更改**

```bash
cd /Users/bytedance/Bob_ProductID_newissue
git add judgment_criteria.md
git commit -m "feat: update ansa (Type 6) criteria with PBR Rule 1.2.1 and Rule 3.11"
```

---

## Task 3: 更新 judgment_criteria.md - Type 16 (child_sexualization) 判定标准

**Files:**
- Modify: `/Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md:256-271`

- [ ] **Step 1: 读取当前 Type 16 内容**

```bash
# 已读取，当前内容位于第 256-271 行
```

- [ ] **Step 2: 替换 Type 16 判定标准为 PBR 整合版本**

将原 Type 16 内容（第 256-271 行）替换为：

```markdown
### Type 16: child_sexualization 儿童性化（最高优先级）
**定义:** 涉及儿童的性化内容，包括性化的卡通人物

**判定原则: 任何性语境都属于严重违规**

**判定标准 (满足任一即可):**

#### A. 儿童模特性化
1. 儿童模特以性化方式展示
2. 儿童穿着不适当的成人化服装
3. 儿童姿势或角度具有性暗示
4. 任何性暗示、成人化性语境或性化构图（无论是否裸露）

#### B. 性化卡通人物 (PBR Rule 4 Child Safety)
1. **性化卡通人物 (Rule 4.1.1)**: 卡通人物被性化展示
2. 动漫/卡通人物以儿童形象出现但具有性化特征
3. 儿童形象的卡通人物处于性暗示姿势或场景

**零容忍规则:**
- ⚠️ 无论置信度高低，只要有嫌疑即标记需人工审核
- ⚠️ 优先级：高于 ANSA、politically_sensitive 等所有安全类
```

- [ ] **Step 3: 验证文件修改正确**

```bash
grep -n "性化卡通人物" /Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md
# Expected: 找到匹配行
```

- [ ] **Step 4: 提交更改**

```bash
cd /Users/bytedance/Bob_ProductID_newissue
git add judgment_criteria.md
git commit -m "feat: update child_sexualization (Type 16) with PBR Rule 4 child safety"
```

---

## Task 4: 更新 judgment_criteria.md - 豁免规则和常见误判案例

**Files:**
- Modify: `/Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md:352-371`

- [ ] **Step 1: 读取当前常见误判案例内容**

```bash
# 已读取，当前内容位于第 352-371 行
```

- [ ] **Step 2: 在常见误判案例表格中添加 PBR 相关案例**

在原表格（第 354-370 行）中添加以下行（在现有行之后）：

```markdown
| 模特佩戴乳贴 | vulgar | 正常商品 | 乳贴产品展示，如无人体模特则不属于低俗 |
| 丁字裤正常展示 | vulgar | 正常商品 | 如无私密部位裸露或性暗示姿势，需结合上下文 |
| 书籍封面接吻 | vulgar | 正常商品 | Exemption 1: 书籍封面接吻场景豁免 |
| 时尚身体链 | vulgar | 正常商品 | Exemption 3: 时尚珠宝无性暗示营销豁免 |
| 万圣节项圈 | vulgar | 正常商品 | Exemption 4: 服饰/文化/宗教饰品豁免 |
| 正常护士服 | vulgar | 正常商品 | 非性化的职业服装不属于性角色扮演制服 |
| 正常动漫人物 | vulgar | 正常商品 | 无性化特征的普通动漫人物不属于违规 |
```

- [ ] **Step 3: 验证文件修改正确**

```bash
grep -n "Exemption 1" /Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md
# Expected: 找到匹配行
```

- [ ] **Step 4: 提交更改**

```bash
cd /Users/bytedance/Bob_ProductID_newissue
git add judgment_criteria.md
git commit -m "feat: add PBR exemption cases to common misjudgment table"
```

---

## Task 5: 更新 judgment_criteria.md - 版本历史

**Files:**
- Modify: `/Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md:374-381`

- [ ] **Step 1: 读取当前版本历史**

```bash
# 已读取，当前内容位于第 374-381 行
```

- [ ] **Step 2: 在版本历史表格顶部添加新版本记录**

在版本历史表格中添加新行（在 v4.0 行之前）：

```markdown
| v4.1 | 2026-06-12 | 整合 PBR 低俗规则：vulgar 补充 Rule 1-4 完整判定标准（身体暴露、性暗示行为、低俗商品、情色饰品）；ansa 补充 Rule 1.2.1 和 Rule 3.11；child_sexualization 补充 Rule 4 儿童安全；新增 4 项豁免规则；补充量化阈值（1/2 乳房、50% 画面等） |
```

同时更新页面顶部的版本信息（第 4-7 行）：

```markdown
## 版本信息
- 版本: v4.1
- 更新日期: 2026-06-12
- 维护者: TikTok Shop EU 运营团队
- 变更说明: 从 v3.1 的 8 种类型扩展到 v4.0 的 19 种类型；v4.1 整合 PBR 低俗规则，补充完整判定标准、量化阈值和豁免条款
```

- [ ] **Step 3: 验证文件修改正确**

```bash
grep -n "v4.1" /Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md
# Expected: 至少找到 2 处匹配（版本信息 + 版本历史）
```

- [ ] **Step 4: 提交更改**

```bash
cd /Users/bytedance/Bob_ProductID_newissue
git add judgment_criteria.md
git commit -m "feat: update version to v4.1 with PBR integration changelog"
```

---

## Task 6: 同步更新 juror_system_prompt_v4.0.txt - Type 3 (vulgar)

**Files:**
- Modify: `/Users/bytedance/Bob_ProductID_newissue/juror_system_prompt_v4.0.txt:43-54`

- [ ] **Step 1: 读取当前 Type 3 内容**

```bash
# 已读取，当前内容位于第 43-54 行
```

- [ ] **Step 2: 替换 Type 3 判定标准（与 judgment_criteria.md 保持一致）**

将原 Type 3 内容（第 43-54 行）替换为：

```markdown
### Type 3: vulgar 泛低俗 (Pan Vulgar)
**定义:** 主图包含性暗示、过度暴露或挑逗性内容（非直接裸露），符合 PBR 低俗判定标准
**判定标准 (满足任一即可):**
#### A. 身体暴露类 (PBR Rule 1)
- 胸部过度暴露 (Rule 1.1.1): 内衣展示中超过 1/2 乳房暴露
- 胸部特写 (Rule 1.1.2): 胸部占画面 ≥ 50%
- 乳头凸起 (Rule 1.1.3): 乳头透过衣物明显凸起
- 乳贴/隐形文胸 (Rule 1.1.4): 模特佩戴粘性乳贴
- 丁字裤/极小内裤 (Rule 1.2.2): 臀部大部分暴露
- 透视装露臀沟 (Rule 1.2.3): 透视衣物露出完整臀沟
- 上臀沟暴露 (Rule 1.2.4): 露出臀沟顶部
- 微丁字裤 (Rule 1.3.1): 极小覆盖度的内衣
- 开裆内衣 (Rule 1.3.2): 开裆内衣穿在模特/假人身上
- 背部全裸 (Rule 1.4): 上半身背部全裸
#### B. 性暗示行为类 (PBR Rule 2)
- 暗示性弯腰 (Rule 2.1)、四肢着地 (Rule 2.2)、跪姿 (Rule 2.3)、分腿 (Rule 2.4)、躺卧 (Rule 2.5)
- 脱衣/半脱状态 (Rule 2.6)、性表情 (Rule 2.7)、接吻 (Rule 2.8)、抚摸 (Rule 2.9)、暗示性拍摄角度 (Rule 2.10)
#### C. 低俗商品类 (PBR Rule 3)
- 人脸/阳具图案内裤 (Rule 3.1)、性角色扮演制服 (Rule 3.2)、透视上衣 (Rule 3.3)
- 生殖器造型商品 (Rule 3.4)、剪影/卡通性姿势 (Rule 3.5)、Barry Wood (Rule 3.6)
- 旗帜模特 (Rule 3.7)、海报/服装少衣模特 (Rule 3.8)、性感动漫 (Rule 3.9)、生殖器隐喻 (Rule 3.10)
#### D. 情色饰品类 (PBR Rule 4)
- 私密部位珠宝 (Rule 4.1)、情色束身带 (Rule 4.2)、BDSM/恋物配饰 (Rule 4.3)
**明确排除项:**
- ❌ 正常泳装/内衣展示（无挑逗）
- ❌ 平铺内衣展示（无人体）
- ❌ 书籍封面接吻 (Exemption 1)
- ❌ 非性化提衣 (Exemption 2)
- ❌ 时尚珠宝 (Exemption 3)
- ❌ 服饰/文化/宗教饰品 (Exemption 4)
**置信度要求:** ≥ 0.8
```

- [ ] **Step 3: 验证文件修改正确**

```bash
grep -n "Rule 1.1.1" /Users/bytedance/Bob_ProductID_newissue/juror_system_prompt_v4.0.txt
# Expected: 找到匹配行
```

- [ ] **Step 4: 提交更改**

```bash
cd /Users/bytedance/Bob_ProductID_newissue
git add juror_system_prompt_v4.0.txt
git commit -m "feat: sync juror prompt Type 3 (vulgar) with PBR rules"
```

---

## Task 7: 同步更新 juror_system_prompt_v4.0.txt - Type 6 (ansa)

**Files:**
- Modify: `/Users/bytedance/Bob_ProductID_newissue/juror_system_prompt_v4.0.txt:108-118`

- [ ] **Step 1: 读取当前 Type 6 内容**

```bash
# 已读取，当前内容位于第 108-118 行
```

- [ ] **Step 2: 替换 Type 6 判定标准（与 judgment_criteria.md 保持一致）**

将原 Type 6 内容（第 108-118 行）替换为：

```markdown
### Type 6: ansa 成人内容 (Adult Nudity and Sexual Activities)
**定义:** 露骨的成人色情内容 (区别于 vulgar 的暗示性内容)
**判定标准:**
- 全裸臀部+臀沟 (Rule 1.2.1): 同时展示全裸臀部和完整臀沟
- 私密部位直接裸露（乳头、生殖器、肛门）
- 露骨性动作展示
- 成人情趣用品的露骨展示
**明确排除项:**
- ❌ 经典艺术作品（断臂维纳斯、大卫雕像等）
- ❌ 医学/教育用途（解剖图、临床影像）
- ❌ 非露骨的性暗示（归为 vulgar）
**关键:** 需结合语境判断 — 艺术/医学用途 vs 色情意图
```

- [ ] **Step 3: 验证文件修改正确**

```bash
grep -n "全裸臀部+臀沟" /Users/bytedance/Bob_ProductID_newissue/juror_system_prompt_v4.0.txt
# Expected: 找到匹配行
```

- [ ] **Step 4: 提交更改**

```bash
cd /Users/bytedance/Bob_ProductID_newissue
git add juror_system_prompt_v4.0.txt
git commit -m "feat: sync juror prompt Type 6 (ansa) with PBR rules"
```

---

## Task 8: 同步更新 juror_system_prompt_v4.0.txt - Type 16 (child_sexualization)

**Files:**
- Modify: `/Users/bytedance/Bob_ProductID_newissue/juror_system_prompt_v4.0.txt:202-212`

- [ ] **Step 1: 读取当前 Type 16 内容**

```bash
# 已读取，当前内容位于第 202-212 行
```

- [ ] **Step 2: 替换 Type 16 判定标准（与 judgment_criteria.md 保持一致）**

将原 Type 16 内容（第 202-212 行）替换为：

```markdown
### Type 16: child_sexualization 儿童性化（最高优先级）
**定义:** 涉及儿童的性化内容，包括性化的卡通人物
**判定原则: 任何性语境都属于严重违规**
**判定标准:**
- 儿童模特以性化方式展示
- 儿童穿着不适当的成人化服装
- 儿童姿势或角度具有性暗示
- 任何性暗示、成人化性语境或性化构图（无论是否裸露）
- 性化卡通人物 (PBR Rule 4.1.1): 卡通人物被性化展示
**零容忍规则:**
- ⚠️ 无论置信度高低，只要有嫌疑即标记需人工审核
- ⚠️ 优先级：高于 ANSA、politically_sensitive 等所有安全类
```

- [ ] **Step 3: 验证文件修改正确**

```bash
grep -n "性化卡通人物" /Users/bytedance/Bob_ProductID_newissue/juror_system_prompt_v4.0.txt
# Expected: 找到匹配行
```

- [ ] **Step 4: 提交更改**

```bash
cd /Users/bytedance/Bob_ProductID_newissue
git add juror_system_prompt_v4.0.txt
git commit -m "feat: sync juror prompt Type 16 (child_sexualization) with PBR rules"
```

---

## Task 9: 同步更新 juror_system_prompt_v4.0.txt - 特别注意和输出要求

**Files:**
- Modify: `/Users/bytedance/Bob_ProductID_newissue/juror_system_prompt_v4.0.txt:247-254`

- [ ] **Step 1: 读取当前特别注意部分**

```bash
# 已读取，当前内容位于第 247-254 行
```

- [ ] **Step 2: 更新 vulgar 判定注意事项，添加 PBR 规则引用要求**

将原第 248 行：
```markdown
- **vulgar 判定需谨慎**：正常泳装、内衣展示不属于低俗，仅在有明确性挑逗时才判定，置信度≥0.8
```

替换为：
```markdown
- **vulgar 判定需谨慎**：正常泳装、内衣展示不属于低俗，仅在符合 PBR 规则时才判定，置信度≥0.8；必须在 evidence 中引用具体 PBR 规则编号
- **vulgar vs ansa 区分**：直接裸露→ansa，暗示/覆盖但过度暴露→vulgar；全裸臀部+臀沟→ansa
- **豁免规则检查**：判定 vulgar 前必须检查是否符合 4 项 PBR 豁免条件
```

- [ ] **Step 3: 验证文件修改正确**

```bash
grep -n "PBR 规则编号" /Users/bytedance/Bob_ProductID_newissue/juror_system_prompt_v4.0.txt
# Expected: 找到匹配行
```

- [ ] **Step 4: 提交更改**

```bash
cd /Users/bytedance/Bob_ProductID_newissue
git add juror_system_prompt_v4.0.txt
git commit -m "feat: update juror prompt special notes with PBR rule citation requirement"
```

---

## Task 10: 规则一致性自检和推送 GitHub

**Files:**
- Verify: `/Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md`
- Verify: `/Users/bytedance/Bob_ProductID_newissue/juror_system_prompt_v4.0.txt`

- [ ] **Step 1: 验证两个文件规则一致性**

```bash
# 检查两个文件都包含相同的 PBR 规则
echo "=== judgment_criteria.md PBR rules ==="
grep -c "Rule 1\." /Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md
grep -c "Rule 2\." /Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md
grep -c "Rule 3\." /Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md
grep -c "Rule 4\." /Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md
grep -c "Exemption" /Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md

echo "=== juror_system_prompt_v4.0.txt PBR rules ==="
grep -c "Rule 1\." /Users/bytedance/Bob_ProductID_newissue/juror_system_prompt_v4.0.txt
grep -c "Rule 2\." /Users/bytedance/Bob_ProductID_newissue/juror_system_prompt_v4.0.txt
grep -c "Rule 3\." /Users/bytedance/Bob_ProductID_newissue/juror_system_prompt_v4.0.txt
grep -c "Rule 4\." /Users/bytedance/Bob_ProductID_newissue/juror_system_prompt_v4.0.txt
grep -c "Exemption" /Users/bytedance/Bob_ProductID_newissue/juror_system_prompt_v4.0.txt

# Expected: 两个文件的 Rule 1-4 和 Exemption 数量一致
```

- [ ] **Step 2: 验证版本号一致性**

```bash
grep "版本:" /Users/bytedance/Bob_ProductID_newissue/judgment_criteria.md | head -1
# Expected: 版本: v4.1
```

- [ ] **Step 3: 推送到 GitHub**

```bash
cd /Users/bytedance/Bob_ProductID_newissue
git push origin main
```

- [ ] **Step 4: 提交最终验证**

```bash
cd /Users/bytedance/Bob_ProductID_newissue
git add docs/superpowers/specs/2026-06-12-vulgar-pbr-integration-design.md
git add docs/superpowers/plans/2026-06-12-vulgar-pbr-integration-plan.md
git commit -m "docs: add PBR integration design doc and implementation plan"
git push origin main
```

---

## 计划自检

### 1. 设计文档覆盖检查

| 设计文档章节 | 对应任务 | 覆盖状态 |
|-------------|---------|---------|
| 规则映射表 (Rule 1-4) | Task 1, 6 | ✅ 完整覆盖 |
| 豁免规则整合 | Task 1, 4, 6 | ✅ 完整覆盖 |
| 量化阈值 | Task 1, 6 | ✅ 完整覆盖 |
| ansa 判定标准更新 | Task 2, 7 | ✅ 完整覆盖 |
| child_sexualization 儿童安全 | Task 3, 8 | ✅ 完整覆盖 |
| 输出格式增强 (PBR 规则引用) | Task 9 | ✅ 完整覆盖 |
| 版本历史更新 | Task 5 | ✅ 完整覆盖 |
| 一致性验证 | Task 10 | ✅ 完整覆盖 |

### 2. 占位符检查
- ✅ 无 TBD/TODO
- ✅ 所有代码步骤均有完整代码块
- ✅ 所有命令均有预期输出
- ✅ 无"类似 Task N"等模糊描述

### 3. 类型一致性检查
- ✅ 所有 PBR 规则编号在两个文件中一致
- ✅ vulgar/ansa/child_sexualization 类型名称在所有任务中一致
- ✅ Exemption 编号在所有任务中一致

---

## 执行选择

Plan complete and saved to `docs/superpowers/plans/2026-06-12-vulgar-pbr-integration-plan.md`. Two execution options:

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

**Which approach?**
