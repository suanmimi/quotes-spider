from spider import parse_page


def test_parse_page():
    with open("fixture.html", encoding = "utf-8") as f:
        html = f.read()
        rows = parse_page(html)
        assert len(rows) == 10
