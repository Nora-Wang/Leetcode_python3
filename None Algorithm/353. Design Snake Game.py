Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

Example:

Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)


DIRECTIONS = {'U':(-1,0), 
              'L':(0,-1), 
              'R':(0, 1), 
              'D':(1, 0)}


#将snack和food都设计为deque，满足FIFO的原则
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.p = collections.deque([(0,0)])
        self.score = 0
        
        self.width = width
        self.height = height
        
        self.food = collections.deque(food)

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        x = self.p[-1][0] + DIRECTIONS[direction][0]
        y = self.p[-1][1] + DIRECTIONS[direction][1]
        
        #out of screen
        if x < 0 or x >= self.height or y < 0 or y >= self.width:
            return -1
        
        #eat itself
        #if (x,y) == self.p[0], means the next position should be the tail of the snack; but meanwhile, the tail will become
        #self.p[1]. So it does't matter.
        if (x,y) in self.p and (x,y) != self.p[0]:
            return -1
        
        #eat food
        self.p.append((x,y))
        if self.food and [x,y] == self.food[0]:
            self.food.popleft()
            self.score += 1
        else:
            self.p.popleft()
            
        return self.score
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
