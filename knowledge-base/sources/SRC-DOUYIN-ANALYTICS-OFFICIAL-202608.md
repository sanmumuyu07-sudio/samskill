---
source_id: SRC-DOUYIN-ANALYTICS-OFFICIAL-202608
title: 抖音官方数据字段按业务场景和产品页面定义
source_type: 平台官方文档组
evidence_grade: A
verification_status: 已核官方页面
checked_at: 2026-08-12
recheck_at: 2026-09-12
---

# 抖音官方数据字段按业务场景和产品页面定义

## 官方来源

- 视频数据接入方案：https://open.douyin.com/platform/resource/docs/ability/open-data/video-data-solution
- 经营分析视频分析：https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/operation/data/management-analysis/analytics
- 生活服务交易分析：https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/operation/data/data-center/ta/trade
- 查询特定视频数据：https://open.douyin.com/platform/resource/docs/openapi/video-management/douyin/search-video/video-data/

## 能支持什么

- 不同数据产品提供播放、互动、流量来源、入口点击与交易漏斗等不同字段。
- 指标范围、更新时间、授权和归因窗口依具体产品而定。
- 平台提供自身周期、行业或大盘对比时，应优先使用同页面给出的口径。

## 不能支持什么

- 所有创作者后台字段完全一致。
- 一个固定完播或互动阈值适合所有账号。
- 某指标低可以唯一定位到一个文案原因。

## 进入叁木系统

每次复盘先保存字段定义、数据页面、采集时间、统计周期与业务场景，再进行比较；平台页面变化时更新字典，不保留过期“权重公式”。
