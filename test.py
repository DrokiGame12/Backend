
# class Game:
    
#     over = False
#     player = 'X'
#     table = [[' ', ' ', ' '],
#             [' ', ' ', ' '],
#             [' ', ' ', ' ']]
    
#     def step(self, row, column):
#         if self.table[row][column] == ' ':
#             self.table[row][column] = self.player
#             self.check()
#             if self.player == 'X':
#                 self.player = 'O'
#             else:
#                 self.player = 'X'
#     def check(self):
#         for i in range(2):
#             if ' ' != self.table[0][i] == self.table[1][i] == self.table[2][i]:
#                 print(f'{row[i]} - Выиграл')
#                 self.over = True
#             elif ' ' != self.table[i][0] == self.table[i][1] == self.table[i][2]:
#                 print(f'{row[i]} - Выиграл')
#                 self.over = True
# game = Game()
# while True:
#     if game.over:
#         break
#     row, column = map(int, input(f'Ходит {game.player}: ').split())
#     game.step(row=row-1, column=column-1)
#     for row in game.table:
#         print(*row)
#     game.check()
