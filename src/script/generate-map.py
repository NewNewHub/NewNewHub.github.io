import json

def all_svg(width, height, locations):
  with open("./output.svg", "w") as svg:
    svg.write(f"<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{height}'>\n\n")
    svg.write("  "+background("gray")+"\n")
    svg.write(axis(width, height))
    for point in locations:
      x, y = tuple(point["position"].split(', '))
      svg.write(draw_item(x, y, point["name"], width, height))
    svg.write("\n</svg>")


def draw_item(locx, locy, name, width, height):
  cx = int(locx) // 2 + width // 2
  cy = int(locy) // 2 + height // 2
  return f"""
  <!-- {name} -->
  <circle cx="{cx}" cy="{cy}" r="5" fill="black"/>
  <text x="{cx+10}" y="{cy-10}" font-size="14" text-anchor="start" fill="white">{name}</text>
  """


def background(color):
  return f"<rect width='100%' height='100%' fill='{color}' />"


def axis(width, height):
  return f"""
  <!-- 经纬线 -->
  <line x1="{width//2}" x2="{width//2}" y1="0" y2="{height}" stroke="black"/>
  <line x1="0" x2="{width}" y1="{height//2}" y2="{height//2}" stroke="black"/>
  """


if __name__ == "__main__":
    width = 800
    height = 800
    with open("./locations.json", "r") as input:
      locations = json.load(input)
    all_svg(width, height, locations)