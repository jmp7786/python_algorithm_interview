from typing import List
n = int(input())

class NQueens:
    def solve(self, n: int) -> List[List[str]]:
        self.__results = []
        self.__col_set = set()  # column duplicates
        self.__diag_set1 = set()  # row-col duplicates
        self.__diag_set2 = set()  # row+col duplicates
        self.__n = n  # length

        for x in range(n):
            self.__bt(0, x, [])

        return self.__results

    # python str is immutable
    def __create_str_row(self, col: int) -> str:
        str_list = ['.'] * self.__n
        str_list[col] = 'Q'
        return ''.join(str_list)

    def __bt(self, row: int, col: int, board: List[str]):
        # exit conditions
        if row == self.__n or col == self.__n:
            return
        if col in self.__col_set:
            return
        diag1_info = row - col
        diag2_info = row + col
        if diag1_info in self.__diag_set1:
            return
        if diag2_info in self.__diag_set2:
            return

            # process
        str_line = self.__create_str_row(col)
        board.append(str_line)

        if len(board) == self.__n:
            self.__results.append(board.copy())
            board.pop()
            return

        # duplicates sets
        self.__col_set.add(col)
        self.__diag_set1.add(diag1_info)
        self.__diag_set2.add(diag2_info)

        # recursive calls
        for x in range(self.__n):
            self.__bt(row + 1, x, board)

            # duplicates sets pop
        self.__diag_set2.remove(diag2_info)
        self.__diag_set1.remove(diag1_info)
        self.__col_set.remove(col)
        board.pop()


nQsolver = NQueens().solve(n)

print(nQsolver)