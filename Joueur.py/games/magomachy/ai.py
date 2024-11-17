from typing import List
from joueur.base_ai import BaseAI
import random

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
Expand
message.txt
17 KB
﻿
from typing import List
from joueur.base_ai import BaseAI
import random

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class AI(BaseAI):
    """ The AI you add and improve code inside to play Magomachy. """

    @property
    def game(self) -> 'games.magomachy.game.Game':
        """games.magomachy.game.Game: The reference to the Game instance this AI is playing.
        """
        return self._game # don't directly touch this "private" variable pls

    @property
    def player(self) -> 'games.magomachy.player.Player':
        """games.magomachy.player.Player: The reference to the Player this AI controls in the Game.
        """
        return self._player # don't directly touch this "private" variable pls

    def get_name(self) -> str:
        """This is the name you send to the server so your AI will control the player named this string.

        Returns:
            str: The name of your Player.
        """
        # <<-- Creer-Merge: get-name -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return "Magomachy Python Player" # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self) -> None:
        """This is called once the game starts and your AI knows its player and game. You can initialize your AI here.
        """
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your start logic
        self.player.choose_wizard("map")
        # <<-- /Creer-Merge: start -->>

    def game_updated(self) -> None:
        """This is called every time the game's state updates, so if you are tracking anything you can update it here.
        """
        # <<-- Creer-Merge: game-updated -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your game updated logic
        # <<-- /Creer-Merge: game-updated -->>

    def end(self, won: bool, reason: str) -> None:
        """This is called when the game ends, you can clean up your data and dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why your AI won or lost.
        """
        # <<-- Creer-Merge: end -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your end logic
        # <<-- /Creer-Merge: end -->>
    def action(self, wizard: 'games.magomachy.wizard.Wizard') -> int:
        """This is called whenever your wizard selects an action.

        Args:
            wizard (games.magomachy.wizard.Wizard): Wizard performs action.

        Returns:
            int: Three of the choices a Wizard can make as an action.
        """
        # <<-- Creer-Merge: Action -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # Put your game logic here for Action
        return -1
        # <<-- /Creer-Merge: Action -->>
    def move(self, wizard: 'games.magomachy.wizard.Wizard') -> int:
        """This is called whenever your wizard makes a move.

        Args:
            wizard (games.magomachy.wizard.Wizard): Wizard moves.

        Returns:
            int: Eight cardinal directions.
        """
        # <<-- Creer-Merge: Move -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # Put your game logic here for Move
        return -1
        # <<-- /Creer-Merge: Move -->>






    def run_turn(self) -> bool:
    
        print("Your turn! Here's the map:")

        if not self.player.wizard:
            print("Choosing a wizard...")
            self.player.choose_wizard("sustaining")

        # Access the current turn from the Game instance.
        current_turn = self.game.current_turn

            
        if self.game.current_turn == 0 or self.game.current_turn == 1:
            wizard = 'sustaining'
            self.player.choose_wizard(wizard)
            return True
        else:
            x = self.player.wizard.tile.x
            y = self.player.wizard.tile.y
            tile = self.game.get_tile_at(int(x), int(y))

            if current_turn % 2 != 0:
                
                # Move south until hitting a wall (checking if there is a valid tile south)
                if self.player.wizard.tile.tile_south is not None:
                    if(current_turn < 16):
                        tile = self.player.wizard.tile.tile_south
                        self.player.wizard.move(tile)
                        print("Moved South")
                    else:
                        random_number = random.randint(1, 4)
                        if random_number == 1:
                            tile = self.player.wizard.tile.tile_south
                            self.player.wizard.move(tile)
                            print("Moved South")
                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_south)
                            print("Punch South")              

                        elif random_number == 2:
                            tile = self.player.wizard.tile.tile_north
                            self.player.wizard.move(tile)
                            print("Moved North")
                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_north)
                            print("Punch North")
                        
                        elif random_number == 3:
                            tile = self.player.wizard.tile.tile_west
                            self.player.wizard.move(tile)
                            print("Moved West")                           
                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_west)
                            print("Punch West")                 
                        
                        elif random_number == 4:
                            tile = self.player.wizard.tile.tile_east
                            self.player.wizard.move(tile)
                            print("Moved East")
                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_east)
                            print("Punch East")


            # If the wizard is at (1, 8)
            elif current_turn % 2 == 0:
                # Move north until hitting a wall
                if self.player.wizard.tile.tile_north is not None:
                    if(current_turn <= 8):
                        tile = self.player.wizard.tile.tile_north
                        self.player.wizard.move(tile)
                        print("Moved North")
                    
                    else:
                        random_number = random.randint(1, 4)
                        if random_number == 1:
                            tile = self.player.wizard.tile.tile_south
                            self.player.wizard.move(tile)
                            print("Moved South")
                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_south)
                            print("Punch South")

                        elif random_number == 2:
                            tile = self.player.wizard.tile.tile_north
                            self.player.wizard.move(tile)
                            print("Moved North")
                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_north)
                            print("Punch North")
                        
                        elif random_number == 3:
                            tile = self.player.wizard.tile.tile_west
                            self.player.wizard.move(tile)
                            print("Moved West")
                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_west)
                            print("Punch West")
                        
                        elif random_number == 4:
                            tile = self.player.wizard.tile.tile_east
                            self.player.wizard.move(tile)
                            print("Moved East")
                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_east)
                            print("Punch East")


                # If the wizard is at (8, 1)
            if current_turn % 2 != 0:
                
                # Move south until hitting a wall (checking if there is a valid tile south)
                if self.player.wizard.tile.tile_south is not None:
                    if(current_turn < 16):
                        tile = self.player.wizard.tile.tile_south
                        self.player.wizard.move(tile)
                        print("Moved South")

                    else:
                        random_number = random.randint(1, 4)
                        if random_number == 1:
                            tile = self.player.wizard.tile.tile_south
                            self.player.wizard.move(tile)
                            print("Moved South")
                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_south)
                            print("Punch South")
                            

                        elif random_number == 2:
                            tile = self.player.wizard.tile.tile_north
                            self.player.wizard.move(tile)
                            print("Moved North")

                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_north)
                            print("Punch North")
                            

                        elif random_number == 3:
                            tile = self.player.wizard.tile.tile_west
                            self.player.wizard.move(tile)
                            print("Moved West")
                            
                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_west)
                            print("Punch West")
                          
                            
                        
                        elif random_number == 4:
                            tile = self.player.wizard.tile.tile_east
                            self.player.wizard.move(tile)
                            print("Moved East")
                            
                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_east)
                            print("Punch East")


            # If the wizard is at (1, 8)
            elif current_turn % 2 == 0:
                # Move north until hitting a wall
                if self.player.wizard.tile.tile_north is not None:
                    if(current_turn <= 8):
                        tile = self.player.wizard.tile.tile_north
                        self.player.wizard.move(tile)
                        print("Moved North")
                    
                    else:
                        random_number = random.randint(1, 4)
                        if random_number == 1:
                            tile = self.player.wizard.tile.tile_south
                            self.player.wizard.move(tile)
                            print("Moved South")
                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_south)
                            print("Punch South")

                        elif random_number == 2:
                            tile = self.player.wizard.tile.tile_north
                            self.player.wizard.move(tile)
                            print("Moved North")
                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_north)
                            print("Punch North")
                        
                        elif random_number == 3:
                            tile = self.player.wizard.tile.tile_west
                            self.player.wizard.move(tile)
                            print("Moved West")
                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_west)
                            print("Punch West")
                        
                        elif random_number == 4:
                            tile = self.player.wizard.tile.tile_east
                            self.player.wizard.move(tile)
                            print("Moved East")
                            self.player.wizard.cast('Punch', self.player.wizard.tile.tile_east)
                            print("Punch East")
    
            return True

        # If no other actions are possible, end the turn.
            print("Ending turn...")
        # <<-- Creer-Merge: runTurn -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # Put your game logic here for runTurn
        return True
        # <<-- /Creer-Merge: runTurn -->>




    def find_path(self, start: 'games.magomachy.tile.Tile', goal: 'games.magomachy.tile.Tile') -> List['games.magomachy.tile.Tile']:
        """A very basic path finding algorithm (Breadth First Search) that when given a starting Tile, will return a valid path to the goal Tile.

        Args:
            start (games.magomachy.tile.Tile): The starting Tile to find a path from.
            goal (games.magomachy.tile.Tile): The goal (destination) Tile to find a path to.

        Returns:
            list[games.magomachy.tile.Tile]: A list of Tiles representing the path, the the first element being a valid adjacent Tile to the start, and the last element being the goal.
        """

        if start == goal:
            # no need to make a path to here...
            return []

        # queue of the tiles that will have their neighbors searched for 'goal'
        fringe = []

        # How we got to each tile that went into the fringe.
        came_from = {}

        # Enqueue start as the first tile to have its neighbors searched.
        fringe.append(start)

        # keep exploring neighbors of neighbors... until there are no more.
        while len(fringe) > 0:
            # the tile we are currently exploring.
            inspect = fringe.pop(0)

            # cycle through the tile's neighbors.
            for neighbor in inspect.get_neighbors():
                # if we found the goal, we have the path!
                if neighbor == goal:
                    # Follow the path backward to the start from the goal and
                    # # return it.
                    path = [goal]

                    # Starting at the tile we are currently at, insert them
                    # retracing our steps till we get to the starting tile
                    while inspect != start:
                        path.insert(0, inspect)
                        inspect = came_from[inspect.id]
                    return path
                # else we did not find the goal, so enqueue this tile's
                # neighbors to be inspected

                # if the tile exists, has not been explored or added to the
                # fringe yet, and it is pathable
                if neighbor and neighbor.id not in came_from and (
                    neighbor.is_pathable()
                ):
                    # add it to the tiles to be explored and add where it came
                    # from for path reconstruction.
                    fringe.append(neighbor)
                    came_from[neighbor.id] = inspect

        # if you're here, that means that there was not a path to get to where
        # you want to go; in that case, we'll just return an empty path.
        return []

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here
    # <<-- /Creer-Merge: functions -->>
