from math import sqrt

print('Pythagorean theorem calculator! Calculate your triangle sides.')
print('Assume the sides are a, b, c and c is the hypotenuse (the side opposite the right angle)')
formula = input('Which side (a, b, c) do you wish to calculate? side> ')

if formula == 'c':
	side_a = int(input('Input the length of side a: '))
	side_b = int(input('Input the length of side b: '))

	side_c = sqrt(side_a * side_a + side_b * side_b)
	
	print('The length of side c is: ' )
	print(round(side_c,2))

elif formula == 'a':
    side_b = int(input('Input the length of side b: '))
    side_c = int(input('Input the length of side c: '))
    
    side_a = sqrt((side_c * side_c) - (side_b * side_b))
    
    print('The length of side a is' )
    print(round(side_a,2))

elif formula == 'b':
    side_a = int(input('Input the length of side a: '))
    side_c = int(input('Input the length of side c: '))
        
    side_c = sqrt(side_c * side_c - side_a * side_a)
    
    print('The length of side b is')
    print(round(side_c,2))

else:
	print('Please select a side between a, b, c')
	