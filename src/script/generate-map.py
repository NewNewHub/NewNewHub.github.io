import json
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_DIR = os.path.join(FILE_DIR, "..", ".vuepress", "public", "assets", "images")


def all_svg(
    width: int | float,
    height: int | float,
    locations: dict[str, dict[str, tuple[int | float, int | float]]],
):
    with open(os.path.join(SAVE_DIR, "transportation.svg"), "w") as svg:
        svg.write(
            f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">\n"""
        )
        svg.write(background("gray"))
        svg.write(axis(width, height))
        num_groups = len(locations)
        for i, (group, points) in enumerate(locations.items()):
            svg.write(open_group(group, i, num_groups, width, height))
            for label, coord in points.items():
                x, y = coord[:2]
                svg.write(draw_item(x, y, label, width, height))
            svg.write(close_group())
        svg.write(styles(list(locations.keys())))
        svg.write("</svg>\n")


def open_group(
    group: str, idx: int, total: int, width: int | float, height: int | float
):
    cx = int(width / (total + 1) * (idx + 1))
    cy = int(height / 20)
    return f"""
  <!-- {group} -->
  <text x="{cx}" y="{cy}" font-size="18" text-anchor="middle">{group}</text>
  <g id="{group}" opacity="0.1">
    <text x="{cx}" y="{cy}" font-size="18" text-anchor="middle">{group}</text>\n"""


def close_group():
    return "  </g>\n"


def styles(groups: list[str]):
    group_styles = " ".join([f"#{group}:hover{{opacity:1}}" for group in groups])
    default_styles = (
        "text{fill:white;} circle{fill:black;} *{transition: all .5s ease-out;}"
    )
    return f"""
  <style>
  {group_styles} {default_styles}
  </style>\n"""


def draw_item(
    locx: int | float,
    locy: int | float,
    name: str,
    width: int | float,
    height: int | float,
):
    cx = locx // 2 + width // 2
    cy = locy // 2 + height // 2
    return f"""
    <!-- {name} -->
    <circle cx="{cx}" cy="{cy}" r="5" />
    <text x="{cx+10}" y="{cy-10}" font-size="14">{name}</text>\n"""


def background(color: str):
    return f"""  <rect width="100%" height="100%" fill="{color}" />\n"""


def axis(width: int | float, height: int | float):
    return f"""
  <!-- 经纬线 -->
  <line x1="{width//2}" x2="{width//2}" y1="0" y2="{height}" stroke="black" />
  <line x1="0" x2="{width}" y1="{height//2}" y2="{height//2}" stroke="black" />\n"""


def sort_locations_by_group(places: list[dict[str, str]]):
    sorted_dict: dict[str, dict[str, tuple[int | float, int | float]]] = {}
    for e in places:
        if e["group"] not in sorted_dict:
            sorted_dict[e["group"]] = {}
        sorted_dict[e["group"]][e["name"]] = tuple(
            int(x) for x in e["position"].split(", ")
        )
    return sorted_dict


if __name__ == "__main__":
    width = 800
    height = 800
    with open("./locations.json", "r") as input:
        locations = json.load(input)
    locations_by_group = sort_locations_by_group(locations)
    all_svg(width, height, locations_by_group)
