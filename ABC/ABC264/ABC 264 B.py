r, c = map(int, input().split())
g = ["###############",
     "#.............#",
     "#.###########.#",
     "#.#.........#.#",
     "#.#.#######.#.#",
     "#.#.........#.#",
     "#.#.#.###.#.#.#",
     "#.#.#.#.#.#.#.#",
     "#.#.#.###.#.#.#",
     "#.#.#.....#.#.#",
     "#.#.#######.#.#",
     "#.#.........#.#",
     "#.###########.#",
     "#...........#.#",
     "###############"]

print("black" if g[r - 1][c - 1] == "#" else "white")