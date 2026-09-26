# How many whole boxes of pizza does a family of 4 need?
family_size = 4
pieces_pizza_in_a_box = 8
family1 = int(input('How many pieces does person 1 eat? '))
family2 = int(input('How many pieces does person 2 eat? '))
family3 = int(input('How many pieces does person 3 eat? '))
family4 = int(input('How many pieces does person 4 eat? '))
pizza_pieces_needed = family1 + family2 + family3 + family4
boxes = (
pizza_pieces_needed // pieces_pizza_in_a_box+ (pizza_pieces_needed % pieces_pizza_in_a_box > 0))
pieces_ordered = boxes * pieces_pizza_in_a_box
left_pieces = pieces_ordered - pizza_pieces_needed
print(f'The number of whole pizza boxes needed is {boxes}.')
print(f'The number of leftover pieces is {left_pieces}.')


