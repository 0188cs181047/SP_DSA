def generate_pattern(rows, col):
  if not isinstance(rows, int) or not isinstance(col, int) or rows <= 0 or col <= 0:
    raise ValueError("rows and col must be postitive integers")
  return [
      ['X' if (row + col) % 2 == 0 else '0' for col in range(col)]
      for row in range(rows)
    ]

print(generate_pattern(3, 4))