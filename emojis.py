#! /usr/bin/env python3

''' Test printing emoji codes '''

names = ('\N{grinning face}',
         '\N{grinning face with smiling eyes}',
         '\N{rolling on the floor laughing}',
         '\N{face with tears of joy}',
         '\N{slightly smiling face}',
         '\N{upside-down face}',
         '\N{winking face}',
         '\N{smiling face with smiling eyes}',
         '\N{smiling face with halo}',
         '\N{thinking face}',
         '\N{skull and crossbones}',
         '\N{see-no-evil monkey}',
         '\N{hear-no-evil monkey}',
         '\N{speak-no-evil monkey}',
         '\N{monkey face}',
         '\N{monkey}',
         '\N{kiss mark}',
         '\N{penguin}',
         '\N{eagle}')

for i in names:
    print(i, end="  ")
print()
