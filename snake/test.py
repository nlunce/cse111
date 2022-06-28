from main import *
import pytest

# No test functions for next_turn() and main() because they manipulate the GUI

def test_change_direction():
	
	assert change_direction('down') == 'down'
	assert change_direction('up') == 'down'

	assert change_direction('left') == 'left'
	assert change_direction('right') == 'left'

	assert change_direction('up') == 'up'
	assert change_direction('down') == 'up'

	assert change_direction('right') == 'right'
	assert change_direction('left') == 'right'
	
	
def test_check_collisions():

	class Test_Snake:
		def __init__(self, coords):
			self.coordinates = coords

	collisison_coordinates = [
		#snake self collision
		[(0, 70), (10, 70), (10, 80), (0, 80), (0, 70), (0, 60), 	(0, 50), (0, 40), (0, 30), (0, 20)],
		#snake negative x boundry
		[(-50,0)],
		#snake negative y boundry
		[(0,-50)],
		#snake exceed x boundry
		[(GAME_WIDTH+1, 0)],
		#snake exceed y boundry
		[(0, GAME_WIDTH+1)]
	]

	#Collision tests
	for coord in collisison_coordinates:
		test_snake = Test_Snake(coord)
		assert check_collisions(test_snake) == True

	#No collision test
	non_collision_coordinates = [(0,0)]
	test_snake = Test_Snake(non_collision_coordinates)
	assert check_collisions(test_snake) == False


pytest.main(['-v', '--tb=line', '-rN', __file__])