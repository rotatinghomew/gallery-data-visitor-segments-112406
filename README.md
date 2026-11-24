# 数字展行为记录和体验模式资料

以下台账为合成数据，不涉及真实访客、供应商或展馆。CSV 采用 UTF-8，首行为字段名，空字段代表源资料未给出。标识仅在字段明示的实体范围内使用。`data/agreements.json` 是当期业务方提供的运营资料，`data/formats.json` 记录文件列顺序和确定的外键引用。

- `data/sessions.csv` 记录按馆期和观察窗口记参观机会。列为 `session`、`venue`、`period`、`participants`、`identity`、`minutes`、`observation`。
- `data/sensor_events.csv` 记录按真实传感器和可见体验方式记观察。列为 `session`、`ordinal`、`minute`、`signal`、`mode`、`participant`、`step`。
- `data/profile.csv` 记录当馆期可见信号、开放模式及数据使用范围。venue 与 period 共同定位一条记录。列为 `venue`、`period`、`visible`、`available`、`licence_group`、`partition`。
- `data/interviews.csv` 记录独立访谈中的深访、协同和辅助使用线索，三项分别为 0 或 1。列为 `session`、`reviewer`、`actual_depth`、`actual_joint`、`assistance`、`source`、`received_period`。
- `data/service_orders.csv` 记录需要保留的功能和可比群组门槛。列为 `order`、`venue`、`period`、`mode`、`committed`、`eligible_groups`、`status`。
- `data/change_candidates.csv` 记录可并存相邻期开法、可见的传感器及是否有语音和对比读屏。列为 `case`、`venue`、`period`、`retain`、`visible`、`supports_aux`。
- `data/live_receipt.csv` 记录模式采用结果。后续采集能力按这条回执而非候选假定。列为 `record`、`case`、`period`、`venue`、`sensors`、`actual_mode`、`received`。

使用 Python 3.11，无第三方依赖。用 `python3 -m unittest discover -s tests -v` 核对文件的可读性、列结构和确定引用，源文件保持只读。
