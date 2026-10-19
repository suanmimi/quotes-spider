![CI](https://github.com/suanmimi/quotes-spider/actions/workflows/ci.yml/badge.svg)
功能：爬 quotes.toscrape.com，取名句和作者，存 JSON
用法：pip install -r requirements.txt → python spider.py
要点：
requests + BeautifulSoup 解析
ThreadPoolExecutor 并发，12.3s → 1.5s
404 兜底 + 分批探测，未知页数自动停
pytest 覆盖解析逻辑，ruff + mypy + GitHub Actions
