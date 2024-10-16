class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # need a check array size of tiles to keep track of true and false
        # have a current string to append into set
        # need a set
        stringSet = set()
        count = [False] * (len(tiles))
        def addSet(string_set, tiles, current_string, check):

            for i in range(len(tiles)):
                if not check[i]:
                    current_string += tiles[i]
                    string_set.add(current_string)
                    check[i] = True
                    addSet(string_set, tiles, current_string, check)
                    check[i] = False
                    current_string = current_string[:-1]

        addSet(stringSet, tiles, "", count)
        return len(stringSet)
        