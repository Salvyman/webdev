print('''                         ___________
                    __.-' `     `  ``--.___
 VK               .'.        `     `  `    `-.___
                 / -                   ` `  ` `  `--.
                / -                    -       `  `  `-.
               /_ -        '           .-           . ` `.  .-.
              /         |             - -'      `  / \  ` `// |
             /      `       '        -        `   ||\ `   //  |
           .'           |       '    -            || |'    `' '
         .'-       `    |  |  |    -   .     -  //       |    '
       .' -     `                     .         /       ` .-  `
     .'   - '      `   /.|'`.   |   /        /       ` o ||o' `
    J     )  '        /'  ``|`|    /         /  /       `||'.'
    |__.-'7'       .-'  \ `   ``.       |     / / /  .  '|||
      _.-'      .-'      \` '   /`.     \ ___  / '.  \\  |||
     /     __.-'         | '   /  |     |    `-----'-.\\ ( )
    /   .-'              J    /   |     |      |       \`-<
   /   /                 F   J     \    |       \       `-'
  /   /                 /   |       |   |        `-._     )
 |   /                 (    |       | \ )            `.   |
-`---`--------.---------`.   `.     \   \             /'  |   __| |   |
  .-.___`-.___ `._   ---. `.   `.___ \   \           |   /   (    |   |
 ------    `---._    `------\_____)_\_\   \_          \='|  \_ _|\__,_|
 __.-.      --.        `-----.____    '._/__`._  ___   \=/   _/       _
    .--           -.  -                        `-   `------.--.__.---'
''')

print("Welcome to Treasure Island. Find the treasure to win the game... but choose wisely, for there be monsters and other dangers on the island\n\n")

step1 = input("You're walking down a trail and come across a fork in the path.\nGo left or right? left or right\n")
if step1 == 'left':
       step2 = input("You take a left. As you walk down the path you come across a dock by the river.\nDo you wait or swim across? wait or swim\n\n")
else:
       print("You encounter a werewolf. Without any means to protect yourself, it kills you almost instantly. \nGAME OVER")
       exit(1)

if step2 == "wait":
       print("Great! Your patience paid off and a ferry comes around to escort you to the island across the river.")
       step3 = input("You navigate through the dense jungle. After hours of walking, you encounter 3 doors lined up, standing upright but they are not attached to any frame. The first one is Red, the second is Blue and the third is Grey. Which one do you open? \nRed, Blue, or Grey \n\n")
else:
       print("You make it halfway across the river but you suddenly find yourself in a riptide that carries you away into the ocean. You have drowned. \nGAME OVER")
       exit(1)

if step3 == "Red":
       print("You enter and notice a shield and remarkably-crafted silver sword lying on the cold, concrete ground in front of you. As you pick them up, the door slams shut behind you and a horde of werewolves come charging for you. You fight valiantly and slay many of the beasts, but they eventually overwhelm you. \nGAME OVER")
       exit(1)
elif step3 == "Blue":
       print("You enter the door and a wave of euphoria suddenly rushes over you. The door gently shuts behind you, but it does seem to make you worry. You feel at peace so much that you remain until dehydration overtakes you. \nGAME OVER")

else:
       print("You open the grey door and down a long, narrow hallway lies a chest with glimmering gold overfilling its contents; the chest cannot contain all of the treasure. You triumphantly make your way down the hallway, fill your pockets and your back with the treasure and leave the island for good. \nYOU WIN! CONGRATULATIONS!")