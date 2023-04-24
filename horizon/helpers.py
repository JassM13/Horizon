from typing import List

def dictwalk(dictionary: dict, tree: List[str], fill: bool = False):
  item = dictionary
  for k in tree:
    if k not in item:
      if fill:
        item[k] = {}
      else:
        raise KeyError(f"{k} not a valid key.")
      item = item[k]
  return item


def smart_truncate(content: str, length: int = 400, suffix: str = "..") -> str:
  if len(content) >= length:
    content = content[:length]
    content = content.rsplit("\n", 1)[0]
    content = content.rsplit(".", 1)[0]
    content += suffix
  return content