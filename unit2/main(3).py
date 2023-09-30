class player:
  def play(self):
    print('the player is platig cricket')
class batsman(player):
  def play(self):
    print('the btsman is batting')
class bowler(player):
  def play(self):
    print('the bowleris bowlling')
p=player()
p.play()
b=batsman()
b.play()
B=bowler()
B.play()